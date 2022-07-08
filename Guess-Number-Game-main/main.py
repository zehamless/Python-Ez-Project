from art import logo, win, lose
import random
import sys

easyTurn = 10
hardTurn = 5

print(logo)
def level():
  lvl_in = input("Choose level: easy/hard?\n").lower()
  
  if lvl_in == "easy":
    return easyTurn
  elif lvl_in == "hard":
    return hardTurn
  else:
    print("Wrong Input")
    sys.exit(0)

def check(guess, number, turn):
  if guess == number:
    print(win)
    return turn+20
  elif number-5 < guess < number+5:
    print("a little bit more\n")
    return turn-1
  elif guess < number:
    print("Need more\n")
    return turn-1
  elif guess > number:
    print("Too Much\n")
    return turn-1


def game():
  number = random.randint(1, 100)
  # print(number)
  turn = level()
  print(f"Your Turn: {turn}")
  
  guess = int(input("Guess the number: "))
  turn = check(guess, number, turn)
  if turn < 20:
    print(f"Your Turn: {turn}")

  gameStat = False
  

  while guess != number:
    guess = int(input("Guess the number: "))
    turn = check(guess, number, turn)

    if guess == number:
      gameStat = True
    elif turn == 0:
      print(lose)
      gameStat = True
    else:
      print(f"Your turn: {turn}")
  
game()

