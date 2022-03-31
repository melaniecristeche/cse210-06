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

#         # hide all frames class
#         def hide_all_frames(self):
#             for row in frames:
#                 for frame in row:
#                     frame.showed = False
#                     frame.unhidden = False

#         # randomize_frames class
#         def randomize_frames(self):
#             # Choose X and Y randoms, swap
#             number_of_rows = len(frames)
#             number_of_columns = len(frames[0])
#             for y in range(number_of_rows):
#                 for x in range(number_of_columns):
#                     x_random = random.randint(0, number_of_columns - 1)
#                     y_random = random.randint(0, number_of_rows - 1)
#                     temporal_frame = frames[y][x]
#                     frames[y][x] = frames[y_random][x_random]
#                     frames[y_random][x_random] = temporal_frame