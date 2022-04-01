# from game.frame import Frame 
# import random 

# class Randomize_frames():

# randomize_frames class
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