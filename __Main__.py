
from pyray import is_mouse_button_down, is_mouse_button_pressed

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

# The button, which at the end is a rectangle
#DrawRectangle (HEIGHT - constants.button_height,int(HEIGHT/2), 30,30,BLUE)
#button = rect (0, screen_height - constants.button_height,
# button_width, screen_height)


class Frame:
    def __init__(self, image_source):
        self.display = True
        self.discovered = False
        """
        This class is responsible for collecting the source of each image 
        (that is, the name of the file)
         We need the source for later, to compare the cards
        """
        
        self.image_source = image_source
        #self.imagen_real = LoadTexture(image_source)
        self.image = LoadImage (image_source)
        # self.imagen = raylib.LoadImage("assets/coco.png")

frames = [
    [Frame(b"./assets/coco.png"), Frame(b"./assets/coco.png"),
     Frame(b"./assets/manzana.png"), Frame(b"./assets/manzana.png")],
    [Frame(b"./assets/limon.png"), Frame(b"./assets/limon.png"),
     Frame(b"./assets/naranja.png"), Frame(b"./assets/naranja.png")],
    [Frame(b"./assets/pera.png"), Frame(b"./assets/pera.png"),
     Frame(b"./assets/pina.png"), Frame(b"./assets/pina.png")],
    [Frame(b"./assets/platano.png"), Frame(b"./assets/platano.png"),
     Frame(b"./assets/sandia.png"), Frame(b"./assets/sandia.png")],
 ]



# hide all frames class
def hide_all_frames():
    for row in frames:
        for frame in row:
            frame.display = False
            frame.discovered = False

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

# draw frames class
def draw_frames():
    x = 0
    y = 0
    # loop through the frames
    for row in frames:
        x = 0
        for frame in row:
            """
            If it is discovered or should be displayed, we draw the real image. 
            If not, we draw the hidden image
            """
            if frame.discovered or frame.display:
                name_name = b"./assets/manzana.png"
                #name_name = Frame.image_source
                scarfy1 = LoadTexture(name_name)
                #DrawTexture(Frame.image_source)
                DrawTexture(scarfy1, x, y, RAYWHITE)
                #game_screen.blit(Frame.imagen_real, (x, y))

            else:
                #game_screen.blit(constants.imagen_oculta, (x, y))
                name_name = b"./assets/oculta.png"
                #name_name = Frame.image_source
                scarfy1 = LoadTexture(name_name)
                DrawTexture(scarfy1, x, y, RAYWHITE)
            x += constants.measure_frame
        y += constants.measure_frame

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

# game class
def check_if_you_win():
    if win():
        restart_game()

def win():
    for row in frames:
        for frame in row:
            if not frame.discovered:
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

def main():
    #The button´s font
    font_size = 20

    # flags
    # Flag to know if the card should be hidden within N seconds
    last_seconds = None
    can_play = True  # Flag to know whether to react to user events
    # Know if the game is started; so we know whether to hide or display pieces, in addition to the button
    game_started = False
    # flags the cards when looking for a pair. We need them as indices for the frame array
     # x1 with y1 are for the first card
    
    x1 = None
    y1 = None
    # And the following for the second card
    x2 = None
    y2 = None

    """
    Funciones útiles
    """
    #start_game()

      
    #hide_all_frames()
    #draw_frames()

    
    value = 1
   
    InitWindow (WIDTH, HEIGHT, b"Working with Images")
    SetTargetFPS(60)
        
    while not WindowShouldClose():
            
        BeginDrawing()
        ClearBackground(RAYWHITE)
            
        xPosMouse = GetMouseX()
        yPosMouse = GetMouseX()
        #print ("LLEGASTE")
        # if is_mouse_button_pressed(False) and can_play:
        
        prove = is_mouse_button_pressed (False)
        if  (prove == 0 and can_play):
            xPosMouse = GetMouseX()
            yPosMouse = GetMouseX()
            #print (prove)
            if not game_started:
                start_game()
        else:
            if not game_started:
                continue
            x = math.floor(xPosMouse / constants.measure_frame)
            y = math.floor(yPosMouse / constants.measure_frame)

            frame = frames[y][x]
            if frame.display or frame.discovered:
                continue

            if x1 is None and y1 is None:
                x1 = x
                y1 = y
                frames[y1][x1].display = True
            else:
                x2 = x
                y2 = y
                frames[y2][x2].display = True
                Frame1 = frames[y1][x1]
                Frame2 = frames[y2][x2]

                if Frame1.image_source == Frame2.image_source:
                    frames[y1][x1].discovered = True
                    frames[y2][x2].discovered = True
                    x1 = None
                    x2 = None
                    y1 = None
                    y2 = None
                else:
                    last_seconds = int(time.time())
                    can_play = False
            check_if_you_win()
        EndDrawing()

        now = int(time.time())

        if last_seconds is not None and now - last_seconds >= constants.seconds_display_frame:
            frames[y1][x1].display = False
            frames[y2][x2].display = False
            x1 = None
            y1 = None
            x2 = None
            y2 = None
            last_seconds = None
            # At this point the user can click again as the images will already be hidden
            can_play = True

        x = 0
        y = 0
        # loop through the frames
        for row in frames:
            x = 0
            for frame in row:
                """
                If it is discovered or should be displayed, we draw the real image. 
                If not, we draw the hidden image
                """
                if frame.discovered or frame.display:
                    name_name = b"./assets/manzana.png"
                    scarfy1 = LoadTexture(name_name)
                    DrawTexture(scarfy1, x, y, RAYWHITE)
                    #game_screen.blit(Frame.imagen_real, (x, y))

                else:
                    #game_screen.blit(constants.imagen_oculta, (x, y))
                    # name_name = b"./assets/oculta.png"
                    name_name = frame.image_source
                    scarfy1 = LoadTexture(name_name)
                    DrawTexture(scarfy1, x, y, RAYWHITE)
                x += constants.measure_frame
            y += constants.measure_frame
            
    CloseWindow()
    
if __name__ == "__main__":
    exit(main())