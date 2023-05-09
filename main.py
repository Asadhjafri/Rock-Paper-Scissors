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

game_images = [rock, paper, scissors]

user_choice = int(
  input(
    "Lets play! Choose 0 for Rock, 1 for Paper or 2 Scissors to start.\n "))
5

computer_choice = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= len(game_images) or user_choice < 0:
  print("Invalid input. Please choose a number between 0 and", len(game_images) - 1)
elif user_choice == 0 and computer_choice == 1:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose!")
elif computer_choice > user_choice:
  print("You lose!")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It is a draw!")
