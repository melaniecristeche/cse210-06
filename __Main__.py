
from pyray import is_mouse_button_pressed
import raylib

from game.frame import Frame 
from game.game import Game
from game.hide_all_frames import Hide_all_frames
from game.randomize_frames import Randomize_frames

import constants
import sys
import math
import time
import random

from raylib import * 

"""
    This class is responsible for collecting the source of each image 
    (that is, the name of the file)
    We need the source for later, to compare the cards
    """

class Frame:
    def __init__(self, image_source):

        self.showed = True
        self.unhidden = False
               
        self.image_source = image_source
        #self.imagen_real = LoadTexture(image_source)
        self.real_image = LoadImage (image_source)
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


# We calculate the size of the screen based on the size of the squares
screen_width = len(frames[0]) * constants.measure_frame
screen_height = (len(frames) * constants.measure_frame) + constants.button_height
button_width = screen_width


#Flags
last_seconds = None     # To know if we can hide our card during N seconds
can_play = True         # To know if we can react to user events 
game_started = False    # Our game is Started or not, to know if we'll hide or show cards. 

# First Card            # When we are looking for a pair card, we'll need indexs to the List.
x1 = None               
y1 = None

# Second Card
x2 = None
y2 = None

# hide all frames class
def hide_all_frames():
    for row in frames:
        for frame in row:
            frame.showed = False
            frame.unhidden = False

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

# game class
def check_if_you_win():
    if win():
        restart_game()

#Return FALSE if at least one frame is not unhidden. TRUE is all frames are unhidden. 
def win():
    for row in frames:
        for frame in row:
            if not frame.unhidden:
                return False
    return True

def restart_game():
    global game_started
    game_started = False

def start_game():
    global game_started
    # Randomize 3 times
    for i in range(3):
        randomize_frames()
    hide_all_frames()
    game_started = True

InitWindow (constants.WIDTH, constants.HEIGHT, b"Memory Game")
SetTargetFPS(60)


xPosMouse = 0
yPosMouse = 0
sigue = 1

while not WindowShouldClose():
    BeginDrawing()
    #raylib.DrawText(b"Press letter B to star game", 80, 700,20, constants.RED)
    ClearBackground(constants.RAYWHITE)
    
    #if IsKeyDown(KEY_B) and can_play:
    if can_play:
        if not game_started:
            start_game()

        xPosMouse = GetMouseX()
        yPosMouse = GetMouseY()

        if is_mouse_button_pressed(raylib.MOUSE_BUTTON_LEFT) :
            x = int(math.floor(xPosMouse / constants.measure_frame))
            y = int(math.floor(yPosMouse / constants.measure_frame))

            frame = frames[y][x]
            
            if frame.showed or frame.unhidden:
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
                    frames[y1][x1].unhidden = True
                    frames[y2][x2].unhidden = True
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
        # At this point the user can click again as the images will already be unhidden
        can_play = True

    #ClearBackground(RAYWHITE)
    x = 0
    y = 0

     # loop through the frames
    for row in frames:
        x = 0
        for frame in row:

            if frame.unhidden or frame.showed:
                name_image = frame.image_source
                scarfy1 = LoadTexture(name_image)
                DrawTexture(scarfy1, x, y, constants.RAYWHITE)
            else:
                name_image = constants.unhidden_image_name
                scarfy1 = LoadTexture(name_image)
                DrawTexture(scarfy1, x, y, constants.RAYWHITE)      
            x += constants.measure_frame
        y += constants.measure_frame
    EndDrawing()    
CloseWindow()