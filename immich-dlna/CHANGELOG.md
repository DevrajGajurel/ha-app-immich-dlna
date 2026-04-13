# Changelog

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
