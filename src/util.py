def GetNewEloScore(self_elo, enemy_elo, win, games_played, k_factor = 60, min_factor = 15):
  """
  Return a players elo after winning/losing against a certain enemy.
  self_elo -- int > 0
  enemy_elo -- int > 0
  win -- True or False
  games_played -- int > 0
  k_factor -- int > 0
  min_factor -- k_factor >= int > 0 
  """

  mult_factor = 2 * max(k_factor - 3 * games_played, min_factor)
  actual_score = 1 if win else 0
  expected_score = 1 / (1 + pow(10, (enemy_elo - self_elo) / 400))
  return round(self_elo + mult_factor * (actual_score - expected_score))

print(GetNewEloScore(1000, 1000, False, 20, 60, 15))