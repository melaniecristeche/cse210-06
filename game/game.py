from game.frame import Frame
from game.hide_all_frames import Hide_all_frames
from game.randomize_frames import Randomize_frames

import random 
import constants

class Game:

    def __init__(self):

        game_started = False    # Our game is Started or not, to know if we'll hide or show cards. 

        frame = Frame()
        self.frames = frame.frames()

        rand = Randomize_frames()
        hide = Hide_all_frames()

        self.hide_all_frames = hide.hide_all_frames()
        self.randomize_frames = rand.randomize_frames()

        def check_if_you_win():
            if win():
                restart_game()

        #Return FALSE if at least one frame is not unhidden. TRUE is all frames are unhidden. 
        def win():
            for row in self.frames:
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
                self.randomize_frames()
            self.hide_all_frames()
            game_started = True

  