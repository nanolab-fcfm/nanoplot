# nanoplot

Tiny package that ships Tomás' Matplotlib style and helpers.

## Install

```bash
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
```
