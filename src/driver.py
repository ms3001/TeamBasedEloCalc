import pickle
from league_scraper_v1 import scrapeMatchHistoryUrl
from database import Database
from game import Game

db = Database()
game = Game()

def main():
  print("Welcome to the multiplayer ELO calculator tool!")
  StartDecisionLoop()

def StartDecisionLoop():
  val = input("Enter your action. (press h for help).\n")
  if not val.isalpha():
    print("Bad input! try again. (press h for help).")
    StartDecisionLoop()

  # TODO(ms3001): Maybe we can change these ifs out for a dictionary mapping to functions.
  if val == 'h':
    print("Options:\n" +
    "h: Help (this option).\n" +
    "q: Quit.\n" + 
    "a: Add player.\n" + 
    "g: Get database.\n" +
    "s: Setup game.\n" + 
    "f: Enter who won the game.\n"
    "r: Read player db from file.\n"
    "w: Write player db to file.\n"
    "m: Scrape a matchhistory.na.leagueoflegends.com URL.\n"
    )
    
    #input("Press enter to continue.\n")
    StartDecisionLoop()

  elif val == 'q':
    print("Thanks for using this tool :)")
    exit()

  elif val == 'a':
    player = input("Enter new player name:\n")
    AddPlayer(player)

  elif val == 'g':
    print("Current datbase: ")
    db.PrintDatabase()

  elif val == 's':
    print ("Staring game setup.")
    SetupGame()

  elif val == 'f':
    FinishGame()

  elif val == 'r':
    val = input("Enter filename to read from:\n")
    ReadFromFile(val)

  elif val == 'w':
    val = input("Enter filename to write to:\n")
    WriteToFile(val)

  elif val == 't':
    print("Initializing for testing.")
    TestingSetup()

  elif val == 'm':
    ScrapeGame();


  else:
    print("Unrecognized option.\n")

  StartDecisionLoop() # keeps user in decision loop till they quit.

    



def ReadFromFile(filename):
  print("Attempting to read from: " + filename)
  global db 
  db = pickle.load(open(filename, "rb"))

def WriteToFile(filename):
  print("Attempting to write to file: " + filename)
  pickle.dump(db, open( filename, "wb" ) )

def AddPlayer(player):
  print("Attempting to add " + player + " to database.")
  db.AddNewPlayer(player)
 
def TestingSetup():
  for i in range(10):
    AddPlayer("p"+str(i))

def SetupGame():
  if (len(db.players) < 10):
    print("Not enough players to start a game! Must have at least 10.")
    return
  
  team_1 = []
  team_2 = []
  
  # build a mapping from index to potential players to select
  players_by_index = {}
  i = 0
  for player in db.players.values():
    players_by_index[i] = player
    i += 1

  for _ in range(5):
    print("Players to select from: " + ', '.join(str(key) + ":" + players_by_index[key].name for key in players_by_index.keys()))

    index = int(input("Please enter the player index of the next player for team 1: " + "\n"))
    team_1.append(players_by_index[index])
    players_by_index.pop(index)
    print("Selected players for team 1: " + ', '.join([player.name for player in team_1]))

  for _ in range(5):
    print("Players to select from: " + ', '.join(str(key) + ":" + players_by_index[key].name for key in players_by_index.keys()))

    index = int(input("Please enter the player index of the next player for team 2: " + "\n"))
    team_2.append(players_by_index[index])
    players_by_index.pop(index)
    print("Selected players for team 2: " + ', '.join([player.name for player in team_2]))
  
  print("Team 1: " + ', '.join([player.name for player in team_1]))
  print("Team 2: " + ', '.join([player.name for player in team_2]))
  print("Would you like to restart team selection?") #TODO(ms3001): Implement this.

  game.SetTeam1(team_1)
  game.SetTeam2(team_2)

def FinishGame():
  global game
  print("Team 1: " + ', '.join([player.name for player in game.team_1]))
  print("Team 2: " + ', '.join([player.name for player in game.team_2]))
  winner = int(input("Enter '1' if team 1 won, or '2' if team 2."))
  if game.FinishGame(winner):
    print("Game concluded!")
    game = Game()

def ScrapeGame():
  global game
  matchUrl = input("Input the URL of a match:")
  print("Input the login of a player from that match")
  usernametext = input("Username:")
  passwordtext = input("Password:")
  result = scrapeMatchHistoryUrl(usernametext, passwordtext, matchUrl)

  for player in result[1]:
    db.AddNewPlayer(player)

  team_1 = []
  team_2 = []
  for player in result[1][:5]:
    team_1.append(db.GetPlayer(player))
  for player in result[1][5:]:
    team_2.append(db.GetPlayer(player))

  game.SetTeam1(team_1)
  game.SetTeam2(team_2)

  game.FinishGame(int(result[0]))

  game = Game()

if __name__ == "__main__":
  main()