from pade.core.agent import Agent
from pade.misc.utility import display_message

class Player(Agent):
    def __init__(self, aid, card):
        super(Player, self).__init__(aid=aid)
        self.card = card
    
    def react(self, message):
        self.card.check_number(message.content)
        if(self.card.count == 25):
            display_message("Bingoooooo")