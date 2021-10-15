from pade.core.agent import Agent
from pade.misc.utility import display_message

class Player(Agent):
    def __init__(self, aid, card):
        super(Player, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Hello world')
    
    def react(self, message):
        pass