# Home Assistant Add-on: Immich DLNA

Run Immich-DLNA inside Home Assistant so DLNA clients can browse and play media from Immich.

## Required options

- `immich_url`
- `immich_api_token`
- `http_port` (defaults to `8200`)

## Notes

- This add-on uses `host_network: true`, which is recommended for DLNA/SSDP discovery.
- Most advanced DLNA settings use safe internal defaults to keep setup simple.
