# run.py
import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame and set up display
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent-Environment Simulation")

# Colors and font
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
font = pygame.font.Font(None, 40)

# Environment and Agent setup
env = Environment(WIDTH, HEIGHT)
agent = Agent(x=WIDTH // 2, y=HEIGHT // 2, speed=5, environment=env)
RECT_WIDTH, RECT_HEIGHT = 25, 25  # Rectangle size for agent

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detect keyboard input
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    elif keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    elif keys[pygame.K_DOWN]:
        dy = 1

    # Move the agent
    agent.move(dx, dy)

    # Fill the screen and draw the agent as a rectangle
    screen.fill(WHITE)
    agent_pos = agent.get_position()
    agent_rect = pygame.Rect(agent_pos[0], agent_pos[1], RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(screen, BLUE, agent_rect)

   # Display the agent's position
    position_text = font.render(f"Position: {agent_pos}", True, (0, 0, 0))
    screen.blit(position_text, (10, 10))

    # Update the display and set frame rate
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
