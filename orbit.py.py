import math
from random import choice
import pygame
from pygame import color
pygame.init()

class SpaceBody:
    def __init__(self, x, y, vx, vy, radius, color, mass=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.mass = mass
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

earth = SpaceBody(x=400, y=400, vx=0, vy=0, radius=30, color=(0, 100, 255), mass=4000)
moon = SpaceBody(x=600, y=400, vx=0, vy=-4.5, radius=18, color=(150, 150, 150))
satellite = SpaceBody(x=700, y=400, vx=0, vy=3.7, radius=10, color=(200, 100, 0))


# Moon history
moon_history = []

# Screen recolution
screen = pygame.display.set_mode((800, 800))

trail_surface = pygame.Surface((800, 800))
trail_surface.set_colorkey((0, 0, 0))

# Time
dt = 0.03

# Start program
running = True

# Beginning of the cycle
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Distance between the Earth and the Moon along the X and Y axes
    dx = earth.x - moon.x
    dy = earth.y - moon.y
    dx2 = earth.x - satellite.x
    dy2 = earth.y - satellite.y


    # Hypotenuse
    distance = math.sqrt(dx**2 + dy**2)
    distance2 = math.sqrt(dx2**2 + dy2**2)


    # Force of attraction
    f_total = earth.mass / (distance**2)
    f_total2 = earth.mass / (distance2**2)

    # Division of force on X and Y axes
    fx = f_total * (dx / distance)
    fy = f_total * (dy / distance)
    fx2 = f_total2 * (dx2 / distance2)
    fy2 = f_total2 * (dy2 / distance2)

    # Acceleration
    moon.vx += fx * dt
    moon.vy += fy * dt
    satellite.vx += fx2 * dt
    satellite.vy += fy2 * dt

    # Trajectory
    speed_moon_x = moon.x + (moon.vx * dt)
    moon.x = speed_moon_x
    speed_moon_y = moon.y + (moon.vy * dt)
    moon.y = speed_moon_y
    speed_sat_x = satellite.x + (satellite.vx * dt)
    satellite.x = speed_sat_x
    speed_sat_y = satellite.y + (satellite.vy * dt)
    satellite.y = speed_sat_y


    # Tail
    current_x = int(moon.x)
    current_y = int(moon.y)
    pygame.draw.circle(trail_surface, (80, 80, 80), (int(moon.x), int(moon.y)), 2)
    current_x = int(satellite.x)
    current_y = int(satellite.y)
    pygame.draw.circle(trail_surface, (100, 50, 0), (int(satellite.x), int(satellite.y)), 2)


    # General screen color
    screen.fill((0, 0, 0))
    screen.blit(trail_surface, (0, 0))

    # What do we see
    earth.draw(screen)
    moon.draw(screen)
    satellite.draw(screen)


    pygame.display.flip()