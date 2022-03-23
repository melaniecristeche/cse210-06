
import constants
from game.actor import Actor
from game.card import card
from game.cast import Cast
from game.color import Color
from game.directing.director import Director
from game.point import Point
from game.services.video_service import VideoService
from game.services.keyboard_service import KeyboardService
from game.scripting.script import Script


def main():
       
    # create the cast
    cast = Cast()
    for i in range(1):
        cast.add_actor("red_cards",card(color=constants.RED))
        cast.add_actor("blue_cards",card(color=constants.BLUE))
        cast.add_actor("yellow_cards",card(color=constants.YELLOW))
        cast.add_actor("green_cards",card(color=constants.GREEN))
        cast.add_actor("black_cards",card(color=constants.BLACK))
            

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
   
    script = Script()
    # script.add_action("input", ControlActorsAction(keyboard_service))
    # script.add_action("update", MoveActorsAction())
    # script.add_action("update", HandleCollisionsAction())
    # script.add_action("output", DrawActorsAction(video_service))
    
    
    director = Director(video_service)
    director.start_game(cast, script)
   

if __name__ == "__main__":
    main()
