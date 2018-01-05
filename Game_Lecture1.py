import pygame
import gamebox
import random

# Reading the high score
infile = open("info.txt", "r")
highest_score = int(infile.readline().strip())
infile.close()

agreed = False
camera = gamebox.Camera(800, 600)
score = 0
ticks_per_second = 30


# game timer
time = 400
auto_box = gamebox.from_color(780, 590, "white", 200, 20)
auto_box.speedx = 10
controlled_box = gamebox.from_color(250, 250, "Blue", 50, 20)

coins = [gamebox.from_color(random.randint(10, 750), 0, "yellow", 12, 12),
         gamebox.from_color(random.randint(10, 750), 0, "yellow", 12, 12)]

fire = []

def tick(keys):
    global time, score, minutes

    # clear display
    camera.clear("black")

    # AUTOMATED BOX
    if auto_box.speedx > 0 and auto_box.x > 800:
        auto_box.speedx = -10
    elif auto_box.speedx < 0 and auto_box.x < 0:
        auto_box.speedx = 10
    auto_box.move_speed()
    camera.draw(auto_box)

    # Controlled Box
    if pygame.K_RIGHT in keys:
        controlled_box.x += 5
    if pygame.K_LEFT in keys:
        controlled_box.x -= 5
    if pygame.K_UP in keys:
        controlled_box.y -= 5
    if pygame.K_DOWN in keys:
        controlled_box.y += 5
    if pygame.K_SPACE in keys:
        new_shot = gamebox.from_color(controlled_box.x, controlled_box.y, 'white', 5, 5)
        # if len(fire) < 3:
        fire.append(new_shot)
    camera.draw(controlled_box)

    # increase timer
    time -= 1
    if time <= 0:
        game_over = gamebox.from_text(350, 350, "GAME OVER", "Arial", 40, "Red")
        camera.draw(game_over)
        write_score(score, highest_score)
        gamebox.pause()

    if score < 0:
        you_lose = gamebox.from_text(350, 350, "You Lose", "Arial", 40, "Red")
        camera.draw(you_lose)
        write_score(score, highest_score)
        gamebox.pause()

    # calculate minutes,seconds,fractions of seconds
    frac = str(int((time%ticks_per_second)/ticks_per_second*10))
    seconds = str(int((time/ticks_per_second)%60)).zfill(2)
    minutes = str(int((time/ticks_per_second)/60))

    # write timer to screen
    timer = gamebox.from_text(700, 50, minutes+":"+seconds+"."+frac,"Arial",40,"red")  # TEXT OBJECT
    camera.draw(timer)

    # Write Score to screen
    scr = gamebox.from_text(150, 50, "Score: " + str(score), "Arial", 60, "blue")
    camera.draw(scr)

    # Fired shots
    for shot in fire:
        shot.y -= 10
        camera.draw(shot)

    # Define the coins
    for coin in coins:
        for shot in fire:
            if shot.touches(coin):
                score += 1
                fire.remove(shot)
                if coin in coins:
                    coins.remove(coin)
        coin.speedy += 0.03
        if auto_box.touches(coin):
            score += 10
            coins.remove(coin)
        if controlled_box.touches(coin):
            score += 1
            coins.remove(coin)
        if coin.y >= 610:
            score -= 1
            coins.remove(coin)
        coin.move_speed()
        camera.draw(coin)
    if len(coins) < 4:
        new_coin = gamebox.from_color(random.randint(10, 750), 0, "yellow", 12, 12)
        coins.append(new_coin)
    camera.display()

def write_score(current, highest):
    outfile = open("info.txt", "w")
    if current > highest:
        outfile.write(str(current))
    else:
        outfile.write(str(highest_score))

def intro(keys):
    global time, score, minutes, agreed
    if agreed == True:
        # keep this line the last one in your program
        gamebox.timer_loop(ticks_per_second, tick)
    else:
        camera.clear("black")
        message = gamebox.from_text (250, 250, "PRESS SPACE TO START", "arial", 34, "red")
        camera.draw(message)
        if pygame.K_s in keys:
            agreed = True
        camera.display()

gamebox.timer_loop(ticks_per_second, intro)
