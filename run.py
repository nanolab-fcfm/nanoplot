#!/usr/bin/env python3
"""Demo script for nanoplot showcasing various plot types."""

import matplotlib.pyplot as plt
import numpy as np
import nanoplot as nplt

# Apply the style
nplt.apply()

# Create a figure with multiple subplots
n, m = 2, 3
fig, axes = plt.subplots(n, m, figsize=(20 * m, 20 * n))
fig.suptitle("nanoplot Demo - Various Plot Types", fontsize=60, y=0.95)

# 1. Line plot with markers
ax1 = axes[0, 0]
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)
ax1.plot(x, y1, marker="o", label="sin(x)", markersize=8)
ax1.plot(x, y2, marker="s", label="cos(x)", markersize=8)
ax1.set_title("Line Plot")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Scatter plot
ax2 = axes[0, 1]
np.random.seed(42)
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
ax2.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6)
ax2.set_title("Scatter Plot")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# 3. Histogram
ax3 = axes[0, 2]
data = np.random.normal(0, 1, 1000)
ax3.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
ax3.set_title("Histogram")
ax3.set_xlabel("Value")
ax3.set_ylabel("Frequency")

# 4. Heatmap
ax4 = axes[1, 0]
data_heatmap = np.random.rand(10, 10)
im = ax4.imshow(data_heatmap, cmap='viridis', aspect='auto')
ax4.set_title("Heatmap")
plt.colorbar(im, ax=ax4)

# 5. Bar plot
ax5 = axes[1, 1]
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
bars = ax5.bar(categories, values, color=['red', 'blue', 'green', 'orange', 'purple'])
ax5.set_title("Bar Plot")
ax5.set_xlabel("Categories")
ax5.set_ylabel("Values")
# Add value labels on bars
for bar, value in zip(bars, values):
    ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             str(value), ha='center', va='bottom', fontsize=30)

# 6. Box plot
ax6 = axes[1, 2]
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
ax6.boxplot(data_box, labels=['Group 1', 'Group 2', 'Group 3'])
ax6.set_title("Box Plot")
ax6.set_xlabel("Groups")
ax6.set_ylabel("Values")

plt.tight_layout(rect=[0, 0, 1, 0.92])  # Leave space at top for title
plt.savefig("demo_plot.pdf", format="pdf", bbox_inches="tight")
print("Comprehensive demo plot saved as demo_plot.pdf")
