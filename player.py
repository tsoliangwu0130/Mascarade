#!/usr/bin/python
import function

# The function for player's action
def player(currentPlayer, round):
	# The first 4 round
	if round <= 4:
		print "Swap card? [Y/N]"
		action = raw_input()
		if action == "Y":
			return "Swap"
		elif action == "N":
			return "noAction"
		else:
			"Please enter a valid option."
	# after 4 round
	else:
		print "Choose an action:\n1.Swap card\n2.Secretly look at the card.\n3.Announce their character.\n"
		action = raw_input()
		if action == "1":
			return "Swap"
		elif action == "2":
			print currentPlayer
			return "Glance"
		elif action == "3":
			return "announce"
		else:
			"Please enter a valid option."
