# agent.py
import pygame

class Agent:
    def __init__(self, x, y, speed, environment):
        """
        Initialize the agent with position, speed, and a reference to the environment.
        :param x: Initial x-coordinate of the agent.
        :param y: Initial y-coordinate of the agent.
        :param speed: Initial speed of the agent.
        :param environment: The environment within which the agent moves.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.environment = environment  # Link to the environment

    def move(self, dx, dy):
        """
        Move the agent within the environment boundaries.
        :param dx: Change in x direction (-1 for left, 1 for right).
        :param dy: Change in y direction (-1 for up, 1 for down).
        """
        # Update position based on direction and speed
        self.x += dx * self.speed
        self.y += dy * self.speed
        
        # Wrap around screen edges
        if self.x < 0:
            self.x = self.environment.width
        elif self.x > self.environment.width:
            self.x = 0

        if self.y < 0:
            self.y = self.environment.height
        elif self.y > self.environment.height:
            self.y = 0

        # Increase speed each time the agent moves
        if dx != 0 or dy != 0:
            self.speed += 0.1  # Increment speed
    

    def get_position(self):
        """
        Get the current position of the agent.
        :return: Tuple of x and y coordinates.
        """
        return int(self.x), int(self.y)
