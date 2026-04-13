# Home Assistant Add-on: Immich DLNA

Run Immich-DLNA inside Home Assistant so DLNA clients can browse and play media from Immich.

## Required options

- `immich_url`
- `immich_api_token`

## Notes

- This add-on uses `host_network: true`, which is recommended for DLNA/SSDP discovery.
- If your Immich uses self-signed certificates, set `immich_verify_ssl` to `false`.
