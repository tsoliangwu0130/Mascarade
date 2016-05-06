import function

# The function for player's action
def player(currentPlayer, round):
	
	# the first 4 round
	if round <= 4:
		action = raw_input("Swap card? [Y/N]")
		if action == "Y":
			return "Swap"
		elif action == "N":
			return "No Action"
		else:
			"Please enter a valid option."
	
	# after 4 round
	else:
		print "Choose an action:"
		print "1. Swap card"
		print "2. Secretly look at the card."
		print "3. Announce their character."
		
		action = raw_input()
		if action == "1":
			return "Swap"
		elif action == "2":
			function.glance()
			return "Glance"
		elif action == "3":
			return "Announce"
		else:
			"Please enter a valid option."
