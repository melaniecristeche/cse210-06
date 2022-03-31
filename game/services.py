from game.frame import Frame
import constants

# We calculate the size of the screen based on the size of the squares
def get_size_square(self):
    screen_width = len(self.frames[0]) * constants.measure_frame
    screen_height = (len(self.frames) * constants.measure_frame) + constants.button_height
    button_width = screen_width