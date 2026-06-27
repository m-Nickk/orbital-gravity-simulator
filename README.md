# 2D Orbital Gravity Simulator (Solar System Update)

A 2D physical engine written in Python using the `pygame` library. It simulates the gravitational interaction between space bodies using Newton's law of universal gravitation and custom numerical integration, now scaled up to model a complete planetary system.

## New Features in this Version

* **Full Solar System Scale**: Simulates the Sun and all 8 planets of the Solar System simultaneously with customized masses, starting positions, and balanced circular velocities.
* **Physics Substepping (Time Acceleration)**: Executes 10 physics calculation cycles per single visual frame. This engineering technique speeds up the simulation dramatically without losing numerical integration accuracy or causing orbital decay.
* **Dynamic Dynamic UI (Labels)**: Integrates hardware-efficient text rendering (`pygame.font`) to display dynamic text names next to each planet that move synchronously with their coordinates.
* **OOP Architecture**: Space bodies are modeled as scalable independent objects using a custom `SpaceBody` class, automated via a single unified list.
* **Graphic Optimization**: Uses a separate hardware-optimized surface (`trail_surface`) to draw infinite orbital paths without losing CPU/GPU performance.

## Variables & Constants Used

* **Sun**: Central body with a super-high mass parameter (`mass=50000`) serving as the gravitational anchor.
* **8 Planets**: Independent orbital bodies with fine-tuned initial tangential velocities (`vx` ranging from `10.3` to `28.8`) to ensure perfectly stable circular orbits.
* **dt**: Base time step constant (`0.02`) wrapped inside a 10x substepping loop for safe and fast execution.
* **dx, dy, distance**: Variables for spatial vector calculation based on the Pythagorean theorem to track relative distances to the Sun.

## How to Run

1. Install dependencies:
   ```bash
   pip install pygame
   ```

2. Run the simulation:
   ```bash
   python Solar_System.py
   ```
