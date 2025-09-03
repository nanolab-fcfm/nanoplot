#!/usr/bin/env python3
"""Demo script for nanoplot."""

import matplotlib.pyplot as plt
import nanoplot as nplt
# Apply the style
nplt.apply()

# Create a demo plot
plt.plot([0,1,2],[0,1,4], marker="o", label="demo")
plt.legend()
plt.title("nanoplot demo")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
