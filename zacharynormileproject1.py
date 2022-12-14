# -*- coding: utf-8 -*-
"""ZacharyNormileProject1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16glmRgKI6m0DtvYA1RUhW8w3qqKZT2n6
"""

from IPython.utils.path import random #imports for random and color coding the text. Spices the end result up and allows for computer to play random choices
from termcolor import colored, cprint

print("The Rules of Rock-Paper-Scissors:\n"
      + "Rock vs Paper -> Paper wins\n" + 
      "Rock vs Scissors -> Rock wins\n" + 
      "Paper vs Scissors -> Scissors wins\n")
user = input("What is your name? ") #Asks for the users name for use in the game to make things friendlier
wants_to_play = True #Check for continuing the loop or stopping it to close the game
#Below, each player can choose what to use for the game.
while wants_to_play == True: 
  print("Enter your choice \n 1. Rock\n 2. Paper\n 3. Scissors\n") 
  userchoice = int(input(user + ": ")) #Allows user to enter their choice, referrs to them by name
  if userchoice not in range(1,4): #Makes sure user input is a valid option within the choice range
    print("Invalid choice!") 
    continue
  if userchoice == 1:
    cprint(user + " chose rock", 'red') #1 = rock, tells the user so. Color coded for who is using the command where red = user and blue = computer
  if userchoice == 2:
    cprint(user + " chose paper", 'red')
  if userchoice == 3:
    cprint(user + " chose scissors", 'red')
  compchoice = random.randint(1,3) #Computer chooses their choice for the game randomly
  print("Computer:", compchoice)
  if compchoice == 1:
    cprint("Computer chose rock", 'blue') #Computer's choice is listed
  if compchoice == 2:
    cprint("Computer chose paper", 'blue')
  if compchoice == 3:
    cprint("Computer chose scissors", 'blue')
#Below, the results are outlined based on what was chosen
  if compchoice == userchoice: #Tie option if same choice is picked for both players
    cprint("\nTie game!", 'green', attrs=['bold'])
  if compchoice == 1 and userchoice == 2:
    cprint("\nPaper covers rock: " + user + " wins!", 'red', attrs=['bold']) #If user wins, text is bold and red
  if compchoice == 1 and userchoice == 3:
    cprint("\nRock crushes scissors: Computer wins!", 'blue', attrs=['bold']) #If computer wins, text is bold and blue
  if compchoice == 2 and userchoice == 1:
    cprint("\nPaper covers rock: Computer wins!", 'blue', attrs=['bold']) #Flavor text to add a fun element
  if compchoice == 2 and userchoice == 3:
    cprint("\nScissors cuts paper: " + user + " wins!", 'red', attrs=['bold']) #User's name is used when user wins
  if compchoice == 3 and userchoice == 1:
    cprint("\nRock crushes scissors: " + user + " wins!", 'red', attrs=['bold'])
  if compchoice == 3 and userchoice == 2:
    cprint("\nScissors cuts papser: 'Computer wins!", 'blue', attrs=['bold'])
#After the game is complete, we ask the player whether they want to play or not.
  while wants_to_play == True: #creates a nested loop for this question and its answers
    print("\nDo you want to play again? (Y/N)") 
    response = input().lower() 
    if response == 'y': #If 'y', continues the game. Space added for clear viewing
      print("\n")
      break #breaks out of the nested loop and goes back to the original loop
    if response == 'n':  #If 'n', closes the game. Turns 'wants_to_play' check to False, closing the game.
      print("\nThanks for playing! \U0001f600") #Emoji added for fun
      wants_to_play = False #Ends the game and breaks out of both loops
    else: #If not y or n, asks the question again
      print("\nInvalid response")
      continue