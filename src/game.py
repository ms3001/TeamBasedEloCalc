from util import GetNewEloScore
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
      return False

    team_1_avg = sum(player.elo for player in self.team_1) / 5.0
    team_2_avg = sum(player.elo for player in self.team_2) / 5.0 #TODO(ms3001): add config file to set team size and other fields

    # calculate new scores
    for player in self.team_1:
      player.UpdateElo(GetNewEloScore(player.elo, team_2_avg, True if winner == 1 else False, player.games_played))
      #print(player.elo)
    for player in self.team_2:
      player.UpdateElo(GetNewEloScore(player.elo, team_1_avg, True if winner == 2 else False, player.games_played))
      #print(player.elo)

    return True

  def PrintGameState(self):
    print("Team 1:")
    print("Team 2:")    

  
