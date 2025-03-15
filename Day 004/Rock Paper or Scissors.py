# Import the random module for opponent emulation
import random

# User input
playerDecision = int(input("Rock: 1\nPaper: 2\nor Scissor: 3\n >"))

# Exit if invalid user input
if playerDecision >= 4 or playerDecision <= 0 :
    print(playerDecision)
    print("INPUT ERROR\nNOT VALID")
    exit()

# Computer decides what they want to play
cpuDecision = random.randint(1,3)

# print(f"Computer decided: {cpuDecision}") # Debug

# Multi-string ASCII art 
# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handsigns = [rock, paper, scissors]

# Display decisions

decision  = ["Rock","Paper","Scissor"]

print(f"Player chose {decision[(playerDecision - 1)]}\n{handsigns[(playerDecision - 1)]}")
print(f"\n\n\nComputer chose {decision[(cpuDecision - 1)]}\n{handsigns[(cpuDecision - 1)]}")

# Rock defeats Scissor
if playerDecision == 1 and cpuDecision == 3:
    print("You Win!")
# Scissor defeats Paper
elif playerDecision == 3 and cpuDecision == 2:
    print("You Win!")
# Paper defeats Rock
elif playerDecision == 2 and cpuDecision == 1:
    print("You Win!")
# Draw
elif playerDecision == cpuDecision:
    print(f"It is a Draw!!!")
# Winning condition not met, you lose
else:
    print("You Lose!")
