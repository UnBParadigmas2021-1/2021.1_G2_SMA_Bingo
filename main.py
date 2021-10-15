from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from sys import argv
from agents.card import Card
from agents.player import Player

class AgenteHelloWorld(Agent):
  def __init__(self, aid):
    super(AgenteHelloWorld, self).__init__(aid=aid)
    display_message(self.aid.localname, 'Hello World!')

if __name__ == '__main__':
  agents = list()
  c = 0
  number_of_players = 3
  port = int(argv[1]) 
  for i in range(number_of_players):
    ## Criando cartelas do bingo
    card_name = 'agent_card_{}@localhost:{}'.format(port, port)
    agent_card = Card(AID(name=card_name))
    port+=1
    ## Criando jogadores do bingo
    player_name = 'agent_player_{}@localhost:{}'.format(port, port)
    agent_player = Player(AID(player_name))
    agents.append(agent_card)
    agents.append(agent_player)
    port+=1

  start_loop(agents)
