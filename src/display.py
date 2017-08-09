import numpy as np
import scipy.misc as smp

from src.vector import Vector as vect

def find_screen_center(screen_width, screen_height, screen_depth):
    x = screen_width/2
    y = screen_height/2
    z = screen_depth
    center = vect(x,y,z)
    return center

def find_absolute_screen_position(relative_position, screen_center):
    x = relative_position[0]
    y = relative_position[1]

    delta_x = -1*screen_center[0]
    delta_y = +1*screen_center[1]
    delta_z = +1*screen_center[2]

    return vect(x + delta_x, y + delta_y, delta_z)

def initialize_screen(screen_width, screen_height):
    screen = np.zeros( (screen_height, screen_width, 3), dtype=np.uint8 )
    return screen 

def write_screen_pixel(screen, position, color):
    x = position[0]
    y = position[1]

    screen[-y,x] = tuple(color)

def display_image(screen):
    image = smp.toimage(screen)
    image.save('output.png')
    image.show()
