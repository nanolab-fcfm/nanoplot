from __future__ import annotations
import contextlib
from importlib import resources
from typing import Iterable, List

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


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


def imshow_with_colorbar(data, ax=None, **kwargs):
    """
    Create an imshow plot with a properly sized colorbar.
    
    This function ensures the colorbar has the full height of the image
    by using make_axes_locatable to create a proper colorbar axis.
    
    Parameters
    ----------
    data : array-like
        The data to display with imshow
    ax : matplotlib.axes.Axes, optional
        The axes to plot on. If None, uses the current axes.
    **kwargs : dict
        Additional arguments passed to plt.imshow
        
    Returns
    -------
    im : matplotlib.image.AxesImage
        The imshow object
    cbar : matplotlib.colorbar.Colorbar
        The colorbar object
    """
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    
    if ax is None:
        ax = plt.gca()
    
    # Create the imshow plot
    im = ax.imshow(data, **kwargs)
    
    # Create a divider for the existing axes instance
    divider = make_axes_locatable(ax)
    
    # Append axes to the right of ax, with 20% of the width
    cax = divider.append_axes("right", size="5%", pad=0.05)
    
    # Create the colorbar
    cbar = plt.colorbar(im, cax=cax)
    
    return im, cbar


def subplots_with_colorbar(nrows=1, ncols=1, **kwargs):
    """
    Create subplots with proper colorbar support.
    
    This function creates subplots and returns a helper function
    that can be used to add colorbars to any of the subplots.
    
    Parameters
    ----------
    nrows, ncols : int
        Number of rows and columns for subplots
    **kwargs : dict
        Additional arguments passed to plt.subplots
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object
    axes : array-like
        The axes objects
    add_colorbar : function
        A function that takes (im, ax) and returns a colorbar
    """
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    
    fig, axes = plt.subplots(nrows, ncols, **kwargs)
    
    def add_colorbar(im, ax):
        """Add a colorbar to the given axes."""
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        return plt.colorbar(im, cax=cax)
    
    return fig, axes, add_colorbar
