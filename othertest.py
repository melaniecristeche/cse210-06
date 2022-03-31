
from pyray import is_mouse_button_pressed
import pyray
import raylib

import constants
import sys
import math
import time
import random

from raylib import * 

WIDTH = 700
HEIGHT = 700

LIGHTGRAY = (200, 200, 200, 255)
RAYWHITE = (245, 245, 245, 255)  # raylib logo white
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0) 
RED = (255, 0, 0)

last_seconds = None
can_play = True 
game_started = False
x1 = None
y1 = None
x2 = None
y2 = None

# The button, which at the end is a rectangle
#DrawRectangle (HEIGHT - constants.button_height,int(HEIGHT/2), 30,30,BLUE)
#button = rect (0, screen_height - constants.button_height,
# button_width, screen_height)
"""
    This class is responsible for collecting the source of each image 
    (that is, the name of the file)
    We need the source for later, to compare the cards
    """

class Frame:
    def __init__(self, image_source):

        self.showed = True
        self.hidden = False
               
        self.image_source = image_source
        #self.imagen_real = LoadTexture(image_source)
        self.image = LoadImage (image_source)
        # self.imagen = raylib.LoadImage("assets/coco.png")

frames = [
    [Frame(b"./assets/arandano.png"), Frame(b"./assets/arandano.png"),
     Frame(b"./assets/manzana.png"), Frame(b"./assets/manzana.png")],
    [Frame(b"./assets/limon.png"), Frame(b"./assets/limon.png"),
     Frame(b"./assets/naranja.png"), Frame(b"./assets/naranja.png")],
    [Frame(b"./assets/pera.png"), Frame(b"./assets/pera.png"),
     Frame(b"./assets/fresa.png"), Frame(b"./assets/fresa.png")],
    [Frame(b"./assets/platano.png"), Frame(b"./assets/platano.png"),
     Frame(b"./assets/sandia.png"), Frame(b"./assets/sandia.png")],]

# raylib.draw
# raylib.DrawRectangle(400, boxposY, 80, 80, (0,0,255))
# boton = pyray.Rectangle
# screen = InitWindow (WIDTH, HEIGHT, b"Working with Images")
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (206, 206, 206)
blue = (30, 136, 229)

# We calculate the size of the screen based on the size of the squares
screen_width = len(frames[0]) * constants.measure_frame
screen_height = (len(frames) * constants.measure_frame) + constants.button_height
button_width = screen_width

def start_game():
    global game_started
    # Randomize 3 times
    for i in range(3):
        randomize_frames()
    hide_all_frames()
    game_started = True

# randomize_frames class
def randomize_frames():
    # Choose X and Y randoms, swap
    number_of_rows = len(frames)
    number_of_columns = len(frames[0])
    for y in range(number_of_rows):
        for x in range(number_of_columns):
            x_random = random.randint(0, number_of_columns - 1)
            y_random = random.randint(0, number_of_rows - 1)
            temporal_frame = frames[y][x]
            frames[y][x] = frames[y_random][x_random]
            frames[y_random][x_random] = temporal_frame

# hide all frames class
def hide_all_frames():
    for row in frames:
        for frame in row:
            frame.showed = False
            frame.hidden = False
# game class
def check_if_you_win():
    if win():
        restart_game()

def win():
    for row in frames:
        for frame in row:
            if not frame.hidden:
                return False
    return True

def restart_game():
    global game_started
    game_started = False

InitWindow (WIDTH, HEIGHT, b"Memory Game")
SetTargetFPS(60)     
xPosMouse = 0
yPosMouse = 0
continue_start_game = 0



while not WindowShouldClose():
    BeginDrawing()
    raylib.DrawRectangle(10, 650, 80,80, RED)
    ClearBackground(RAYWHITE)

    #start_game()

    if is_mouse_button_pressed(raylib.MOUSE_BUTTON_RIGHT) and can_play:
        # print ("helo")
        if is_mouse_button_pressed(raylib.MOUSE_BUTTON_LEFT):
            xPosMouse = GetMouseX()
            yPosMouse = GetMouseY()

            if not game_started:
                start_game()
            
        else:
            if not game_started:
                continue

            x = int(math.floor(xPosMouse / constants.measure_frame))
            y = int(math.floor(yPosMouse / constants.measure_frame))

            frame = frames[y][x]
            
            if frame.showed or frame.hidden:
                continue

            if x1 is None and y1 is None:
                x1 = x
                y1 = y
                frames[y1][x1].showed = True
            else:
                x2 = x
                y2 = y
                frames[y2][x2].showed = True
                frame1 = frames[y1][x1]
                frame2 = frames[y2][x2]

                if frame1.image_source == frame2.image_source:
                    frames[y1][x1].hidden = True
                    frames[y2][x2].hidden = True
                    x1 = None
                    x2 = None
                    y1 = None
                    y2 = None
                else:
                    last_seconds = int(time.time())
                    can_play = False
            check_if_you_win()
        
    now = int(time.time())

    if last_seconds is not None and now - last_seconds >= constants.seconds_showed_frame:
        frames[y1][x1].showed = False
        frames[y2][x2].showed = False
        x1 = None
        y1 = None
        x2 = None
        y2 = None
        last_seconds = None
        # At this point the user can click again as the images will already be hidden
        can_play = True
    ClearBackground(RAYWHITE)
    x = 0
    y = 0
     # loop through the frames
    for row in frames:
        x = 0
        for frame in row:

            if frame.hidden or frame.showed:
                name_image = frame.image_source
                scarfy1 = LoadTexture(name_image)
                
                DrawTexture(scarfy1, x, y, RAYWHITE)
                    #game_screen.blit(Frame.imagen_real, (x, y))

            else:
                name_image = constants.hidden_image_name
                scarfy1 = LoadTexture(name_image)
                DrawTexture(scarfy1, x, y, RAYWHITE)
            x += constants.measure_frame
        y += constants.measure_frame

    EndDrawing()    
CloseWindow()

