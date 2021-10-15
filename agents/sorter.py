from pade.core.agent import Agent
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import display_message
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
import random

class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)
    
    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.sort_number()

class Sorter(Agent):
    def __init__(self, aid, players):
        super(Sorter, self).__init__(aid=aid, debug=False)
        self.sorted_numbers = []
        self.behaviours.append(ComportTemporal(self, 5.0))
        self.players = players.copy()

    
    def sort_number(self):
        sorted_number = random.randint(1, 75)
        display_message(self.aid.localname, sorted_number)
        display_message(self.aid.localname, self.sorted_numbers)
        while sorted_number in self.sorted_numbers:
            sorted_number = random.randint(1, 75)
        self.sorted_numbers.append(sorted_number)
        message = ACLMessage(ACLMessage.INFORM)
        for player in self.players:
            message.add_receiver(AID(player))
        message.set_content(sorted_number)
        self.send(message)