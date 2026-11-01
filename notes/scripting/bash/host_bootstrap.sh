#!/usr/bin/env bash
# Prepare a fresh Ubuntu 24.04 host to run homelab stack
#
#
#   ./main.sh           # print what would happen, change nothing
#   ./main.sh --apply   # execute (uses sudo)
#
# Covers only what blocks or protects the stack: Run BEFORE restoring volumes.
# Deliberately NOT covered: zsh/dotfiles, LVM layout (do at install time,
# see the sizing note at the bottom)
set -euo pipefail

APPLY=0
[[ "${1:-}" == "--apply" ]] && APPLY=1
TARGET_USER="${TARGET_USER:-$(id -un)}"

run()  { if ((APPLY)); then echo "  + $*"; eval "$@"; else echo "  would: $*"; fi; }
skip() { echo "  ok (already done): $*"; }
step() { echo; echo "── $* ────────────────────────────────"; }

((APPLY)) || echo "=== DRY RUN — nothing will change. Pass --apply to execute. ==="
[[ $EUID -eq 0 ]] && { echo "Run as your normal user, not root (it uses sudo where needed)."; exit 1; }
. /etc/os-release
[[ "${VERSION_ID:-}" == "24.04" ]] || echo "!! Built for Ubuntu 24.04; this is ${PRETTY_NAME:-unknown}. The docker.sources suite below says 'noble'."

step "1/3  Docker CE — from Docker's repo, NOT Ubuntu's docker.io"
if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
  skip "docker $(docker --version 2>/dev/null | awk '{print $3}' | tr -d ,) + compose plugin present"
else
  run "sudo apt-get update -qq"
  run "sudo apt-get install -y ca-certificates curl"
  run "sudo install -m 0755 -d /etc/apt/keyrings"
  run "sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc"
  run "sudo chmod a+r /etc/apt/keyrings/docker.asc"
  run "sudo tee /etc/apt/sources.list.d/docker.sources >/dev/null <<'SRC'
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: noble
Components: stable
Architectures: amd64
Signed-By: /etc/apt/keyrings/docker.asc
SRC"
  run "sudo apt-get update -qq"
  run "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
  run "sudo systemctl enable --now docker"
fi
if id -nG "$TARGET_USER" | tr ' ' '\n' | grep -qx docker; then
  skip "$TARGET_USER already in docker group"
else
  run "sudo usermod -aG docker '$TARGET_USER'"
  echo "  !! log out and back in before docker works without sudo"
fi

step "2/3  caddy_proxy network — external, created by NO compose file"
if docker network inspect caddy_proxy >/dev/null 2>&1; then
  skip "caddy_proxy exists"
else
  run "docker network create caddy_proxy"
fi

step "3/3  firewall"
# NOTE: published Docker ports BYPASS ufw — the daemon writes its own iptables DOCKER-USER
# chain. ufw here protects the HOST, not the containers. Only Caddy (80/443) and Gitea's
# sshd (2222) are published by this stack.
if ! command -v ufw >/dev/null 2>&1; then run "sudo apt-get install -y ufw"; fi
run "sudo ufw allow ssh"          # first, so enabling cannot lock you out
run "sudo ufw allow 80/tcp"
run "sudo ufw allow 443/tcp"
run "sudo ufw allow 2222/tcp"
run "sudo ufw --force enable"
# sshd hardening.
if [[ -s "$HOME/.ssh/authorized_keys" ]]; then
  run "sudo tee /etc/ssh/sshd_config.d/99-hardening.conf >/dev/null <<'SSHD'
PermitRootLogin no
PasswordAuthentication no
SSHD"
  run "sudo systemctl restart ssh"
else
  echo "  !! ~/.ssh/authorized_keys is empty — NOT disabling password auth (would lock you out)."
  echo "     Install your key, then re-run. Old host had 2 ed25519 keys: alex@workstation, alex@laptop"
fi

cat <<'DONE'

Disk sizing, if you are still partitioning (not automated — do it at install time):
  Leave free extents in the VG so you can `lvextend` later instead of guessing now.
DONE

