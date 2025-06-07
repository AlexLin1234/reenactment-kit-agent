"""Utility for pulling reference images from museum APIs."""

from __future__ import annotations

import logging

import requests

logger = logging.getLogger(__name__)


def _search_met(item: str) -> dict[str, str] | None:
    """Search the Metropolitan Museum of Art collection API."""
    search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    try:
        resp = requests.get(search_url, params={"q": item, "hasImages": True}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:  # pragma: no cover - network call
        logger.warning("MET search failed: %s", exc)
        return None

    ids = data.get("objectIDs")
    if not ids:
        return None

    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{ids[0]}"
    try:
        resp = requests.get(object_url, timeout=10)
        resp.raise_for_status()
        obj = resp.json()
    except Exception as exc:  # pragma: no cover - network call
        logger.warning("MET object retrieval failed: %s", exc)
        return None

    image = obj.get("primaryImageSmall") or obj.get("primaryImage")
    if not image:
        return None

    return {
        "image_url": image,
        "museum": "Metropolitan Museum of Art",
    }


def _search_royal_armories(item: str) -> dict[str, str] | None:
    """Search the Royal Armouries collection API."""
    search_url = "https://collectionapi.royalarmouries.org/objects/search"
    try:
        resp = requests.get(search_url, params={"q": item, "pageSize": 1}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:  # pragma: no cover - network call
        logger.warning("Royal Armouries search failed: %s", exc)
        return None

    items = data.get("data")
    if not items:
        return None

    obj = items[0]
    attributes = obj.get("attributes", {})
    image = attributes.get("imageThumbURL") or attributes.get("imageUrl")
    if not image:
        return None

    return {
        "image_url": image,
        "museum": "Royal Armouries",
    }


def fetch_references(item: str) -> dict:
    """Return reference image information for ``item``.

    The function attempts to query several museum APIs for the first
    available image. Currently supported sources are the Metropolitan
    Museum of Art and the Royal Armouries. If no result is found, an empty
    dictionary is returned.
    """

    for search_func in (_search_met, _search_royal_armories):
        result = search_func(item)
        if result:
            return result

    logger.info("No reference found for '%s'", item)
    return {"image_url": "", "museum": ""}
