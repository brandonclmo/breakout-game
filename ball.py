import pygame as pg
from settings import ball_x_speed, ball_y_speed, ball_radius

Ballspeed = -1.1 #Change Ball speed here(has to be a negative value, because it will move left for x and up for y)
#I want to set a cap on the exponential growth of the speed, maybe make it linear 
class Ball:

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.radius = ball_radius
        self.color = pg.Color("red")
        self.x_speed = ball_x_speed
        self.y_speed = ball_y_speed
    def move(self):
        # Draw outline first (black, slightly larger radius)
        pg.draw.circle(self.screen, (0, 0, 255), [self.x, self.y], self.radius + 10)
        # Draw the filled ball
        pg.draw.circle(self.screen, self.color, [self.x, self.y], self.radius)
        self.y -= self.y_speed
        self.x -= self.x_speed
        pg.draw.circle
        # print (self.x, self.y) 
        print(f"Ball speed: x_speed={self.x_speed}, y_speed={self.y_speed}") 
    def bounce_x(self):
        self.x_speed *= Ballspeed

    def bounce_y(self):
        self.y_speed *= Ballspeed

    def check_for_contact_on_x(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen.get_width():
            self.bounce_x()

    def check_for_contact_on_y(self):
        if self.y + self.radius <= 0:
            self.bounce_y()