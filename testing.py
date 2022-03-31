from pyray import is_mouse_button_pressed
import raylib
import random



width_window = 800
heigth_window = 450
boxposY = 200

YELLOW = (255, 255, 0) 
RED = (255, 0, 0)
BLUE = (0, 0, 255)

scrollSpeed = 4

title_screen = b"Testing my code"

raylib.InitWindow(width_window, heigth_window, title_screen)

raylib.SetTargetFPS(60)


while not raylib.WindowShouldClose():
    raylib.BeginDrawing()
    raylib.ClearBackground = [BLUE]
        
    raylib.DrawText(b"Congrats! Mother Facts", 40,100,40,YELLOW)
    posX = raylib.GetMouseX()
    posY = raylib.GetMouseY()
    if is_mouse_button_pressed(raylib.MOUSE_BUTTON_LEFT):
        print ("YOU PRESSED LEFT CLICK")
        print(f"X={posX}")
        print(f"Y={posX}")

        for i in range (3):
            random_color = random.randint(1,3)
        if random_color == 1:
            raylib.DrawRectangle(posX, posY, 80,80, YELLOW)
        elif random_color == 2:
            raylib.DrawRectangle(posX, posY, 80,80, BLUE)
        else:
            raylib.DrawRectangle(posX, posY, 80,80, RED)
    
    boxposY = boxposY- int(raylib.GetMouseWheelMove()) * scrollSpeed
    raylib.DrawRectangle(400, boxposY, 80, 80, (0,0,255))

        #raylib.DrawText (raylib.TextFormat("Box position Y: ", boxposY), 10,40,20,RED)

        #raylib.DrawText (raylib.TextFormat("Box position Y: ", boxposY), 10,40,20,RED)

    raylib.EndDrawing()

raylib.CloseWindow()