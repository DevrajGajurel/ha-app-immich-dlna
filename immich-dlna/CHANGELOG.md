# Changelog

## 0.1.11

- Consolidate venv install into one `RUN` using `/opt/venv/bin/pip` only (no system `pip3`), avoiding PEP 668 failures and stale layer caches when updating from 0.1.9.

## 0.1.10

- Fix Docker build on Home Assistant base images: install `immich-dlna` into `/opt/venv` to satisfy PEP 668 (externally managed system Python).
- Run the service via `/opt/venv/bin/immich-dlna` so startup is reliable under s6.

## 0.1.9

- Remove deprecated `build.yaml` and keep build parameters directly in `Dockerfile` per current Home Assistant builder guidance.
- Update add-on base image default to `ghcr.io/home-assistant/base:latest`.

## 0.1.8

- Harden DLNA base URL auto-detection to avoid startup failure when specific network commands are unavailable.
- Add route-based IP detection with safe fallbacks so the add-on always starts and still advertises reachable media URLs.

## 0.1.7

- Replace unavailable `bashio::env.exists` call with a portable shell environment check in the add-on startup script.
- Fix startup crash loop caused by `command not found` in Home Assistant base images.

## 0.1.6

- Auto-detect a non-loopback host IP and set `IMMICH_DLNA_BASE_URL` at startup when not provided.
- Fix media playback for DLNA clients by avoiding loopback (`127.0.0.1`) media URLs in Home Assistant add-on deployments.

## 0.1.5

- Add Docker build cache-busting argument (`APP_BUILD_VERSION`) to ensure updated source is reinstalled during add-on builds.
- Bump add-on version to guarantee Home Assistant offers an in-place update path.

## 0.1.4

- Reduce SSDP discovery log noise by moving per-request M-SEARCH logs to debug level.
- Add startup summary logs for DLNA-exposed content (timeline count, album count, album names).
- Bump add-on version so Home Assistant can deliver in-place upgrades without uninstall/reinstall.

## 0.1.3

- Simplify Home Assistant add-on configuration to only `immich_url`, `immich_api_token`, and `http_port` (default `8200`).
- Keep advanced runtime settings on internal defaults to reduce setup complexity.

## 0.1.2

- Add Home Assistant add-on branding assets as `icon.png` and `logo.png` so the logo appears in the UI.

## 0.1.1

- Include Python package files in the add-on repository so `pip install git+...` succeeds during Home Assistant image builds.
- Update add-on metadata URLs and branding assets.

## 0.1.0

- Initial Home Assistant add-on packaging for Immich-DLNA.
