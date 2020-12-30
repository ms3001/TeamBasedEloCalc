class Player:
  """ A class to represent a single player """
  def __init__(self, name):
    self.name = name
    self.elo = 1000
    self.games_played = 0
    self.games_won = 0
    self.eloList = []

  def __getstate__(self):
    return self.__dict__.copy()

  def __setstate__(self, state):
    self.__dict__.update(state)

  def UpdateElo(self, new_elo):
    # TODO: check input
    if new_elo > self.elo:
      self.games_won += 1

    self.elo = new_elo
    self.games_played += 1

  def PrintPlayer(self):
    print("Name: " + str(self.name) + " ELO: " + str(self.elo) + " Games played: " + str(self.games_played) + " Games won: " + str(self.games_won))


  