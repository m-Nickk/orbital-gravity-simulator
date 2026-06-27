# 2D Orbital Gravity Simulator

A 2D physical engine written in Python using the `pygame-ce` library. It simulates the gravitational interaction between space bodies using Newton's law of universal gravitation and custom numerical integration.

##  Features
* **OOP Architecture**: Space bodies are modeled as scalable independent objects using a custom `SpaceBody` class.
* **Physics Engine**: Calculates multi-body gravitational forces ($F = G \frac{m_1 m_2}{r^2}$) dynamically at each time step.
* **Graphic Optimization**: Uses a separate hardware-optimized surface (`trail_surface`) to draw infinite orbital paths without losing CPU/GPU performance.
* **Counter-rotating Orbits**: Simulates multiple satellites orbiting a central mass in different directions simultaneously.

## Variables & Constants used
* `earth`: Central body with high mass parameter (`mass=4000`)
* `moon` & `satellite`: Space bodies with initial velocities (`vy=-4.5` and `vy=3.7`)
* `dt`: Time step constant (`0.03`) for smooth numerical integration
* `dx`, `dy`, `distance`: Variables for spatial coordinates calculation based on the Pythagorean theorem

## How to Run
1. Install dependencies:
   ```bash
   pip install pygame-ce
   ```
2. Run the simulation:
   ```bash
   python orbit.py
   ```
