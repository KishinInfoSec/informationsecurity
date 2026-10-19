---
title: preventing-server-side-parameter-pollution
tags: [api-testing, server-side-parameter-pollution, type/reference, phase/hardening, platform/api]
---

# Preventing server-side parameter pollution

To prevent server-side parameter pollution, use an allowlist to define characters that don't need encoding, and make sure all other user input is encoded before it's included in a server-side request. You should also make sure that all input adheres to the expected format and structure.
