import random
import os
from typing import List
from game_data import data
from art import logo
from art import vs


list = data
"""def start():
  #picking out the first two celebrities
  compare_a=random.choice(list)
  list.remove(compare_a)
  compare_b=random.choice(list)
  list.remove(compare_b)
  print(compare_a, compare_b)
  return compare_a, compare_b"""


def pick(celebrities):
  """picks a random celebrity (and removes it from the list)."""
  compare_a = random.choice(list)
  #list.remove(compare_a)
  return compare_a


def introduction(dict_1, dict_2):
  """prints out the two celebrities' name, description and country."""
  print(
      f"Compare A: {dict_1['name']}, a {dict_1['description']}, from {dict_1['country']}"
  )
  print(vs)
  print(
      f"Against B: {dict_2['name']}, a {dict_2['description']}, from {dict_2['country']}"
  )


def user_input():
  """takes input from user"""
  user_choice = (input("Who has more followers? Type 'A' or 'B':").lower())
  return user_choice

def compare(celebrity_1, celebrity_2, user_choice):
  """compares the two followings and determines if the user's choice was right."""
  follower1 = celebrity_1["follower_count"]
  follower2 = celebrity_2["follower_count"]
  if (follower1>follower2 and user_choice=='a') or (follower1<follower2 and user_choice=='b'):
    user_right=True
  else:
    user_right=False
  return user_right

def play_again():
  again = input("Do you want to play again? Type 'y' or 'n':")
  if again.lower() == 'y':
    game_should_continue=True
  else:
    game_should_continue=False
  return game_should_continue


#start
def game():

  print(logo)
  count = 0
  celebrity1 = pick(list)
  celebrity2 = pick(list)
  game_should_continue = True
  
  while game_should_continue:
    
    celebrity1=celebrity2
    celebrity2=pick(list)
    while celebrity1==celebrity2:
      celebrity2=pick(list)
      
    introduction(celebrity1, celebrity2)
    user_is_right=compare(celebrity1, celebrity2, user_input())

    os.system("clear")
    print(logo)
    
    if user_is_right:
      count += 1
      print(f"You're right! Current score: {count}.")
    elif not user_is_right:
      print(f"Sorry, that's wrong. Final score: {count}.")
      count = 0
      game_should_continue = play_again()
      
  
game()