from game.actor import Actor






class card(Actor):
    """this class holds information for a Card. which should only contain a certain color, and should reveal its color when clicked on.
    
    self.card_color is the color of the card declared at the beginning of the game
    """
    
    def __init__(self,color):
        super().__init__()
        
        self.card_color=color
        
        
        
    
    def get_card_color(self):
        card_color=self.card_color
        return card_color
    
    
        
