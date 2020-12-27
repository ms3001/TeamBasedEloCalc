import pickle
import itertools
import sys

from league_scraper_v1 import scrapeMatchHistoryUrl
from league_scraper_v1 import scrapeMatchHistoryUrlList
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
    "ml: Scrape a list of games from a textfile.\n"
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
    print("Current database: ")
    db.PrintDatabaseSortedByElo()

  elif val == 's':
    print ("Starting game setup.")
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
    ScrapeGame()

  elif val == 'ml':
    ScrapeGameList()


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
  
  pList = []
  team_1 = []
  team_2 = []
  
  # build a mapping from index to potential players to select
  players_by_index = {}
  i = 0
  for player in db.players.values():
    players_by_index[i] = player
    i += 1

  totalElo = 0
  for _ in range(10):
    print("Players to select from: " + ', '.join(str(key) + ":" + players_by_index[key].name for key in players_by_index.keys()))

    index = int(input("Please enter the player index of the next player: " + "\n"))
    pList.append(players_by_index[index])
    totalElo += players_by_index[index].elo
    players_by_index.pop(index)

  minEloDiff = sys.maxsize
  for i in itertools.combinations(pList, 5):
    team1Elo = i[0].elo + i[1].elo + i[2].elo + i[3].elo + i[4].elo
    if (abs(team1Elo*2 - totalElo) < minEloDiff):
      minEloDiff = abs(team1Elo*2 - totalElo)
      minEloTeam = i

  team1Elo = 0
  team2Elo = 0
  for player in minEloTeam:
    team_1.append(player)
    pList.remove(player)
    team1Elo += player.elo

  for player in pList:
    team_2.append(player)
    team2Elo += player.elo

  print("Team 1: " + ', '.join([player.name for player in team_1]))
  print("Team 1 Total Elo: " + str(team1Elo))
  print("Team 2: " + ', '.join([player.name for player in team_2]))
  print("Team 2 Total Elo: " + str(team2Elo))

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
  matchUrl = input("Input the URL of a match:")
  print("Input the login of a player from that match")
  usernametext = input("Username:")
  passwordtext = input("Password:")
  result = scrapeMatchHistoryUrl(usernametext, passwordtext, matchUrl)

  for player in result[1]:
    db.AddNewPlayer(player)

  SimulateGame(result)

def ScrapeGameList():
  print("Input the login of a player from these matches")
  usernametext = input("Username:")
  passwordtext = input("Password:")

  f = open("data/inputUrls.txt", "r")
  urlList = []
  for url in f:
    urlList.append(url)
  f.close()
  print(urlList)

  matchListData = scrapeMatchHistoryUrlList(usernametext, passwordtext, urlList)

  for match in matchListData:
    for player in match[1]:
      db.AddNewPlayer(player)
    SimulateGame(match)

def SimulateGame(match):
  global game

  team_1 = []
  team_2 = []
  for player in match[1][:5]:
    team_1.append(db.GetPlayer(player))
  for player in match[1][5:]:
    team_2.append(db.GetPlayer(player))
  game.SetTeam1(team_1)
  game.SetTeam2(team_2)

  game.FinishGame(int(match[0]))

  game = Game()

if __name__ == "__main__":
  main()