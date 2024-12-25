"Screensaver for Windows written entirely in Python"
import pygame
import random
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up the display
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

# Define colors
BLUE = (0, 51, 153)
WHITE = (255, 255, 255)

# Set up font for displaying time (increased size)
font = pygame.font.Font(None, 72)  # Default font, size 72

# Bubble class
class Bubble:
    def __init__(self):
        self.radius = random.randint(20, 50)
        self.x = random.randint(self.radius, width - self.radius)
        self.y = height + self.radius
        self.speed = random.uniform(1, 3)
        # Generate a random color for the bubble
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        self.y -= self.speed
        if self.y < -self.radius:
            self.y = height + self.radius
            self.x = random.randint(self.radius, width - self.radius)
            # Generate a new random color when the bubble resets
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Create bubbles
bubbles = [Bubble() for _ in range(50)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            running = False

    # Fill the screen with BLUE
    screen.fill(BLUE)

    # Update and draw bubbles
    for bubble in bubbles:
        bubble.move()
        bubble.draw(screen)

    # Get the current date and time in the desired format
    current_time = datetime.now().strftime("%H:%M:%S - %d.%m.%Y")
    time_surface = font.render(current_time, True, WHITE)
    
    # Draw the time on the screen
    screen.blit(time_surface, (40, height - 80))  # Positioning in the lower left corner

    # Update the display
    pygame.display.flip()
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()