import pygame as pg
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scores import ScoreBoard
from settings import *


pg.init()


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Breakout Game")

clock = pg.time.Clock()


# OBJECTS FROM OTHER FILES 
pad = Paddle(paddle_x, paddle_y)
bricks = Bricks(screen, brick_width, brick_height)
ball = Ball(ball_x, ball_y, screen)
score = ScoreBoard(text_x, color, screen)
score.set_high_score()

# Running loop 
running = True
while running:
    for event in pg.event.get():   # Check for quit game
        if event.type == pg.QUIT:
            running = False
    fill_gradient(screen, BG_purple, BG_darkpurple) #Cool gradient BG 
    score.show_scores() #Big numbers 
    pad.appear(screen) #The paddle
    bricks.show_bricks() #The bricks
    

   
   
    # Check if ball hits the x-axis and y-axis 
    ball.check_for_contact_on_x()
    ball.check_for_contact_on_y()


    

    # Check if ball falls off
   
    if score.lives <= 0: #Makes sure it works with the debug mode, also a cheat failsafe? 
        score.game_over()
        game_over = False 

    # Check if ball hits paddle
        # Check if ball hits paddle
    if pad.rect.collidepoint(ball.x, ball.y + ball.radius):
        ball.bounce_y()

    # Check if ball hits brick(collision function)
    for brick in bricks.bricks[:]:  # Iterate over a copy to safely remove bricks
        if brick.collidepoint(ball.x, ball.y - ball.radius) or brick.collidepoint(ball.x, ball.y + ball.radius):
            bricks.bricks.remove(brick)
            ball.bounce_y()
            score.score += 1

    
    if len(bricks.bricks) == 0:# Checks if bricks are all gone
        bricks.set_values()

    # Check for key presses
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        pad.move_right()

    if keys[pg.K_LEFT]:
        pad.move_left()

    #DEBUG MODE PRESS LEFT SHIFT AND ITS BUTTON TO ACTIVATE 
    if keys[pg.K_LSHIFT] and keys[pg.K_9]:  # Debug mode, kill all bricks and win(9)
        bricks.bricks.clear()
        score.success() #Slightly buggy, but it is a debug menu so who cares

    if keys[pg.K_LSHIFT] and keys[pg.K_8]: #Debug mode, revive all bricks(8)
        bricks.bricks.clear()
        bricks.set_values()

    if keys[pg.K_LSHIFT] and keys[pg.K_7]: #Brings up losing menu(7)
        score.game_over()

#Increase/decreases lives 
    if keys[pg.K_LSHIFT] and keys[pg.K_MINUS]: #Lose a life(-)
        if score.lives > 0: 
            score.lives -= 1  #works without killing the game 
    

    if keys[pg.K_LSHIFT] and keys[pg.K_EQUALS]: #Gain a life(+)
        score.lives += 1

    # Restart game
    if keys[pg.K_0]:
        if score.is_game_over(): 
            score.score = 0
            score.lives = 5
            bricks.bricks.clear()
            bricks.set_values()

    pg.display.flip()
    clock.tick(60) #FPS

