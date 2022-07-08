from art import logo, vs
from game_data import data
import random
from replit import clear #you can delete this if error, cuz im using replit
import sys

print(logo)

def randAcc():
  """For random account"""
  return random.choice(data)
# print(randAcc())

def display(account):
  """show data in format"""
  nama = account["name"]
  desc = account["description"]
  country = account["country"]
  return f"Name: {nama}, {desc}, from {country}"

# print(display(randAcc()))
def comparator(account1, account2):
  """Compare between acc"""
  follower1 = account1["follower_count"]
  follower2 = account2["follower_count"]
  if follower1 > follower2:
    state = True
    return state
  else :
    state = False
    return state

def choices(choice, state, score):
  """Checking choice"""
  if choice == "A":
    if state == True:
      score +=1
    else:
      score = -1
  elif choice == "B":
    if state == True:
      score += 1
    else:
      score = -1
  else:
    score = -1
  return score

def game():
  state = True
  score = 0
  
  account1 = randAcc()
  print(display(account1))

  
  while score >= 0:
    account2 = randAcc()
    print(vs)
    print(display(account2))
    choice = str(input("Which has more follower? A/B \n")).upper()
    clear() #replit
    state = comparator(account1, account2)
    account1 = account2
    
    score = choices(choice, state, score)
    if score > 0:
      print(f"Your score: {score}")
      print(display(account1))
    else:
      print("You Lose!!")
      sys.exit()
game()

