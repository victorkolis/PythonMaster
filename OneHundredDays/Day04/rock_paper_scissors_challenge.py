# Rock, Paper, Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

try:
    player_choice = int(input("What do you choose? Rock [0], Paper[1], Scissors[2]\n"))
except:
    print("Error: 404 - Choose a number from 0-2!")

machine_choice = random.randint(0, 2)
rock_paper_scissors_ascii = [rock, paper, scissors]
rps_list = ["R", "P", "S"]

try:
    if player_choice == machine_choice:
        print(rock_paper_scissors_ascii[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors_ascii[machine_choice])
        print("Draw!")
        
    # player wins 01
    elif rps_list[player_choice] == "R" and rps_list[machine_choice] == "S":
        print(rock_paper_scissors_ascii[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors_ascii[machine_choice])
        print("You Win!")

    # player wins 02
    elif rps_list[player_choice] == "S" and rps_list[machine_choice] == "P":
        print(rock_paper_scissors_ascii[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors_ascii[machine_choice])
        print("You Win!")
        
    # player wins 03
    elif rps_list[player_choice] == "P" and rps_list[machine_choice] == "R":
        print(rock_paper_scissors_ascii[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors_ascii[machine_choice])
        print("You Win!")
        
    # machine wins 01
    elif rps_list[machine_choice] == "R" and rps_list[player_choice] == "S":
        print(rock_paper_scissors_ascii[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors_ascii[machine_choice])
        print("You Lose!")

    # machine wins 02
    elif rps_list[machine_choice] == "S" and rps_list[player_choice] == "P":
        print(rock_paper_scissors_ascii[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors_ascii[machine_choice])
        print("You Lose!")
        
    # machine wins 03
    else:
        print(rock_paper_scissors_ascii[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors_ascii[machine_choice])
        print("You Lose!")

except:
    print("That is an invalid request!")