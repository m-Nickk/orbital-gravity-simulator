import math
from random import choice
from turtle import distance
import pygame
from pygame import Clock, color

# Initialize all Pygame modules
pygame.init()

# Template class for creating celestial bodies
class SpaceBody:
    def __init__(self, name, x, y, vx, vy, radius, color, mass=0):
        self.name = name       
        self.x = x
        self.y = y             
        self.vx = vx           
        self.vy = vy           
        self.radius = radius   
        self.color = color     
        self.mass = mass       

    # Method to draw the planet and its text label
    def draw(self, surface):
        # Draw the planet circle on the main screen
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        # Render the planet name into a graphic image (white color)
        text_image = font.render(self.name, True, (255, 255, 255))
        # Overlay the text image onto the screen slightly to the right and above the planet
        surface.blit(text_image, (int(self.x) + self.radius + 5, int(self.y) - 10))

    # Method to move the planet and draw its infinite orbital path
    def move(self, dt, surface):
        # Update coordinates based on current velocity and time step
        self.x += self.vx * dt
        self.y += self.vy * dt

        # If it's a planet (not the Sun), draw a dot on the persistent trail surface
        if self.mass == 0 or self.radius < 20:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 1)

    # Method to calculate gravitational pull towards the Sun
    def attract_to_sun(self, sun, dt):
        if self == sun:
            return  # The Sun does not attract itself

        # Find the distance between the planet and the Sun along the X and Y axes
        dx = sun.x - self.x
        dy = sun.y - self.y
        # Calculate the hypotenuse (straight-line distance)
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance < 5:
            return  # Avoid division by zero during potential collisions

        # Newton's law of universal gravitation (calculate attraction force)
        f_total = sun.mass / (distance**2)
        
        # Split the force into X and Y components and update planet velocities
        self.vx += f_total * (dx / distance) * dt
        self.vy += f_total * (dy / distance) * dt

# Create Solar System objects with balanced circular orbits
Sun = SpaceBody("Sun", x=600, y=600, vx=0, vy=0, radius=25, color=(255, 200, 0), mass=50000)
Mercury = SpaceBody("Mercury", x=600, y=540, vx=28.8, vy=0, radius=4, color=(200, 200, 200), mass=1)
Venus = SpaceBody("Venus", x=600, y=500, vx=22.3, vy=0, radius=6, color=(220, 180, 130), mass=5)
Earth = SpaceBody("Earth", x=600, y=440, vx=17.7, vy=0, radius=7, color=(0, 130, 255), mass=6)
Mars = SpaceBody("Mars", x=600, y=380, vx=15.0, vy=0, radius=5, color=(200, 70, 40), mass=4)
Jupiter = SpaceBody("Jupiter", x=600, y=300, vx=12.9, vy=0, radius=14, color=(210, 160, 130), mass=30)
Saturn = SpaceBody("Saturn", x=600, y=230, vx=11.6, vy=0, radius=11, color=(230, 210, 170), mass=20)
Uranus = SpaceBody("Uranus", x=600, y=180, vx=10.9, vy=0, radius=9, color=(160, 220, 240), mass=10)
Neptune = SpaceBody("Neptune", x=600, y=130, vx=10.3, vy=0, radius=9, color=(60, 100, 245), mass=10)

# Dynamic list to automate operations on all bodies simultaneously
planets = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]

# Main game window resolution setup
screen = pygame.display.set_mode((1200, 1200))

# Create a separate hardware-optimized surface for persistent orbit rendering
trail_surface = pygame.Surface((1200, 1200))

# Make the black background on this surface transparent
trail_surface.set_colorkey((0, 0, 0))

# Create game clock to manage frame rate
clock = pygame.time.Clock()

# Initialize system font for planet names (Arial, size 16, bold)
font = pygame.font.SysFont("Arial", 16, bold=True)

# Base physical time step (delta time) for simulation accuracy
dt = 0.02

# Main loop execution flag
running = True

# Start of the main game loop
while running:
    clock.tick(60)  # Cap the loop execution to 60 frames per second
    
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop when the close button is clicked

    # Substepping block: calculate physics 10 times per frame to speed up time
    for _ in range(10):
        for body in planets:
            body.attract_to_sun(Sun, dt)
        for body in planets:
            body.move(dt, trail_surface)

    # Clear the main screen by filling it with solid black color
    screen.fill((0, 0, 0))
    # Blit the persistent orbit trail surface onto the main window
    screen.blit(trail_surface, (0, 0))

    # Invoke the draw method for each celestial body in our list
    for body in planets:
        body.draw(screen)

    # Flip the display buffer to update the window graphics
    pygame.display.flip()
