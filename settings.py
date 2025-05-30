import pygame as pg


WHITE: tuple = (255, 255, 255)
LIGHTBLUE: tuple = (24, 155, 204)
YELLOW: tuple = (255, 255, 0)
GREEN: tuple = (177, 210, 68)

#Block colours
LIGHTRED: tuple = (193, 66, 63)
RED: tuple = (38, 0, 1)
BLACK: tuple = (0, 0, 0)
PURPLE: tuple = (138, 0, 196)
GREEN: tuple = (177, 210, 68)


#BG colours
BG_purple: tuple = (126, 46, 83)
BG_darkpurple: tuple = (48, 15, 15)

#Background gradient 
def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
  
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pg.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color), (col,y1), (col,y2)

# The BG function has been moved to main.py 

# Screen dimensions
WIDTH = 550
HEIGHT = 600


# Text color
color = WHITE


# Paddle settings
paddle_x = 200
paddle_y = 550
paddle_width = 100
paddle_height = 20


# Ball settings
ball_x = 250
ball_y = 540
ball_x_speed = 2
ball_y_speed = 2
ball_radius = 5


# Text settings
text_x = 300


# Bricks settings
brick_width = 40
brick_height = 20