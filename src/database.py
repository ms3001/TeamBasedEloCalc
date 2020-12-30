import plotly.graph_objects as go
#import plotly.express as px

from player import Player
from util import checkDup

class Database:
  """ A class to store all players and associated information"""
  def __init__(self):
    self.players = {}

  def __getstate__(self):
    return self.__dict__.copy()

  def __setstate__(self, state):
    self.__dict__.update(state)

  def AddNewPlayer(self, player):
    player = checkDup(player)
    if player in self.players:
      #print("Nice try NERD this player already exists!")
      return

    # TODO(manyu): Create a player class rather than this shitty list
    self.players[player] = Player(player) 
    #print("Added player: " + player + " to database.")

  def SetPlayerElo(self, player, elo):
    player = checkDup(player)
    if player not in self.players:
      print("WH :OMEGALUL:??? This player does not exist.")
      return

    self.players[player].UpdateElo(elo)
  
  def PrintDatabase(self):
    for player in self.players:
      print("Name: " + str(self.players[player].name) + " ELO:" + str(self.players[player].elo) + 
      " Games played: " + str(self.players[player].games_played))

  def GetPlayer(self, player):
    player = checkDup(player)
    if player in self.players:
      return self.players[player]
    else:
      raise IndexError("Player Not Found")

  def PrintDatabaseSortedByElo(self):
    plist = list(self.players.values())
    plist.sort(key=lambda x: x.elo, reverse=True)
    for p in plist:
      p.PrintPlayer()

  def GenerateGraphs(self):
    sorted_dict = dict(sorted(self.players.items(), key=lambda item: item[1].elo))

    player_names = list(sorted_dict.keys())
    player_elo = list(p.elo for p in sorted_dict.values())
    player_games = list(p.games_played for p in sorted_dict.values())

    fig = go.Figure([go.Bar(x=player_names, y = player_elo, text=player_elo, textposition='auto', marker=dict(color = player_games, colorscale='burg'))])
    fig.show()

