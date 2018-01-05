# Carrington Murphy (cwm4ec) Craig Doody (cnd5zw)
import pygame


import gamebox


WIDTH_WINDOW = 1000
HEIGHT_WINDOW = 600
time = 1000








# Set the camera
camera = gamebox.Camera(WIDTH_WINDOW, HEIGHT_WINDOW)








# Create the mario character
mario = gamebox.from_image(100, HEIGHT_WINDOW - 80, 'https://t3.rbxcdn.com/fcedf49f6eaf2176e2f788e568304f57')
mario.size = 30, 42  # Height then width
mario.flip()
mario_size = "small"








mario_speed = 9
powered_up = False

background = 'web'
# Create the Background (3392, 460)
if background == 'web':
 image = gamebox.from_image(3500, HEIGHT_WINDOW,
                            'https://www.spriters-resource.com/resources/sheets/19/20592.png')
 image.size = 7000, 1200  # This is the size of the level
else:
 image = gamebox.from_color(3500, HEIGHT_WINDOW, "cyan", 7000, 1200)


# Create a set of all platforms
platforms = []

# Create the ground
ground = []
ground_locations = [20, 60, 100, 140, 180, 220, 260, 300, 340, 380, 420, 460, 500, 540, 580, 620, 660, 700, 740, 780, 820, 860, 900, 940, 980, 1020, 1060, 1100, 1140, 1180, 1220, 1260, 1300, 1340, 1380, 1420, 1460, 1500, 1540, 1580, 1620, 1660, 1700, 1740, 1780, 1820, 1860, 1900, 1940, 1980, 2020, 2060, 2100, 2140, 2180, 2220, 2260,
                  2390, 2430, 2470, 2510, 2550, 2590, 2630, 2670, 2710, 2750, 2790, 2830,
                  2945, 2985, 3025, 3065, 3105, 3145, 3185, 3225, 3265, 3305, 3345, 3385, 3425, 3465, 3505, 3545, 3585, 3625, 3665, 3705, 3745, 3785, 3825, 3865, 3905, 3945, 3985, 4025, 4065, 4105, 4145, 4185, 4225, 4265, 4305, 4345, 4385, 4425, 4465, 4505, 4545, 4585, 4625, 4665, 4705, 4745, 4785, 4825, 4865, 4905, 4945, 4985, 5025,
                  5147, 5187, 5227, 5267, 5305, 5347, 5387, 5427, 5467, 5507, 5547, 5587, 5627, 5667, 5707, 5747, 5787, 5827, 5867, 5907, 5947, 5987, 6027, 6067, 6107, 6147, 6187, 6227, 6267, 6307, 6347, 6387, 6427, 6467, 6507, 6547, 6587, 6627, 6667, 6707, 6747, 6787, 6827, 6867, 6907, 6947]
ground_height = [540,580]




separation_locations = [40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800, 840, 880, 920, 960, 1000, 1040, 1080, 1120, 1160, 1200, 1240, 1280, 1320, 1360, 1400, 1440, 1480, 1520, 1560, 1600, 1640, 1680, 1720, 1760, 1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080, 2120, 2160, 2200, 2240, 2280,
                      2370, 2410, 2450, 2490, 2530, 2570, 2610, 2650, 2690, 2730, 2770, 2810, 2850,
                      2925, 2965, 3005, 3045, 3085, 3125, 3165, 3205, 3245, 3285, 3325, 3365, 3405, 3445, 3485, 3525, 3565, 3605, 3645, 3685, 3725, 3765, 3805, 3845, 3885, 3925, 3965, 4005, 4045, 4085, 4125, 4165, 4205, 4245, 4285, 4325, 4365, 4405, 4445, 4485, 4525, 4565, 4605, 4645, 4685, 4725, 4765, 4805, 4845, 4885, 4925, 4965, 5005, 5045,
                      5127, 5167, 5207, 5247, 5287, 5327, 5367, 5407, 5447, 5487, 5527, 5567, 5607, 5647, 5687, 5727, 5767, 5807, 5847, 5887, 5927, 5967, 6007, 6047, 6087, 6127, 6167, 6207, 6247, 6287, 6327, 6367, 6407, 6447, 6487, 6527, 6567, 6607, 6647, 6687, 6727, 6767, 6807, 6847, 6887, 6927, 6967]




separation = []




for i in range(len(separation_locations)):
  line = gamebox.from_color(separation_locations[i], 560, 'black', 1, 80)
  separation.append(line)




for i in range(len(ground_locations)):
  line = gamebox.from_color(ground_locations[i], 560, 'black', 40, 1)
  separation.append(line)




for i in range(len(ground_locations)):
  for j in range(0,2):
      box = gamebox.from_image(ground_locations[i], ground_height[j], "http://piq.codeus.net/static/media/userpics/piq_18770_400x400.png")
      box.size = 40, 40
      ground.append(box)
      platforms.append(box)
















# Create clouds
cloud_locations = [677, 932, 962, 992, 1247, 1271, 1895, 2255, 2525, 2570, 2585, 2820, 2850, 3480, 3849, 4104, 4134, 4179, 4419, 4449, 5045, 5420, 5675, 5720, 5750, 6005, 6029, 6644]
cloud_height = 100
clouds = []








for i in range(len(cloud_locations)):
  fluff = gamebox.from_image(cloud_locations[i], cloud_height, "http://csassignment.weebly.com/uploads/2/3/3/8/23383134/cloud.png")
  fluff.size = 100, 100
  clouds.append(fluff)




# Box Locations and Heights
coin_box_locations = [530, 736, 772, 2586, 3120, 3504, 3612, 3720, 5632, 4270, 4306]
coin_heights = ['low', 'high', 'low', 'low', 'high', 'low', 'low', 'low', 'low', 'high', 'high']
mushroom_box_locations = [700, 3612]
mushroom_heights = ['low', 'low']
other_box_locations = [664, 736, 808, 2550, 2622, 2658, 2694, 2730, 2766, 2802, 2838, 2874,
                    3012, 3048, 3084, 3120, 3315, 3900,     4010, 4046, 4082, 4234, 4342,
                    4270, 4306, 5560, 5596, 5668]
other_heights =['low', 'low', 'low', 'low', 'low', 'high', 'high', 'high', 'high', 'high', 'high', 'high',
                   'high', 'high', 'high', 'low', 'low', 'low',   'high', 'high', 'high', 'high', 'high',
                   'low', 'low', 'low', 'low', 'low']
staircase_box_locations = [4437, 4473, 4473, 4509, 4509, 4509, 4545, 4545, 4545, 4545,
                         4653, 4653, 4653, 4653, 4689, 4689, 4689, 4725, 4725, 4761,
                         4883, 4919, 4919, 4955, 4955, 4955, 4991, 4991, 4991, 4991, 5027, 5027, 5027, 5027,
                         5145, 5145, 5145, 5145, 5181, 5181, 5181, 5217, 5217, 5253,
                         5990, 6026, 6026, 6062, 6062, 6062, 6098, 6098, 6098, 6098, 6134, 6134, 6134, 6134, 6134, 6170, 6170, 6170, 6170, 6170, 6170, 6206, 6206, 6206, 6206, 6206, 6206, 6206, 6242, 6242, 6242, 6242, 6242, 6242, 6242, 6242, 6278, 6278, 6278, 6278, 6278, 6278, 6278, 6278]
level = [1, 1, 2, 1, 2, 3, 1, 2, 3, 4,
       1, 2, 3, 4, 1, 2, 3, 1, 2, 1,
       1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4,
       1, 2, 3, 4, 1, 2, 3, 1, 2, 1,
       1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
















box_height1 = 375
box_height2 = 200








# Pipes
short_pipe_locations = [956, 5410, 5940]
medium_pipe_locations = [1292]
tall_pipe_locations = [1556, 1916]








# Create lists of all the boxes
coin_boxes = []
activated_coins = []
mushroom_boxes = []
activated_mushrooms = []
other_boxes = []








# Create checkers for the boxes
coin_activation = []
mushroom_activation = []
















pipes = []




stairs = []




# Create Staircases
for i in range(len(staircase_box_locations)):
 stair_height = 0
 if level[i] == 1:
     stair_height = 600-(18+80)
 elif level[i] == 2:
     stair_height = 600-(54+80)
 elif level[i] == 3:
     stair_height = 600-(90+80)
 elif level[i] == 4:
     stair_height = 600-(126+80)
 elif level[i] == 5:
     stair_height = 600-(162+80)
 elif level[i] == 6:
     stair_height = 600 - (198 + 80)
 elif level[i] == 7:
     stair_height = 600 - (234 + 80)
 elif level[i] == 8:
     stair_height = 600 - (270 + 80)
 box = gamebox.from_image(staircase_box_locations[i], stair_height,
                          "http://www.mariowiki.com/images/thumb/a/aa/Brick_Block_-_New_Super_Mario_Bros.png/120px-Brick_Block_-_New_Super_Mario_Bros.png")
 box.size = 36, 36
 stairs.append(box)
 platforms.append(box)




# Create all the coin boxes
coins_list = []
for i in range(len(coin_box_locations)):
 if coin_heights[i] == 'low':
     box_height = 375
 elif coin_heights[i] == 'high':
     box_height = 200
 box = gamebox.from_image(coin_box_locations[i], box_height, "https://s-media-cache-ak0.pinimg.com/236x/a3/6b/67/a36b67487b3f1475f6a70279aa13ea02.jpg")
 coin_image = gamebox.from_image(coin_box_locations[i], box_height - 36, "https://s-media-cache-ak0.pinimg.com/originals/96/4c/f1/964cf112c8928c7c75312f7f15e6b1e0.png")
 coin_image.size = 36, 36
 coins_list.append(coin_image)
 activated_box = gamebox.from_image(coin_box_locations[i], box_height, 'http://orig12.deviantart.net/53bf/f/2009/269/b/e/mario_box_pixels_by_stoobytoons.png')
 box.size = 36, 36
 activated_box.size = 36, 36
 coin_boxes.append(box)
 activated_coins.append(activated_box)
 coin_activation.append(False)
 platforms.append(box)








# Create all the mushroom boxes
mushroom_list = []
for i in range(len(mushroom_box_locations)):
 if coin_heights[i] == 'low':
     box_height = 375
 elif coin_heights[i] == 'high':
     box_height = 200
 box = gamebox.from_image(mushroom_box_locations[i], box_height,
                          "https://s-media-cache-ak0.pinimg.com/236x/a3/6b/67/a36b67487b3f1475f6a70279aa13ea02.jpg")
 mushroom = gamebox.from_image(mushroom_box_locations[i], box_height - 36, "http://pre00.deviantart.net/aceb/th/pre/i/2012/027/2/5/8_bit_mushroom_by_nathanmarino-d4nt1wp.png")
 mushroom.size = 36, 36
 mushroom_list.append(mushroom)
 activated_box = gamebox.from_image(mushroom_box_locations[i], box_height,
                              'http://orig12.deviantart.net/53bf/f/2009/269/b/e/mario_box_pixels_by_stoobytoons.png')
 box.size = 36, 36
 activated_box.size = 36, 36
 mushroom_boxes.append(box)
 activated_mushrooms.append(activated_box)
 mushroom_activation.append(False)
 platforms.append(box)








# Create all the other boxes
for i in range(len(other_box_locations)):
 if other_heights[i] == 'low':
     box_height = 375
 elif other_heights[i] == 'high':
     box_height = 200
 box = gamebox.from_image(other_box_locations[i], box_height,
                          "http://www.mariowiki.com/images/thumb/a/aa/Brick_Block_-_New_Super_Mario_Bros.png/120px-Brick_Block_-_New_Super_Mario_Bros.png")
 box.size = 36, 36
 platforms.append(box)
 other_boxes.append(box)








# Create the pipes
all_walls = []
for pipe_coord in short_pipe_locations:
 pipe = gamebox.from_image(pipe_coord, 515,
                           "http://images.clipartpanda.com/pipe-clipart-a-green-cartoon-pipe-md.png")
 pipe.size = 72, 170
 other_boxes.append(pipe)
 platforms.append(pipe)
 all_walls.append(pipe)
 pipes.append(pipe)
for pipe_coord in medium_pipe_locations:
 pipe = gamebox.from_image(pipe_coord, 475,
                           "http://images.clipartpanda.com/pipe-clipart-a-green-cartoon-pipe-md.png")
 pipe.size = 72, 170
 other_boxes.append(pipe)
 platforms.append(pipe)
 all_walls.append(pipe)
 pipes.append(pipe)
for pipe_coord in tall_pipe_locations:
 pipe = gamebox.from_image(pipe_coord, 440,
                           "http://images.clipartpanda.com/pipe-clipart-a-green-cartoon-pipe-md.png")
 pipe.size = 72, 170
 other_boxes.append(pipe)
 platforms.append(pipe)
 all_walls.append(pipe)
 pipes.append(pipe)




#Define the flag
flag = gamebox.from_image(6700, 340, "http://img09.deviantart.net/0464/i/2011/324/a/e/secret_flagpole_by_yoshigo99-d4b7f6b.png")
flag.size = 100, 380


invincibility = False


# Create a coin variable =
coins = 0
_tick = 0
seconds = 200


death = False
enemy_speed = 6
count = 0


enemies = []
enemy_locations = [685, 1382, 1762, 1798, 2612, 2666, 3143, 3197, 3503, 4070, 4106, 4205, 4277, 5723, 5795, -40]
enemy_speeds = [enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed, enemy_speed]
for location in enemy_locations:
   enemy = gamebox.from_image(location, 500, "http://media.doink.com/thumbnail/1249185/1292183448027.png")
   enemy.size = 45, 45
   enemies.append(enemy)


   # enemy.yspeed += 1
   # enemy.y = enemy.y + enemy.yspeed
   # if character.bottom_touches(enemy):
   #     enemies.remove(enemy)
   #     enemy = gamebox.from_color(random.randint(50, 750), 50, rand_color2, 30, 30)
   #     enemies.append(enemy)
   #     enemy.yspeed = 0
   # elif character.touches(enemy):
   #     gamebox.pause()
game_on = False
title_screen = gamebox.from_image(camera.x, camera.y, "http://8bitreview.com/wp-content/uploads/2015/02/mario_startscreen.jpg")
title_screen.size = WIDTH_WINDOW, HEIGHT_WINDOW
directions = [gamebox.from_text(camera.x, camera.y + 125, 'Press SPACE to Start', 'Arial', 30, 'white', True), gamebox.from_text(camera.x, camera.y + 150, 'Arrow keys to move   SPACE to jump  "R" to restart', 'Arial', 25, 'white'), gamebox.from_text(camera.x, camera.y + 175, 'Carrington Murphy (cwm4ec) & Craig Doody (cnd5zw)', 'Arial', 25, 'white')]


def tick(keys):
 global mario_speed, coins, coin_activation, powered_up, mario_size, _tick, seconds, goomba_direction, death, coins_list, mushroom_list, flag, enemy_speed, invincibility, count, game_on, title_screen
 if pygame.K_SPACE in keys:
     game_on = True
 if not game_on:
     camera.draw(title_screen)
     camera.draw(gamebox.from_color(camera.x, camera.y + 150, 'black', 500, 90))
     for line in directions:
       camera.draw(line)
     camera.display()
     if pygame.K_SPACE in keys:
         game_on = True
 if game_on:
     # Background
     camera.draw(image)
     camera.draw(gamebox.from_text(WIDTH_WINDOW / 2, HEIGHT_WINDOW / 2, "None of the graphics used are meant to modify or infringe on original Nintendo material", "Arial", 20, 'black'))
     camera.draw(gamebox.from_text(WIDTH_WINDOW / 2, (HEIGHT_WINDOW / 2) + 30,
                                   "Thus the name of our program is officially: Normal Mario Brothers",
                                   "Arial", 20, 'black'))
     # Activate Coins Display
     coin_display = gamebox.from_text(camera.x - 420, 40, "Coins: " + str(coins), "Arial", 36, "yellow")
     camera.draw(coin_display)
     # Scrolling based on movement
     if mario.x == 100 and mario.y < 600:
         camera.x = 500
     elif mario.x > (camera.x) and camera.x < 6500:
         camera.x += mario_speed
     elif mario.x < (camera.x - 400) and camera.x > 500:
         camera.x -= mario_speed
     else:
         camera.x += 0


     # enemies
     if invincibility:
         count += 1
     if count >= 30:
         mario_size = "small"
         mario.size = 30, 42
         count = 0
         invincibility = False




     for i in range(0,len(enemies)-1):
         enemies[i].x -= enemy_speeds[i]
         for pipe in pipes:
             if enemies[i].touches(pipe):
                 enemies[i].move_to_stop_overlapping(pipe)
                 enemy_speeds[i] = -enemy_speeds[i]
         if mario.bottom_touches(enemies[i]):
             enemies.remove(enemies[i])
             enemy_speeds.remove(enemy_speeds[i])
         elif mario.touches(enemies[i]):
             if mario_size == "small":
                 death = True
             else:
                 invincibility = True








     # Set up left and right movement
     if pygame.K_LEFT in keys:
         mario.x -= mario_speed
     if pygame.K_RIGHT in keys:
         mario.x += mario_speed
     if pygame.K_x in keys:
         print("X=", mario.x)


     if mario.x >= 6690:
       mario.x = 6690
       mario.yspeed = 10
       if mario.y >= 450:
           mario.y = 450
           camera.draw(gamebox.from_text(camera.x, camera.y, "You Win", 'Arial', 50, "red"))
           gamebox.pause()






     # Timer
     _tick += 1
     if _tick == 30:
         _tick = 0
         seconds -= 1
     timer = gamebox.from_text(camera.x + 450, 40, str(seconds), "Arial", 30, "white")
     camera.draw(timer)








     # Create death and respawn command
     if mario.y > 650 or pygame.K_r in keys or death == True:
         mario.x = 100
         mario.y = 520
         mario_size = "small"
         mario.size = 30, 42
         death = False


     # Draw all coin boxes
     for i in range(0, len(coin_boxes)):
         box = coin_boxes[i]
         box_replacement = activated_coins[i]
         if mario.top_touches(box) and not coin_activation[i]:
             coins += 1
             camera.draw(coins_list[i])
             coin_activation[i] = True
         if coin_activation[i]:
             camera.draw(box_replacement)
         else:
             camera.draw(box)








     # Draw all mushroom boxes
     for i in range(0, len(mushroom_boxes)):
         box = mushroom_boxes[i]
         box_replacement = activated_mushrooms[i]
         if mario.top_touches(box) and not mushroom_activation[i] and mario_size == "small":
             camera.draw(mushroom_list[i])
             mario.size = 40, 65
             mario_size = "large"
             powered_up = True
             mushroom_activation[i] = True
         if mushroom_activation[i]:
             camera.draw(box_replacement)
         else:
             camera.draw(box)








     # Add in gravity
     mario.yspeed += 1
     # Check all platforms
     for platform in platforms:
         if mario.bottom_touches(platform):
             mario.yspeed = 0
             # Add jumping
             if pygame.K_SPACE in keys:
                 mario.yspeed = -18
         if mario.touches(platform):
             mario.move_to_stop_overlapping(platform)
     mario.move_speed()

     for box in stairs:
         camera.draw(box)








     # Draw Everything
     for box in other_boxes:
         camera.draw(box)
     for cloud in clouds:
         camera.draw(cloud)
     for floor in ground:
         camera.draw(floor)
     for line in separation:
         camera.draw(line)
     for enemy in enemies:
         camera.draw(enemy)
     camera.draw(flag)
     camera.draw(mario)
     if seconds == 0:
           camera.draw(gamebox.from_text(camera.x, camera.y, "You Lost!", "arial", 60, 'red'))
           gamebox.pause()
     camera.display()


ticks_per_second = 30
# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)


