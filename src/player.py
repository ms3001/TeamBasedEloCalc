class Player:
  """ A class to represent a single player """
  def __init__(self, name):
    self.name = name
    self.elo = 1000
    self.games_played = 0

  def UpdateElo(self, new_elo):
    # TODO: check input
    self.elo = new_elo
    self.games_played += 1

  