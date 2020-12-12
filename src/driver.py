from database import Database
from game import Game

def main():
  print("heh")
  db = Database()
  db.AddNewPlayer("manyu")
  db.PrintDatabase()

def StartDecisionLoop():
  print("Enter your action. (press h for help).")
  #TODO(manyu): finish this

def ReadFromFile(filename):
  print("Attempting to read from " + filename)

def WriteToFile(filename):
  print("Attempting to write to file" + filename)



if __name__ == "__main__":
  main()
