# nanoplot

Tiny package that ships Tomás' Matplotlib style and helpers.

## Features

- Custom matplotlib style with optimized settings for scientific plots
- Helper functions for proper colorbar positioning with imshow plots
- Context manager for temporary style application
- Optional integration with SciencePlots styles

## Install

```bash
# From PyPI (when published)
uv add nanoplot

# From Git repository
# For public repositories:
uv add git+https://github.com/nanolab-fcfm/nanoplot.git

# For private repositories (requires authentication):
# Option 1: SSH (recommended)
uv add git+ssh://git@github.com/nanolab-fcfm/nanoplot.git

# Option 2: HTTPS with GitHub CLI
gh auth login
uv add git+https://github.com/nanolab-fcfm/nanoplot.git

# Option 3: HTTPS with personal access token
# Will prompt for username/token if repository is private
uv add git+https://github.com/nanolab-fcfm/nanoplot.git

# Local development
pip install -e .
# (or) pip install .    # for a regular install
# optional: pip install ".[science]"  # if you want SciencePlots styles available
```

## Use

```python
import matplotlib.pyplot as plt
import nanoplot as nplt

# Easiest: apply your default style
nplt.apply()  # uses SciencePlots 'science','nature' if available, then your style

# Or use as a context manager (auto-reverts on exit)
with tp.style():
    plt.plot([0,1],[0,1])
    plt.show()

# Or load just the mplstyle path yourself
plt.style.use(nplt.style_path())  # same as tp.apply() but without extra logic

# For imshow plots with proper colorbars:
im, cbar = nplt.imshow_with_colorbar(data)
# or
fig, axes, add_colorbar = nplt.subplots_with_colorbar(2, 2)
im = axes[0, 0].imshow(data)
cbar = add_colorbar(im, axes[0, 0])
```
```
