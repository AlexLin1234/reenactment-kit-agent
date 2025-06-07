"""Simple supplier recommender used by the demo frontend."""

from __future__ import annotations


_SUPPLIER_MAP: dict[str, list[str]] = {
    "longbow": ["Traditional Archery Supply", "Woodland Longbows"],
    "quiver": ["Traditional Archery Supply"],
    "helmet": ["Age of Craft", "Kult of Athena"],
    "breastplate": ["Medieval Armoury"],
    "sword": ["Albion Swords", "Kult of Athena"],
    "shield": ["Kult of Athena"],
    "gambeson": ["Historic Enterprises"],
}


def recommend_suppliers(item: str) -> list[str]:
    """Return a list of supplier names for ``item``.

    If the item is not known, a short list of generic suggestions is
    returned to encourage the user to continue their own search.
    """

    lowered = item.lower()
    for key, suppliers in _SUPPLIER_MAP.items():
        if key in lowered:
            return suppliers

    return [
        "Check with local reenactment groups",
        "Search online specialty vendors",
    ]
