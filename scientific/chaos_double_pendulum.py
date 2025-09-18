import numpy as np
import matplotlib.pyplot as plt

def simulate_pendulum(steps=1000, dt=0.01):
    g = 9.81
    L1, L2 = 1.0, 1.0
    m1, m2 = 1.0, 1.0

    theta1, theta2 = np.pi/2, np.pi/4
    w1, w2 = 0.0, 0.0

    trajectory = []

    for _ in range(steps):
        delta = theta2 - theta1

        den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
        den2 = (L2/L1) * den1

        a1 = (m2*L1*w1**2*np.sin(delta)*np.cos(delta) +
              m2*g*np.sin(theta2)*np.cos(delta) +
              m2*L2*w2**2*np.sin(delta) -
              (m1+m2)*g*np.sin(theta1)) / den1

        a2 = (-m2*L2*w2**2*np.sin(delta)*np.cos(delta) +
              (m1+m2)*g*np.sin(theta1)*np.cos(delta) -
              (m1+m2)*L1*w1**2*np.sin(delta) -
              (m1+m2)*g*np.sin(theta2)) / den2

        w1 += a1*dt
        w2 += a2*dt
        theta1 += w1*dt
        theta2 += w2*dt

        trajectory.append((float(theta1), float(theta2)))

    return trajectory

def plot_pendulum(steps=1000, dt=0.01):
    traj = simulate_pendulum(steps, dt)
    x1, y1, x2, y2 = [], [], [], []

    L1, L2 = 1.0, 1.0
    for t1, t2 in traj:
        x1.append(L1*np.sin(t1))
        y1.append(-L1*np.cos(t1))
        x2.append(x1[-1] + L2*np.sin(t2))
        y2.append(y1[-1] - L2*np.cos(t2))

    fig, ax = plt.subplots()
    ax.plot(x2, y2, "r-", linewidth=0.5)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Double Pendulum Trajectory")
    return fig
