"""
Plot the different types of graphs using the Matplotlib library.

Requirements:
    pip install matplotlib numpy

Run:
    python matplotlib_graphs.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Reproducible random data
rng = np.random.default_rng(42)


def line_plot(ax):
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x), label="sin(x)")
    ax.plot(x, np.cos(x), label="cos(x)", linestyle="--")
    ax.set_title("Line Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()


def bar_chart(ax):
    languages = ["Python", "Java", "C++", "JavaScript", "Go"]
    popularity = [85, 70, 55, 80, 40]
    ax.bar(languages, popularity, color="steelblue")
    ax.set_title("Bar Chart")
    ax.set_ylabel("Popularity")


def horizontal_bar_chart(ax):
    fruits = ["Apple", "Banana", "Cherry", "Mango"]
    sales = [30, 45, 20, 50]
    ax.barh(fruits, sales, color="seagreen")
    ax.set_title("Horizontal Bar Chart")
    ax.set_xlabel("Sales")


def histogram(ax):
    data = rng.normal(loc=50, scale=10, size=1000)
    ax.hist(data, bins=25, color="orchid", edgecolor="black")
    ax.set_title("Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")


def scatter_plot(ax):
    x = rng.random(80)
    y = x + rng.normal(0, 0.1, 80)
    sizes = rng.random(80) * 200
    ax.scatter(x, y, s=sizes, c=y, cmap="viridis", alpha=0.7)
    ax.set_title("Scatter Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def pie_chart(ax):
    labels = ["Food", "Rent", "Transport", "Savings"]
    sizes = [30, 40, 10, 20]
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Pie Chart")


def box_plot(ax):
    data = [rng.normal(m, 1.5, 100) for m in (0, 2, 4)]
    ax.boxplot(data, labels=["A", "B", "C"])
    ax.set_title("Box Plot")


def area_plot(ax):
    x = np.arange(1, 11)
    y = x ** 1.5
    ax.fill_between(x, y, alpha=0.5, color="orange")
    ax.plot(x, y, color="darkorange")
    ax.set_title("Area Plot")


def step_plot(ax):
    x = np.arange(10)
    y = rng.integers(1, 10, 10)
    ax.step(x, y, where="mid", color="crimson")
    ax.set_title("Step Plot")


def stem_plot(ax):
    x = np.arange(0, 10)
    y = np.sin(x)
    ax.stem(x, y)
    ax.set_title("Stem Plot")


def error_bar_plot(ax):
    x = np.arange(1, 6)
    y = x * 2
    ax.errorbar(x, y, yerr=rng.random(5), fmt="o-", capsize=4)
    ax.set_title("Error Bar Plot")


def heatmap(ax):
    data = rng.random((8, 8))
    im = ax.imshow(data, cmap="hot")
    ax.figure.colorbar(im, ax=ax, fraction=0.046)
    ax.set_title("Heatmap")


def violin_plot(ax):
    data = [rng.normal(m, 1, 200) for m in (0, 1.5, 3)]
    ax.violinplot(data, showmeans=True)
    ax.set_title("Violin Plot")


def stacked_bar(ax):
    categories = ["Q1", "Q2", "Q3", "Q4"]
    a = np.array([20, 35, 30, 35])
    b = np.array([25, 32, 34, 20])
    ax.bar(categories, a, label="Product A")
    ax.bar(categories, b, bottom=a, label="Product B")
    ax.set_title("Stacked Bar Chart")
    ax.legend()


def main():
    plots = [
        line_plot, bar_chart, horizontal_bar_chart, histogram,
        scatter_plot, pie_chart, box_plot, area_plot,
        step_plot, stem_plot, error_bar_plot, heatmap,
        violin_plot, stacked_bar,
    ]

    cols = 4
    rows = -(-len(plots) // cols)  # ceiling division
    fig, axes = plt.subplots(rows, cols, figsize=(20, 4.5 * rows))
    axes = axes.flatten()

    for ax, plot in zip(axes, plots):
        plot(ax)

    # Hide unused subplot slots
    for ax in axes[len(plots):]:
        ax.axis("off")

    fig.suptitle("Different Types of Graphs using Matplotlib", fontsize=18)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig("matplotlib_graphs.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
