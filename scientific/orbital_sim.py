import math
import matplotlib.pyplot as plt
import numpy as np

def simulate_orbit(mass, velocity, radius=6.78e6):
    G = 6.674e-11
    mu = G * mass
    period = 2 * math.pi * radius / velocity
    return {"period": period, "velocity": velocity, "radius": radius}

def plot_orbit(mass=5.97e24, velocity=7800, radius=6.78e6):
    theta = np.linspace(0, 2*np.pi, 500)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig, ax = plt.subplots()
    ax.plot(x, y, "b-")
    ax.plot(0, 0, "yo", markersize=12)  # central body
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Circular Orbit Simulation")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    return fig
