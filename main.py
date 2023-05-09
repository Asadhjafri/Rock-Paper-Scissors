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

#Write your code below this line 👇

user_choice = int(input(
  "Lets play! Choose 0 for Rock, 1 for Paper or 2 Scissors to start.\n "))

computer_choice = random.randint(0, 2)

print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 1:
  print("You win!")
elif computer_choice > user_choice:
  print("You lose!")
else:
  print("You typed an invalid number, you lose!")