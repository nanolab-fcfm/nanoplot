from __future__ import annotations
import contextlib
from importlib import resources
from typing import Iterable, List

import matplotlib as mpl
import matplotlib.pyplot as plt


def style_path(name: str = "default") -> str:
    """
    Return the absolute path to an included .mplstyle file.
    """
    return str(resources.files(__package__) / "styles" / f"{name}.mplstyle")


def _maybe_add(base: List[str], style_name: str) -> None:
    """
    Append style_name if available (so missing SciencePlots won't break).
    """
    try:
        # Fast path: check style list first to avoid noisy exceptions
        if style_name in plt.style.available:
            base.append(style_name)
        else:
            # Try a direct use & revert; sometimes 3rd-party styles get
            # discovered only on first call
            plt.style.use(style_name)
            base.append(style_name)
    except Exception:
        # Silently skip if not present
        pass


def apply(
    *,
    include_science_nature: bool = True,
    style_name: str = "default",
    extra: Iterable[str] | None = None,
) -> None:
    """
    Apply Tomás' style, optionally layering SciencePlots' 'science' and 'nature'.

    Parameters
    ----------
    include_science_nature : bool
        If True, try to apply 'science' and 'nature' (skipped if unavailable).
    style_name : str
        Which bundled style to use (corresponds to 'styles/{style_name}.mplstyle').
    extra : Iterable[str] | None
        Additional styles (names or file paths) to layer BEFORE the bundled style.
    """
    chain: List[str] = []

    if include_science_nature:
        _maybe_add(chain, "science")
        _maybe_add(chain, "nature")

    if extra:
        chain.extend(extra)

    chain.append(style_path(style_name))
    plt.style.use(chain)


@contextlib.contextmanager
def style(
    *,
    include_science_nature: bool = True,
    style_name: str = "default",
    extra: Iterable[str] | None = None,
):
    """
    Context manager that applies the style, then restores previous rcParams.
    """
    old = mpl.rcParams.copy()
    try:
        apply(
            include_science_nature=include_science_nature,
            style_name=style_name,
            extra=extra,
        )
        yield
    finally:
        mpl.rcParams.update(old)
