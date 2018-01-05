# game timer

import pygame
import gamebox
camera = gamebox.Camera(800,600)

time = 9000

def tick(keys):
    global time

    # clear display
    camera.clear("blue")

    # increase timer
    time -= 1

    # calculate minutes,seconds,fractions of seconds
    frac = str(int((time%ticks_per_second)/ticks_per_second*10))
    seconds = str(int((time/ticks_per_second)%60)).zfill(2)
    minutes = str(int((time/ticks_per_second)/60))

    # write timer to screen
    timer = gamebox.from_text(50,100,minutes+":"+seconds+"."+frac,"Arial",24,"red")
    camera.draw(timer)
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)


#Define the flag
flag = gamebox.from_image(50, 440, "http://img09.deviantart.net/0464/i/2011/324/a/e/secret_flagpole_by_yoshigo99-d4b7f6b.png")