from pyray import is_mouse_button_pressed
import raylib
import random 

from raylib import *

class Frame:

    def __init__(self, image_source):

        """
    This class is responsible for collecting the source of each image 
    (that is, the name of the file)
    We need the source for later, to compare the cards
    """

        self.showed = True
        self.unhidden = False
               
        self.image_source = image_source
        #self.imagen_real = LoadTexture(image_source)
        self.real_image = LoadImage (image_source)
        # self.imagen = raylib.LoadImage("assets/coco.png")

        self._frames = [
                [Frame(b"./assets/arandano.png"), Frame(b"./assets/arandano.png"),
                Frame(b"./assets/manzana.png"), Frame(b"./assets/manzana.png")],
                [Frame(b"./assets/limon.png"), Frame(b"./assets/limon.png"),
                Frame(b"./assets/naranja.png"), Frame(b"./assets/naranja.png")],
                [Frame(b"./assets/pera.png"), Frame(b"./assets/pera.png"),
                Frame(b"./assets/fresa.png"), Frame(b"./assets/fresa.png")],
                [Frame(b"./assets/platano.png"), Frame(b"./assets/platano.png"),
                Frame(b"./assets/sandia.png"), Frame(b"./assets/sandia.png")],]

        def frames(self):
            
            return self._frames

        