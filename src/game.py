class Game:
  """ A class to represent a single game"""
  def __init__(self):
    self.team_1 = []
    self.team_2 = []
    self.game_ready = False

  def SetTeam1(self, player_list):
    if self.game_ready:
      print("yo game has already been setup! wyd??")
      return
    
    self.team_1 = player_list
    if len(self.team_2) == 5:
      self.game_ready = True

  def SetTeam2(self, player_list):
    if self.game_ready:
      print("yo game has already been setup! wyd??")
      return

    
    self.team_2 = player_list
    if len(self.team_1) == 5:
      self.game_ready = True

  def GamePrediction(self):
    if not self.game_ready:
      print("Predicting that you will lose, because this game is not ready yet.")

    # output likelihood of team_1/team_2 winning

  def FinishGame(self, winner): 
    if not self.game_ready:
      print("You cannot finish what has not been started - yone probably")
      return

    # calculate new scores

    # return the list of players mapping to new elo

  def PrintGameState(self):
    print("Team 1:")
    print("Team 2:")    

  
