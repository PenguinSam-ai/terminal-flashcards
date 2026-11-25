question = "What is anything that occupies space and has mass?"
answer = "matter"
guess = input(question + "\n>")
if guess.lower() == answer:
	print("Correct!")
else:
	print("Wrong! The answer was " + answer)