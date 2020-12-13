from player import Player

class Database:
  """ A class to store all players and associated information"""
  def __init__(self):
    self.players = {}

  def AddNewPlayer(self, player):
    if player in self.players:
      print("Nice try NERD this player already exists!")
      return

    # TODO(manyu): Create a player class rather than this shitty list
    self.players[player] = Player(player) 
    print("Added player: " + player + " to database.")

  def SetPlayerElo(self, player, elo):
    if player not in self.players:
      print("WH :OMEGALUL:??? This player does not exist.")
      return

    self.players[player].UpdateElo(elo)

  def PrintDatabase(self):
    for player in self.players:
      print("Name: " + str(self.players[player].name) + " ELO:" + str(self.players[player].elo) + 
      " Games played: " + str(self.players[player].games_played))