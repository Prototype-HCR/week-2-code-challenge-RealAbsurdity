import time
import neopixel
import board
import digitalio
from rainbowio import colorwheel

# make a neopixel object for 10 pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# declare some inputs for button a and b
button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.DOWN)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(pull=digitalio.Pull.DOWN)

# declare some color constants
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
RAINBOW = None

color_chase_demo = 0
flash_demo = 0
rainbow_demo = 0
rainbow_cycle_demo = 0

# declare a function to do a rainbow animation
def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = colorwheel(idx & 255)
        pixels.show()
        time.sleep(wait)

# declare a function to cycle the rainbow
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(10):
            rc_index = (i * 256 // 10) + j * 5
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

color = 0

while True:
    # gather input values
    button_a_read = button_A.value
    button_b_read = button_B.value

    # set variables based on input
    # set variables based on input
    if button_a_read and button_b_read:
        color = RAINBOW
        #time.sleep(1)
    elif button_a_read:
        color = RED
        #time.sleep(1)
    elif button_b_read:
        color = GREEN
        #time.sleep(1)
    else:
        color = OFF

    # do ouput
    if color != RAINBOW:
        pixels.fill(color)
    else:
        rainbow_cycle(0.01)
    pixels.show()
