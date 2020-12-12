class Database:
  """ A class to store all players and associated information"""
  def __init__(self):
    self.players = {}

  def AddNewPlayer(self, player):
    if player in self.players:
      print("Nice try NERD this player already exists!")
      return

    # TODO(manyu): Create a player class rather than this shitty list
    self.players[player] = [1000, 0]
    print("Added player: " + player + " to database.")

  def SetPlayerElo(self, player, elo):
    if player not in self.players:
      print("WH :OMEGALUL:??? This player does not exist.")
      return

    self.players[player][0]= elo

  def PrintDatabase(self):
    for player in self.players:
      print(player + ":" + str(self.players[player][0]) + ":" + str(self.players[player][1]))