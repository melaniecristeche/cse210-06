from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        red_cards = cast.get_first_actor("red_cards")
        yellow_cards = cast.get_first_actor("yellow_cards")
        blue_cards = cast.get_first_actor("blue_cards")
        green_cards = cast.get_first_actor("green_cards")
        black_cards = cast.get_first_actor("black_cards")
        

        self._video_service.clear_buffer()
        self._video_service.draw_actor(red_cards)
        self._video_service.draw_actor(yellow_cards)
        self._video_service.draw_actor(blue_cards)
        self._video_service.draw_actor(green_cards)
        self._video_service.draw_actor(black_cards)
        self._video_service.flush_buffer()