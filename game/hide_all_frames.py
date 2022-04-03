from game.frame import Frame

class Hide_all_frames(Frame):

    """The Hide_all_frames is doing the hiding process for each frame"""

    def __init__(self):

        #self.showed = True
        #self.unhidden = False
        
        frame = Frame()
        self.frames = frame.frames()
        
    def hide_all_frames(self):
        for row in self.frames:
            for frame in row:
                frame.showed = False
                frame.unhidden = False
