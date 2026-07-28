import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    SCISSORS
'''
hand_signs = [rock, paper, scissors]

user = int(input("ROCK,PAPER,SCISSORS!!!\nEnter 0 for rock, 1 for paper, 2 for scissors: "))
opponent = random.randint(0, 2)
if user >=0 and user <= 2:
    print(f"You chose {hand_signs[user]}")
    print(f"Computer chose {hand_signs[opponent]}")

if user >2 and user <0:
    print("Invalid Number: YOU LOSE!")
elif user == opponent:
    print("It's a tie.")
elif user == 0 and opponent == 2:
    print("You WIN!")
elif opponent == 0 and user == 2:
    print("You LOSE!")
elif user > opponent:
    print("You win!")
elif opponent > user:
    print("You lose!")
