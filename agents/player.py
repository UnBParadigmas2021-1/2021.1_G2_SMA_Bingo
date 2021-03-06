from pade.core.agent import Agent
from pade.misc.utility import display_message
from classes.card import Card
from twisted.internet import reactor


class Player(Agent):
    def __init__(self, aid):
        super(Player, self).__init__(aid=aid, debug=False)
        self.card = Card()
    
    def react(self, message):
        display_message(self.aid.localname, message.content)
        self.card.check_number(message.content)
        if(self.card.check_bingo()):
            display_message(self.aid.localname, "Bingoooooo")
            reactor.callFromThread(reactor.stop)
        