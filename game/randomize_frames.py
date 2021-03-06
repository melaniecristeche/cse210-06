from game.frame import Frame 
import random 

class Randomize_frames(Frame):

    """The Randomize_frames is doing the random process for all the frames
    in each start of the game"""

    def __init__(self):
        
        #self.showed = True
        #self.unhidden = False

        frame = Frame()
        self.frames = frame.get_frames()
        

    def randomize_frames(self):

        # Choose X and Y randoms, swap
        number_of_rows = len(self.frames)
        number_of_columns = len(self.frames[0])

        for y in range(number_of_rows):
            for x in range(number_of_columns):
                x_random = random.randint(0, number_of_columns - 1)
                y_random = random.randint(0, number_of_rows - 1)
                temporal_frame = self.frames[y][x]
                self.frames[y][x] = self.frames[y_random][x_random]
                self.frames[y_random][x_random] = temporal_frame