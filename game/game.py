from argparse import Action
from game.frame import Frame
from game.hide_all_frames import Hide_all_frames
from game.randomize_frames import Randomize_frames

import random 
import constants

class Game(Randomize_frames, Hide_all_frames):

    """The Game class is creating the parameters of the game. """

    def __init__(self):

        #self.game_started = False    # Our game is Started or not, to know if we'll hide or show cards.
        #self.showed = True
        #self.unhidden = False
        
        #self.hide_all_frames()
        #self.randomize_frames()

        #self.win()
        #self.restart_game()
        
        frame = Frame
        self.frames = frame.frames()


    def win(self):

        """Return FALSE if at least one frame is not unhidden. TRUE is all frames are unhidden. """

        for row in self.frames:
            for frame in row:
                if not frame.unhidden:
                    return False
        return True
    
    def check_if_you_win(self):
        if self.win():
           self.restart_game()
  
    def start_game(self):
        #self.game_started
        
        #global game_started
        # Randomize 3 times
        
        for i in range(3):
            self.randomize_frames()
        self.hide_all_frames()

        constants.GAME_STARTED = True
        #game_started = True
        
    def restart_game(self):
        #global game_started
        
        constants.GAME_STARTED = False
        
        #game_started = False
     

   
    
    