# Changelog

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
