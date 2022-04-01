from argparse import Action
from game.frame import Frame
from game.hide_all_frames import Hide_all_frames
from game.randomize_frames import Randomize_frames


import random 
import constants

class Game:

    def __init__(self):

        self.game_started = False    # Our game is Started or not, to know if we'll hide or show cards. 


        def check_if_you_win():

            if win():
                restart_game()

        #Return FALSE if at least one frame is not unhidden. TRUE is all frames are unhidden. 
        def win():
            fram = Frame
            frames = fram.frames()

            for row in frames:
                for frame in row:
                    if not frame.unhidden:
                        return False
            return True

        def restart_game(self):

            self.game_started
            game_started = False

            return game_started

        def start_game():

            self.game_started

            rand = Randomize_frames()
            hide = Hide_all_frames()

            hide_all_frames = hide.hide_all_frames()
            randomize_frames = rand.randomize_frames()

            # Randomize 3 times
            for i in range(3):
                randomize_frames
            hide_all_frames
            game_started = True

  