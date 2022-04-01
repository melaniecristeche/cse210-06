from game.frame import Frame

class Hide_all_frames(Frame):

    def __init__(self):

        self.showed = True
        self.unhidden = False
        
    def hide_all_frames(self):

        frame = Frame()
        self.frames = frame.frames()

        for row in self.frames:
            for frame in row:
                frame.showed = False
                frame.unhidden = False
