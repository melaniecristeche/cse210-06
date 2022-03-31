# from pyray import *

# class Frame():

#     def __init__(self) -> None:
#         """
#         This class is responsible for collecting the source of each image 
#         (that is, the name of the file)
#          We need the source for later, to compare the cards
#         """
#         self.display = True
#         self.discovered = False
        
#         self.image_source = pyray.ima image_source
#         #self.imagen_real = LoadTexture(image_source)
#         self.image = LoadImage (image_source)
#         # self.imagen = raylib.LoadImage("assets/coco.png")

#     def get_images(self):
#         self.frames = [
#         [Frame(b"./assets/arandano.png"), Frame(b"./assets/arandano.png"),
#         Frame(b"./assets/manzana.png"), Frame(b"./assets/manzana.png")],
#         [Frame(b"./assets/limon.png"), Frame(b"./assets/limon.png"),
#         Frame(b"./assets/naranja.png"), Frame(b"./assets/naranja.png")],
#         [Frame(b"./assets/pera.png"), Frame(b"./assets/pera.png"),
#         Frame(b"./assets/fresa.png"), Frame(b"./assets/fresa.png")],
#         [Frame(b"./assets/platano.png"), Frame(b"./assets/platano.png"),
#         Frame(b"./assets/sandia.png"), Frame(b"./assets/sandia.png")],]

#     # hide all frames class
#     def hide_all_frames(self):
#         for row in self.frames:
#             for frame in row:
#                 frame.display = False
#                 frame.discovered = False