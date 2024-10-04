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
hands = [rock, paper, scissors]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors\n"))

print("You choose: ")
print(hands[choose])

comp_choice = random.randint(0, len(hands) - 1)
print("Computer choose: ")
print(hands[comp_choice])

if choose == comp_choice:
    print("Draw!")
else: 
    if choose == 0 and comp_choice == 1: print("You Lose")
    if choose == 1 and comp_choice == 0: print("You Win")

    if choose == 0 and comp_choice == 2: print("You Win")
    if choose == 2 and comp_choice == 0: print("You Lose")

    if choose == 1 and comp_choice == 2:print("You Lose")
    if choose == 2 and comp_choice == 1:print("You Win")

