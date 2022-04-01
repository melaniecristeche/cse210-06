
"""
Variables and configurations that we are going to use throughout the program
"""

# Colors
LIGHTGRAY = (200, 200, 200, 255)
RAYWHITE = (245, 245, 245, 255)  # raylib logo white
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK= (0,0,0)


WIDTH = 800
HEIGHT = 800


button_height = 50  # The button below, to start game
measure_frame = 200  # Image size in pixels
# The back of each card
unhidden_image_name = b"./assets/oculta.png"
#hidden_image = pygame.image.load(hidden_image_name)
seconds_showed_frame = 2  # Seconds to hide the part if it is not correct

"""
A class that represents the frame. He himself has an image and can be
discovered (when it has already been discovered before and it is not the card currently being searched for)
or it can be displayed (when the image is flipped)
It also has a source or image name that will serve to compare it later
"""


# COLUMNS = 40
# ROWS = 20
# CELL_SIZE = 10
# MAX_X = 900
# MAX_Y = 600
# FRAME_RATE = 15
# FONT_SIZE = 15
# Number_of_Cards=20
# CAPTION="Memory Game"