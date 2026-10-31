from __future__ import annotations

from html import escape
from urllib.parse import quote

from aiohttp import web

from immich_dlna.dlna.catalog import ContentCatalog
from immich_dlna.dlna.model import ROOT_ID, Container, MediaItem, parse_asset_id
from immich_dlna.immich import ImmichError

PAGE_SIZE = 60

_STYLE = """
*{box-sizing:border-box}
body{margin:0;background:#101418;color:#e8eaed;font-family:system-ui,sans-serif}
header{padding:14px 20px;background:#1a2027;position:sticky;top:0;z-index:2}
header h1{margin:0;font-size:1.1rem;font-weight:600}
nav{font-size:.85rem;margin-top:4px;color:#9aa0a6}
a{color:inherit;text-decoration:none}
nav a{color:#8ab4f8}
main{padding:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px}
.tile{display:block;background:#1a2027;border-radius:10px;overflow:hidden;position:relative}
.tile:hover{outline:2px solid #8ab4f8}
.thumb{aspect-ratio:1;background:#232a32 center/cover no-repeat;display:flex;align-items:center;justify-content:center;font-size:3rem}
.label{padding:8px 10px;font-size:.85rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.badge{position:absolute;top:8px;right:8px;background:#000a;border-radius:4px;padding:2px 6px;font-size:.75rem}
.pager{display:flex;justify-content:space-between;margin-top:20px;color:#8ab4f8}
.empty,.error{color:#9aa0a6;padding:40px 0;text-align:center}
.error{color:#f28b82}
"""


def _page(title: str, crumbs: str, body: str) -> web.Response:
    html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{escape(title)}</title><style>{_STYLE}</style></head><body>"
        f"<header><h1>{escape(title)}</h1><nav>{crumbs}</nav></header>"
        f"<main>{body}</main></body></html>"
    )
    return web.Response(text=html, content_type="text/html", charset="utf-8")


def _href(object_id: str, start: int = 0) -> str:
    # Relative on purpose: Home Assistant ingress serves us under a path prefix.
    return f"?id={quote(object_id, safe='')}&start={start}"


def _tile(entry: Container | MediaItem) -> str:
    label = escape(entry.title)
    if isinstance(entry, Container):
        count = f" ({entry.child_count})" if entry.child_count else ""
        return (
            f"<a class='tile' href='{_href(entry.object_id)}'>"
            f"<div class='thumb'>&#128193;</div><div class='label'>{label}{count}</div></a>"
        )
    asset_id = parse_asset_id(entry.object_id) or ""
    style = f" style=\"background-image:url('media/asset/{quote(asset_id)}/thumbnail')\""
    badge = "<span class='badge'>&#9654; Video</span>" if entry.is_video else ""
    icon = "&#127902;" if entry.is_video else ""
    return (
        f"<a class='tile' href='media/asset/{quote(asset_id)}' target='_blank'>"
        f"<div class='thumb'{style}>{icon}</div>{badge}<div class='label'>{label}</div></a>"
    )


def register_ui(app: web.Application, catalog: ContentCatalog, server_name: str) -> None:
    async def browse_page(request: web.Request) -> web.Response:
        object_id = request.query.get("id", ROOT_ID) or ROOT_ID
        try:
            start = max(int(request.query.get("start", "0")), 0)
        except ValueError:
            start = 0

        try:
            meta, _ = await catalog.browse(object_id, "BrowseMetadata", 0, 1)
            entries, total = await catalog.browse(object_id, "BrowseDirectChildren", start, PAGE_SIZE)
        except ImmichError as error:
            return _page(server_name, "", f"<div class='error'>Immich error: {escape(str(error))}</div>")

        current = meta[0] if meta else None
        title = current.title if current else server_name
        crumbs = f"<a href='{_href(ROOT_ID)}'>{escape(server_name)}</a>"
        if current is not None and object_id != ROOT_ID:
            parent_id = current.parent_id
            if parent_id not in {ROOT_ID, "-1"}:
                crumbs += f" / <a href='{_href(parent_id)}'>{escape(parent_id.capitalize())}</a>"
            crumbs += f" / {escape(current.title)}"

        body = "<div class='grid'>" + "".join(_tile(e) for e in entries) + "</div>" if entries else (
            "<div class='empty'>Nothing here.</div>"
        )
        if total > PAGE_SIZE:
            prev_link = f"<a href='{_href(object_id, start - PAGE_SIZE)}'>&larr; Previous</a>" if start > 0 else "<span></span>"
            next_link = (
                f"<a href='{_href(object_id, start + PAGE_SIZE)}'>Next &rarr;</a>"
                if start + PAGE_SIZE < total
                else "<span></span>"
            )
            body += (
                f"<div class='pager'>{prev_link}<span>{start + 1}&ndash;{min(start + PAGE_SIZE, total)} of {total}</span>"
                f"{next_link}</div>"
            )
        return _page(title if object_id != ROOT_ID else server_name, crumbs, body)

    app.router.add_get("/", browse_page)
