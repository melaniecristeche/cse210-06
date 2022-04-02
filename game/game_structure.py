
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

class Game_structure(Game):

    def __init__(self):

        #Flags
        self.game_started = False    # Our game is Started or not, to know if we'll hide or show cards. 
        self.last_seconds = None     # To know if we can hide our card during N seconds
        self.can_play = True         # To know if we can react to user events 

        self.xPosMouse = 0
        self.yPosMouse = 0
        self.sigue = 1

        # First Card            # When we are looking for a pair card, we'll need indexs to the List.
        self.x1 = None               
        self.y1 = None

        # Second Card
        self.x2 = None
        self.y2 = None

        frame = Frame
        self.frames = frame.frames()

        self.start_game()
        self.check_if_you_win()
        self.hide_all_frames()
        self.randomize_frames()


    def game_structure(self):
    
        InitWindow (constants.WIDTH, constants.HEIGHT, b"Memory Game")
        SetTargetFPS(60)

    
        while not WindowShouldClose():

                BeginDrawing()
                #raylib.DrawText(b"Press letter B to star game", 80, 700,20, constants.RED)
                ClearBackground(constants.RAYWHITE)
                
                #if IsKeyDown(KEY_B) and can_play:
                if self.can_play:
                    if not self.game_started:
                        self.start_game()

                    self.xPosMouse = GetMouseX()
                    self.yPosMouse = GetMouseY()

                    if is_mouse_button_pressed(raylib.MOUSE_BUTTON_LEFT) :
                        x = int(math.floor(self.xPosMouse / constants.measure_frame))
                        y = int(math.floor(self.yPosMouse / constants.measure_frame))

                        frame = self.frames[y][x]

                        showed = True
                        unhidden = False

                        if frame.showed or frame.unhidden:
                            continue

                        if self.x1 is None and self.y1 is None:
                            x1 = x
                            y1 = y
                            self.frames[y1][x1].showed = True
                        else:
                            x2 = x
                            y2 = y
                            self.frames[y2][x2].showed = True
                            frame1 = self.frames[y1][x1]
                            frame2 = self.frames[y2][x2]

                            if frame1.image_source == frame2.image_source:
                                self.frames[y1][x1].unhidden = True
                                self.frames[y2][x2].unhidden = True
                                x1 = None
                                x2 = None
                                y1 = None
                                y2 = None
                            else:
                                self.last_seconds = int(time.time())
                                self.can_play = False
                        self.check_if_you_win()    
                    
                now = int(time.time())

                if self.last_seconds is not None and now - self.last_seconds >= constants.seconds_showed_frame:
                    self.frames[y1][x1].showed = False
                    self.frames[y2][x2].showed = False

                #ClearBackground(RAYWHITE)
                x = 0
                y = 0

                # loop through the self.frames
                for row in self.self.frames:
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
    
 
