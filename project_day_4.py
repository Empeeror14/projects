import random
logo =print("""
█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
""")
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choices = ["Rock","Paper","Scissors"]





user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissors:\n"))
computer_choice = random.randint(0,2)
print(logo)
print(f"computer choose : {computer_choice}")
if user_choice >= 3:
	print("Invalid number, you lose!")
elif computer_choice == 0 and user_choice == 2:
	print(f" you choose {choices[user_choice]} and computer choose {choices[computer_choice]}")
	print("You lose!")
elif user_choice == 0 and computer_choice == 2:
	print(f" you choose {choices[user_choice]} and computer choose {choices[computer_choice]}")
	print("You win!")
elif user_choice == computer_choice:
	print(f" you choose {choices[user_choice]} and computer choose {choices[computer_choice]}")
	print("It is a draw")
elif user_choice >computer_choice:
	print(f" you choose {choices[user_choice]} and computer choose {choices[computer_choice]}")
	print("You win!")
elif computer_choice > user_choice:
	print(f" you choose {choices[user_choice]} and computer choose {choices[computer_choice]}")
	print("You lose!")
