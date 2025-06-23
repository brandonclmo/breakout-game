import random
import pygame as pg
import settings 

class Bricks:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.random_colors = settings.RED, settings.GREEN 
        self.bricks = []
        self.brick_colors = []
        self.set_values()

    def set_values(self):
        y_values = [int(y) for y in range(100, 200, self.height + 5)]  # 5 is vertical gap, set to 0 for no gap
        x_values = [int(x) for x in range(10, 550, self.width)]  # Use self.width for no horizontal gap
        y_index = 0
        self.loop(x_values, y_values, y_index)

    def loop(self, x_values, y_values, y_index):

        for n in x_values:
            # Check if it is the last position in the x_values list.
            if n == x_values[-1]:

                # Check if all the positions in the y_values has been occupied
                if y_index < len(y_values) - 1:
                    y_index += 1

                    # Run the method again if there are still vacant positions.
                    self.loop(x_values, y_values, y_index)

            # Create new bricks
            else:
                x = n
                y = y_values[y_index]
                brick = pg.Rect(x, y, self.width, self.height)
                self.bricks.append(brick)
                self.brick_colors.append(random.choice(self.random_colors))

    def show_bricks(self):
        for loop in range(len(self.bricks)):
            brick = self.bricks[loop]
            color = self.brick_colors[loop]
            pg.draw.rect(self.screen, color, brick)  # Filled brick
            pg.draw.rect(self.screen, (0, 0, 255), brick, 2)  # yellow outline, width=2

    def exploding_bricks(self, index):
        adjacent = []
        bricks_per_row = len([x for x in range(10, 550, 42)])  # Same as in set_values
        row = index // bricks_per_row

        # Left neighbor (must be in the same row and touching)
        if index > 0 and (index - 1) // bricks_per_row == row:
            left_brick = self.bricks[index - 1]
            this_brick = self.bricks[index]
            if left_brick.right == this_brick.left:
                adjacent.append(index - 1)
        # Right neighbor (must be in the same row and touching)
        if index < len(self.bricks) - 1 and (index + 1) // bricks_per_row == row:
            right_brick = self.bricks[index + 1]
            this_brick = self.bricks[index]
            if right_brick.left == this_brick.right:
                adjacent.append(index + 1)
        return adjacent