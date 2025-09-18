from flask import Flask, request, jsonify, render_template, send_file
import io
import matplotlib.pyplot as plt

from scientific.orbital_sim import simulate_orbit, plot_orbit
from scientific.monte_carlo_pi import estimate_pi, plot_monte_carlo
from scientific.chaos_double_pendulum import simulate_pendulum, plot_pendulum

app = Flask(__name__, static_folder=".", template_folder=".")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/orbit", methods=["POST"])
def orbit():
    data = request.json
    mass = float(data.get("mass", 5.97e24))
    velocity = float(data.get("velocity", 7800))
    result = simulate_orbit(mass, velocity)
    return jsonify(result)

@app.route("/plot/orbit.png")
def orbit_plot():
    buf = io.BytesIO()
    fig = plot_orbit()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/api/pi", methods=["POST"])
def pi():
    data = request.json
    iterations = int(data.get("iterations", 10000))
    result = estimate_pi(iterations)
    return jsonify({"pi_estimate": result})

@app.route("/plot/pi.png")
def pi_plot():
    buf = io.BytesIO()
    fig = plot_monte_carlo()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/api/chaos", methods=["POST"])
def chaos():
    trajectory = simulate_pendulum()
    return jsonify({"trajectory": trajectory[:100]})

@app.route("/plot/chaos.png")
def chaos_plot():
    buf = io.BytesIO()
    fig = plot_pendulum()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
