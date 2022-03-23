from game.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        
        super().__init__()
        self._message = ""

    def get_message(self):
        """Reach the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the provided one.
        
        Args:
            message (string): The provided message.
        """
        self._message = message