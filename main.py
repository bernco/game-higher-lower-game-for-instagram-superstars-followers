"""This program asks the player to guess which superstar has the highest followers on istagram
    A dicitionary of data about the superstars have been made available in the file game_data.py

    Author: Chisom Umunnakwe
    Mentor: Dr. Angela Yu of Appbrewery
"""

#importing dependencies
import random
from game_data import data
from art import logo, vs
from replit import clear

print(logo)

is_right = True
score = 0

#random accound generation for the second account
account_b = random.choice(data)

#function for score keeping
def score_keeper():
  """returns the score of the player"""
  return score


#to continue asking until user fails
while is_right:

  #assigns already random generated account to account a so that only the second accound switches for comparison
  account_a = account_b
  account_b = random.choice(data)
 
  #to make sure both accounts for comparison aren't same
  if account_a == account_b:
    account_b = random.choice(data)
  
  A=(account_a["name"])
  desc=(account_a["description"])
  country=(account_a["country"])
  followers=(account_a["follower_count"])

  
  B=(account_b["name"])
  desc_b=(account_b["description"])
  country_b=(account_b["country"])
  followers_b=(account_b["follower_count"])


  print(f"Compare A: {A}, a {desc} from {country}")
  print(vs)
  print(f"Against B: {B}, a {desc_b} from {country_b}")


  #asks for users choice
  choice = input("who has more followers? 'A' or 'B': ").lower()
  
  #checks highest followers
  highest = max(followers,followers_b)
  clear()
  print(logo)

  score = score_keeper()
  if choice == 'a':
    if followers ==highest:
      score+=1
      print(f"You are right, you have {score}")
      

    else:
      print(f"You are wrong, your score is {score}")
      
      is_right =False
  elif choice == 'b':
    if followers_b==highest:
      score +=  1
      print(f"You are right, you have {score}")
      
      
    else:
      print(f"You are wrong, your score is {score}")
      is_right =False
  


#function for comparing



