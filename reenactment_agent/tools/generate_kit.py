"""Generate a very small kit list based on the persona description."""

from __future__ import annotations


def _kit_for_role(role: str) -> list[str]:
    """Return common equipment for the given role."""

    role = role.lower()
    if "archer" in role:
        return [
            "longbow",
            "quiver of arrows",
            "gambeson",
            "belt pouch",
            "leather boots",
        ]
    if "knight" in role:
        return [
            "helmet",
            "breastplate",
            "gauntlets",
            "sword",
            "shield",
        ]
    if "pikeman" in role or "infantry" in role:
        return [
            "pikestaff",
            "helmet",
            "gambeson",
            "belt",
        ]
    # Generic fallback
    return [
        "tunic",
        "belt",
        "knife",
    ]


def generate_kit_list(persona: str) -> list[str]:
    """Return a list of historical gear items for ``persona``."""

    role_part = persona.lower()
    kit = _kit_for_role(role_part)
    return kit
