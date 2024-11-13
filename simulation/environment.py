# environment.py

class Environment:
    def __init__(self, width, height):
        """
        Initialize the environment with width and height.
        :param width: Width of the environment.
        :param height: Height of the environment.
        """
        self.width = width
        self.height = height

    def limit_position(self, x, y):
        """
        Ensure the agent remains within the environment's boundaries.
        :param x: x-coordinate to be limited.
        :param y: y-coordinate to be limited.
        :return: Tuple of x and y coordinates within boundaries.
        """
        x = max(0, min(x, self.width - 25))  # Adjust for agent size
        y = max(0, min(y, self.height - 25))  # Adjust for agent size
        return x, y
