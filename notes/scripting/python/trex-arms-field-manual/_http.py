#!/usr/bin/env python3
"""Shared polite-HTTP helpers.

Provides a thread-safe global rate limiter, Retry-After parsing, and jittered
exponential backoff. All network scripts import from here so rate limiting is
applied consistently across enumeration, URL resolution, and downloads.

Tune with each script's --rate (requests per second, global across workers).
"""
import os, time, random, threading
import urllib.request, urllib.error
from email.utils import parsedate_to_datetime

DEFAULT_UA = "Mozilla/5.0 (X11; Linux x86_64) VaultDownloader/1.0"
RETRY_STATUS = {408, 425, 429, 500, 502, 503, 504}


class RateLimiter:
    """Global min-interval limiter (thread-safe), shared by all workers."""

    def __init__(self, rate_per_sec):
        self.interval = 1.0 / rate_per_sec if rate_per_sec and rate_per_sec > 0 else 0.0
        self._lock = threading.Lock()
        self._next = 0.0

    def wait(self):
        if self.interval <= 0:
            return
        with self._lock:
            now = time.monotonic()
            if self._next < now:
                self._next = now
            delay = self._next - now
            self._next += self.interval
        if delay > 0:
            time.sleep(delay)


def parse_retry_after(value):
    """Seconds to wait, from Retry-After as delta-seconds or HTTP-date."""
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        dt = parsedate_to_datetime(value)
        return max(0.0, dt.timestamp() - time.time())
    except Exception:
        return None


def _retry_delay(attempt, retry_after=None):
    if retry_after is not None:
        base = min(retry_after, 120.0)
    else:
        base = min(60.0, 1.5 * (2 ** attempt))
    return base + random.uniform(0, min(base, 3.0) * 0.25)


def _open(url, limiter, timeout, headers):
    h = {"User-Agent": DEFAULT_UA}
    if headers:
        h.update(headers)
    if limiter:
        limiter.wait()
    req = urllib.request.Request(url, headers=h)
    return urllib.request.urlopen(req, timeout=timeout)


def fetch_bytes(url, limiter=None, timeout=60, retries=6, headers=None):
    """GET a URL, retrying 429/5xx with Retry-After + backoff. Returns bytes."""
    last = None
    for attempt in range(retries):
        try:
            with _open(url, limiter, timeout, headers) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in RETRY_STATUS or attempt == retries - 1:
                raise
            ra = parse_retry_after(e.headers.get("Retry-After")) if e.headers else None
            time.sleep(_retry_delay(attempt, ra))
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            last = e
            if attempt == retries - 1:
                raise
            time.sleep(_retry_delay(attempt))
    if last:
        raise last
    raise RuntimeError("request failed")


def stream_to(url, dest, limiter=None, timeout=60, retries=6, on_chunk=None):
    """Download url -> dest atomically (.part then rename), with retries."""
    tmp = dest + ".part"
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    last = None
    for attempt in range(retries):
        try:
            if os.path.exists(tmp):
                try:
                    os.remove(tmp)
                except OSError:
                    pass
            with _open(url, limiter, timeout, None) as r, open(tmp, "wb") as f:
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    f.write(chunk)
                    if on_chunk:
                        on_chunk(len(chunk))
            size = os.path.getsize(tmp)
            if size < 1000:
                raise IOError("response too small (%d bytes)" % size)
            os.replace(tmp, dest)
            return size
        except urllib.error.HTTPError as e:
            last = e
            try:
                os.remove(tmp)
            except OSError:
                pass
            if e.code not in RETRY_STATUS or attempt == retries - 1:
                raise
            ra = parse_retry_after(e.headers.get("Retry-After")) if e.headers else None
            time.sleep(_retry_delay(attempt, ra))
        except Exception as e:
            last = e
            try:
                os.remove(tmp)
            except OSError:
                pass
            if attempt == retries - 1:
                raise
            time.sleep(_retry_delay(attempt))
    if last:
        raise last
    raise RuntimeError("download failed")
