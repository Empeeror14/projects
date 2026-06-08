import random
from number_guess_art import logo
EASY_LIVES =10
HARD_LIVES =5
turns =0

print(logo)
# create a random number
answer = random.randint(1,100)
print(f"ojoro!!, the number is sha {answer}")
# create a funtion to compare the guess with the answer
def compare_result(guessed_number, right_answer,turns):
	"""compare guess against answer and print the number of turns remaining"""
	if guessed_number > right_answer:
		print("Too high!")
		return turns - 1
	elif guessed_number < right_answer:
		print("Too low!")
		return turns - 1
	else:
		print(f"Congratulations!, your guess, {guessed_number} is the correct answer.")

# create a function to set the difficulty
def set_difficulty():
	level =input("Do you want to play at the hard or easy level. Type 'easy' or 'hard': \n")
	if level == "easy":
		return EASY_LIVES
	else:
		return HARD_LIVES
def game():
	turns = set_difficulty()

	# create a condition to rep[eat game if guess is wrong
	guess =0
	while guess!=answer:
		print(f"You have {turns} lives remaining to guess the number!")
		# player should guess the random number
		guess = int(input("Guess the number.: "))
		turns = compare_result(guess, answer, turns)
		if turns == 0:
			print("You have run out of lives!")
			return
		elif guess!= answer:
			print("Make another guess")

game()





