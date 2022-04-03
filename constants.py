
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
HEIGHT = 750


measure_frame = 200  # Image size in pixels
# The back of each card
unhidden_image_name = b"./assets/oculta.png"
#hidden_image = pygame.image.load(hidden_image_name)
seconds_showed_frame = 2  # Seconds to hide the part if it is not correct

GAME_STARTED = False
last_seconds = None     # To know if we can hide our card during N seconds


# COLUMNS = 40
# ROWS = 20
# CELL_SIZE = 10
# MAX_X = 900
# MAX_Y = 600
# FRAME_RATE = 15
# FONT_SIZE = 15
# Number_of_Cards=20
# CAPTION="Memory Game"