import random
import matplotlib.pyplot as plt

def estimate_pi(iterations=10000):
    inside = 0
    for _ in range(iterations):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / iterations

def plot_monte_carlo(iterations=5000):
    xs, ys, colors = [], [], []
    inside = 0
    for _ in range(iterations):
        x, y = random.random(), random.random()
        xs.append(x)
        ys.append(y)
        if x**2 + y**2 <= 1:
            colors.append("blue")
            inside += 1
        else:
            colors.append("red")

    fig, ax = plt.subplots()
    ax.scatter(xs, ys, c=colors, s=1)
    circle = plt.Circle((0, 0), 1, fill=False, color="black")
    ax.add_artist(circle)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(f"Monte Carlo π (≈ {4*inside/iterations:.4f})")
    return fig
