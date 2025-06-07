"""Utility functions for suggesting a reenactment persona."""

from __future__ import annotations

import re


def _format_century(value: str) -> str:
    """Normalize a century string to an ordinal form.

    Parameters
    ----------
    value
        The user provided century value which may be a plain number
        (``"15"`` or ``15``) or already contain a suffix such as ``"15th"``.
    """

    digits = re.match(r"(\d+)", str(value).strip())
    if not digits:
        return value.strip()

    number = int(digits.group(1))
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
    return f"{number}{suffix}"


def suggest_persona(century: str, region: str, role: str) -> str:
    """Return a formatted persona description.

    The function tries to clean up the provided values so that the
    resulting string is easy to read and consistent. This helps the
    frontend display a reasonable suggestion without having to rely on
    an LLM call.
    """

    century_formatted = _format_century(century)
    region_formatted = region.strip().title()
    role_formatted = role.strip().lower()
    return f"{century_formatted}-century {region_formatted} {role_formatted}"
