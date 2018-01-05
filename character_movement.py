# Very simple character movement example.
# Craig Dill (cd9au)
# When gamebox.timer_loop() method calls the tick method it sends a set of keys pressed to the keys parameter.
# pygame defines the keys with constants and these constants are used to test if particular key (combinations)
# are currently pressed by the user.
import pygame
import gamebox

camera = gamebox.Camera(800, 600)        # size of window
character = gamebox.from_color(camera.x, camera.y, "green", 10, 10)


def tick(keys):
    # Use pygame key definitions to detect user keyboard input.  Parameter keys can  have more than one key
    # if the decision statements below are converted into if elif, only one key is detected each tick, even though
    # multiple keys are pressed
    if pygame.K_RIGHT in keys:
        character.x += 1
    if pygame.K_LEFT in keys:
        character.x -= 1
    if pygame.K_UP in keys:
        character.y -= 1
    if pygame.K_DOWN in keys:
        character.y += 1
    camera.clear("red")
    camera.draw(character)
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

