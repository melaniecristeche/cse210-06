# from game.frame import Frame
# import random 
# import constants

# class Game():

#     def __init__(self):

#         frames = self.frames()

#         def check_if_you_win():
#             if win():
#                 restart_game()

#         #Return FALSE if at least one frame is not unhidden. TRUE is all frames are unhidden. 
#         def win():
#             for row in frames:
#                 for frame in row:
#                     if not frame.unhidden:
#                         return False
#             return True

#         def restart_game():
#             global game_started
#             game_started = False

#         def start_game():
#             global game_started
#             # Randomize 3 times
#             for i in range(3):
#                 randomize_frames()
#             hide_all_frames()
#             game_started = True

  