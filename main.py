from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from sys import argv
from agents.card import Card
from agents.player import Player
from agents.sorter import Sorter

class AgenteHelloWorld(Agent):
  def __init__(self, aid):
    super(AgenteHelloWorld, self).__init__(aid=aid)
    display_message(self.aid.localname, 'Hello World!')

if __name__ == '__main__':
  agents = list()
  c = 0
  number_of_players = 3
  players_name = []
  port = int(argv[1]) 
  for i in range(number_of_players):
    ## Criando cartelas do bingo
    card_name = 'agent_card_{}@localhost:{}'.format(port, port)
    agent_card = Card(AID(name=card_name))
    port+=1
    agents.append(agent_card)
    ## Criando jogadores do bingo
    player_name = 'agent_player_{}@localhost:{}'.format(port, port)
    players_name.append(player_name)
    agent_player = Player(AID(player_name), agent_card)
    agents.append(agent_player)
    port+=1
    ## Criando globo sorteador
  sorter_name = 'agent_sorter_{}@localhost:{}'.format(port, port)
  agente_sorter = Sorter(AID(name=sorter_name), players_name)
  agents.append(agente_sorter)
  port+=1

  start_loop(agents)
