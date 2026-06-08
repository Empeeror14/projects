from game_data import data
import random
import subprocess
score = 0


def display_account_info(account):
	name =account["name"]
	description =account["description"]
	country =account["country"]
	return f"{name}, a {description} from {country}"


def compare(guess, acc_1, acc_2):
	if acc_1 < acc_2:
		if guess == 1:
			return False
		else:
			return True

	else:
		if guess == 1:
			return True
		else:
			return False




account_2 = random.choice(data)
continue_game =True
while continue_game:
	account_1 = account_2
	account_2 = random.choice(data)
	while account_1 == account_2:
		account_2 = random.choice(data)

	print(f"Compare_1: {display_account_info(account_1)}")
	print("VS")
	print(f"Compare_2: {display_account_info(account_2)}")
	guess =int(input("Who has more followers, 1 or 2?: "))

	no_of_followers_1 =account_1["follower_count"]
	no_of_followers_2 =account_2["follower_count"]

	is_correct =compare(guess, no_of_followers_1, no_of_followers_2)

	
	
	if is_correct:
    		
		score +=1
		print(f"You are correct. Your total score is {score}")
	else:
		print(f"You are wrong. Your final score is {score}")
		continue_game = False






