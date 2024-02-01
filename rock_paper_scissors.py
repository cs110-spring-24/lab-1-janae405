import random
opponent= random.randint(1,3)
user= input("Enter rock, paper, or scissors: ")
if user== "rock":
	if opponent==1: 
		print("It's a tie!")
	elif opponent==2:
		print("You're a loser!")
	else:
		print("You're victorious!")

if user== "paper":
	if opponent==1:
		print("You're a winner!")
	elif opponent==2:
		print("It's a tie.")
	else:
		print("You suck.")
if user== "scissors":
	if opponent==1: 
		print("You're pathetic.")
	elif opponent==2:
		print("Yay! You're a winner!")
	else:
		print("Ugh. It's a tie.")