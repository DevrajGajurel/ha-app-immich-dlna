# Immich DLNA Home Assistant Add-on Repository

This repository contains a Home Assistant add-on for running `immich-dlna`.

Before publishing, replace placeholder GitHub values in:

- `repository.yaml`
- `immich-dlna/config.yaml` (`url`)
- `immich-dlna/build.yaml` (`APP_GIT_URL`, `APP_GIT_REF`)

## Add this repository to Home Assistant

1. In Home Assistant, go to **Settings -> Add-ons -> Add-on Store**.
2. Open the menu (three dots) and click **Repositories**.
3. Add your GitHub repository URL for this folder.
4. Install **Immich DLNA** from the add-on store.

## Configuration

Set these required options in the add-on:

- `immich_url`: your Immich base URL (for example `https://immich.example.com/api`)
- `immich_api_token`: Immich API token

Optional options are exposed in the add-on UI with defaults matching the app defaults.
