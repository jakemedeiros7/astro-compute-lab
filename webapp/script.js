document.addEventListener("DOMContentLoaded", () => {
  // Orbital Mechanics
  document.getElementById("orbital-form").addEventListener("submit", async e => {
    e.preventDefault();
    let mass = document.getElementById("mass").value;
    let velocity = document.getElementById("velocity").value;
    let res = await fetch("/api/orbit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mass, velocity })
    });
    let data = await res.json();
    document.getElementById("orbital-result").innerHTML =
      `Orbital period: ${data.period.toFixed(2)} s<br>
       <img src="/plot/orbit.png?${Date.now()}" width="400">`;
  });

  // Monte Carlo Pi
  document.getElementById("mc-form").addEventListener("submit", async e => {
    e.preventDefault();
    let iterations = document.getElementById("iterations").value;
    let res = await fetch("/api/pi", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ iterations })
    });
    let data = await res.json();
    document.getElementById("mc-result").innerHTML =
      `π ≈ ${data.pi_estimate.toFixed(6)}<br>
       <img src="/plot/pi.png?${Date.now()}" width="400">`;
  });

  // Chaos Pendulum
  document.getElementById("chaos-run").addEventListener("click", async () => {
    let res = await fetch("/api/chaos", { method: "POST" });
    let data = await res.json();
    document.getElementById("chaos-result").innerHTML =
      `Trajectory sample: ${JSON.stringify(data.trajectory.slice(0, 5))}...<br>
       <img src="/plot/chaos.png?${Date.now()}" width="400">`;
  });
});
