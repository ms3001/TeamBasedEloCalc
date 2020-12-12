from database import Database
from game import Game

db = Database()

def main():
  print("Welcome to the multiplayer ELO calculator tool!")
  StartDecisionLoop()

def StartDecisionLoop():
  val = input("Enter your action. (press h for help).\n")
  if len(val) != 1 or not val.isalpha():
    print("Bad input! try again. (press h for help).")
    StartDecisionLoop()

  # TODO(ms3001): Maybe we can change these ifs out for a dictionary mapping to functions.
  if val == 'h':
    print("Options:\n" +
    "h: Help (this option).\n" +
    "q: Quit.\n" + 
    "a: Add player.\n" + 
    "g: Get database.\n")
    
    #input("Press enter to continue.\n")
    StartDecisionLoop()

  elif val == 'q':
    print("Thanks for using this tool :)")
    return

  elif val == 'a':
    player = input("Enter new player name:\n")
    AddPlayer(player)

  elif val == 'g':
    print("Current datbase: ")
    db.PrintDatabase()

  else:
    print("Unrecognized option.\n")

  StartDecisionLoop() # keeps user in decision loop till they quit.

    



def ReadFromFile(filename):
  print("Attempting to read from " + filename)
  #TODO(manyu): finish this

def WriteToFile(filename):
  print("Attempting to write to file" + filename)
  #TODO(manyu): finish this

def AddPlayer(player):
  print("Attempting to add " + player + " to database.")
  db.AddNewPlayer(player)
  



if __name__ == "__main__":
  main()
