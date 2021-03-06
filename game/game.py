from argparse import Action
from game.frame import Frame
from game.hide_all_frames import Hide_all_frames
from game.randomize_frames import Randomize_frames

import random 
import constants

class Game(Randomize_frames, Hide_all_frames):

    """The Game class is creating the parameters of the game. """

    def __init__(self):
        
        frame = Frame
        self.frames = frame.get_frames()


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

        # Randomize 3 times
        
        for i in range(3):
            self.randomize_frames()
        self.hide_all_frames()

        constants.GAME_STARTED = True

        
    def restart_game(self):
       
        constants.GAME_STARTED = False
        
    
     

   
    
    