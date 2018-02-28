def handleCustomer():
	return "You are a customer!"

def handleEmployee():
	return "You are an employee!"

while True:
	user_input = input("Are you a customer? ")
	if user_input == "quit":
		break
	elif user_input == "y" or user_input == "yes":
		print(handleCustomer())
	elif user_input == "n" or user_input == "no":
		print(handleEmployee())

