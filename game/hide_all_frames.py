from game.frame import Frame

class Hide_all_frames(Frame):

    def __init__(self):

        self.showed = True
        self.unhidden = False
        self.frames()
        
    def hide_all_frames(self):

        for row in self.frames:
            for frame in row:
                frame.showed = False
                frame.unhidden = False
