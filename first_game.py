# Carrington Murphy - cwm4ec
import pygame
import gamebox
import random

WIDTH_WINDOW = 800
HEIGHT_WINDOW = 600
# Set the camera
camera = gamebox.Camera(WIDTH_WINDOW,HEIGHT_WINDOW)
# Create the character
character = gamebox.from_color(WIDTH_WINDOW/2, HEIGHT_WINDOW - 60, "orange", 30, 50)
# character.size = 40, 60
# Give the character a y speed
character.yspeed = 0
# Define the bounds action
BOUNDS_ACTION = "wrap"

# Define the ground
ground = gamebox.from_color((WIDTH_WINDOW/2), 600, "black", WIDTH_WINDOW, 50)
# Create other walls
walls = []
walls.append(ground)
# Create Coins
coins = []
for i in range(0,20):
    x_value = 40*random.randint(1, 20)
    y_value = 100*random.randint(1,5)
    walls.append(gamebox.from_color(x_value, y_value, "black", 50, 10))
    coin = gamebox.from_color(x_value, y_value - 20, "yellow", 15, 15)
    coins.append(coin)
# Define the time and score
seconds = 30
_tick = 0
ticks_per_second = 30
score = 0
agreed = False

def tick(keys):
    # Define global variables
    global score, _tick, seconds
    # Background
    camera.clear("cyan")
    # Bounds Action
    if BOUNDS_ACTION == "wrap":
        # Determine bounds contact and if so, wrap
        if character.x >= WIDTH_WINDOW:
            character.x = 0                     # wrap
        elif character.x <= 0:
            character.x = WIDTH_WINDOW
        # Vertical Part
        # elif character.y <= 0:
        #     character.y = HEIGHT_WINDOW
        # elif character.y >= HEIGHT_WINDOW:
        #     character.y = 0

    # Do left and right movement
    if pygame.K_LEFT in keys:
        character.x -= 10
    if pygame.K_RIGHT in keys:
        character.x += 10
    character.move_speed()

    # Draw the walls
    for item in walls:
        camera.draw(item)
        if character.bottom_touches(item):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -15
        # Glitching Fix
        if character.touches(item):
            character.move_to_stop_overlapping(item)

    # Add in gravity
    character.yspeed += 1

    # Collect the coins
    for coin in coins:
        if character.touches(coin):
            score += 1
            coins.remove(coin)
        if len(coins) > 0:
            camera.draw(coin)
    # Check for win
    if score == 20:
        gamebox.pause()
        you_win = gamebox.from_text(camera.x, camera.y, "YOU WIN", "Arial", 80, "green")
        camera.draw(you_win)
    # Check for lose
    if seconds <= 0:
        game_over = gamebox.from_text(camera.x, camera.y - 20, "GAME OVER", "Arial", 80, "Red")
        camera.draw(game_over)
        gamebox.pause()
    # Activate Score
    camera.draw(gamebox.from_text(100, 50, "Score: " + str(score) + "/20", "Arial", 40, "blue"))
    # then you call camera.draw(box) for each GameBox you made
    camera.draw(character)

    # Timer
    _tick += 1
    if _tick == 30:
        _tick = 0
        seconds -= 1
    timer = gamebox.from_text(camera.x, 30, str(seconds), "Arial", 50, "red")
    camera.draw(timer)
    # usually camera.display() should be the last line of the tick method
    camera.display()


def restart(keys):
    if pygame.K_r in keys:
        restart = True

def intro(keys):
    global score, agreed
    if agreed == True:
        gamebox.timer_loop(ticks_per_second, tick)
    else:
        camera.clear("yellow")
        start_statement = gamebox.from_text(camera.x, camera.y + 50, "PRESS THE 'S' KEY TO START", "arial", 25, "black")
        instructions1 = gamebox.from_text(camera.x, camera.y - 30, "Try to collect all 20 coins in 30 seconds!", "arial", 34,
                                          "black")
        instructions2 = gamebox.from_text(camera.x, camera.y, "Use the arrow keys to move around and space to jump",
                                          "arial", 34, "black")
        camera.draw(start_statement)
        camera.draw(instructions1)
        camera.draw(instructions2)
        if pygame.K_s in keys:
            agreed = True
        camera.display()

gamebox.timer_loop(ticks_per_second, intro)