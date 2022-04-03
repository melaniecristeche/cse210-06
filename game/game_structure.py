
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
    """This Game_structure class is in charge of the functionality of the class Game
    and implements all the other functions in one class"""
    
    #game_started = False
    # Our game is Started or not, to know if we'll hide or show cards. 
    

    def __init__(self):
        
        self.showed = True      #ready
        self.unhidden = False   #ready

        frame = Frame
        self.frames = frame.get_frames()
        
        #Flags
        constants.last_seconds = None        
        self.can_play = True        
        constants.GAME_STARTED = False
        
        # When we are looking for a pair card, we'll need indexs to the List.
        # First Card            
        self.x1 = None               
        self.y1 = None

        # Second Card
        self.x2 = None
        self.y2 = None
        
        self.xPosMouse = 0
        self.yPosMouse = 0

        InitWindow (constants.WIDTH, constants.HEIGHT, b"Memory Game")
        SetTargetFPS(60)
    
    def game_structure(self):

        while not WindowShouldClose():
            BeginDrawing()
            #raylib.DrawText(b"Press letter B to star game", 80, 700,20, constants.RED)
            ClearBackground(constants.RAYWHITE)
            
            if self.can_play:
                #if not self.game_started:    
                if not constants.GAME_STARTED:
                    self.start_game()

                self.xPosMouse = GetMouseX()
                self.yPosMouse = GetMouseY()

                if is_mouse_button_pressed(raylib.MOUSE_BUTTON_LEFT) :
                    x = int(math.floor(self.xPosMouse / constants.measure_frame))
                    y = int(math.floor(self.yPosMouse / constants.measure_frame))

                    frame = self.frames[y][x]

                    # showed = True
                    # unhidden = False

                    if frame.showed or frame.unhidden:
                        continue

                    if self.x1 is None and self.y1 is None:
                        self.x1 = x
                        self.y1 = y
                        self.frames[self.y1][self.x1].showed = True
                    else:
                        self.x2 = x
                        self.y2 = y
                        self.frames[self.y2][self.x2].showed = True
                        frame1 = self.frames[self.y1][self.x1]
                        frame2 = self.frames[self.y2][self.x2]

                        if frame1.image_source == frame2.image_source:
                            self.frames[self.y1][self.x1].unhidden = True
                            self.frames[self.y2][self.x2].unhidden = True
                            self.x1 = None
                            self.x2 = None
                            self.y1 = None
                            self.y2 = None
                        else:
                            constants.last_seconds = int(time.time())
                            self.can_play = False
                    self.check_if_you_win()    
                
            now = int(time.time())

            if constants.last_seconds is not None and now - constants.last_seconds >= constants.seconds_showed_frame:
                self.frames[self.y1][self.x1].showed = False
                self.frames[self.y2][self.x2].showed = False
                self.x1 = None
                self.x2 = None
                self.y1 = None
                self.y2 = None
                constants.last_seconds = None
                self.can_play = True

            #ClearBackground(RAYWHITE)
            x = 0
            y = 0

            # loop through the self.frames
            for row in self.frames:
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
    
 
