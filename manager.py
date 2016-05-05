#!/usr/bin/python
import random
import characterDescription
import managerFunction

# All roles available
allRolesList = ["spy", "bishop", "fool", "inquisitor", "judge", "peasant", "peasant", "queen", "king", "witch", "cheat", "widow", "thief", "beggar"]

# Set player numbers
while True:
	try:
		playersNumber = int(raw_input("Number of players (4 - %d)? " %len(allRolesList)))
		if playersNumber < 4 or playersNumber > len(allRolesList):
			print "Please enter a number between 4 to %d." %len(allRolesList)
			continue
	except:
		print "Please enter a valid number."
		continue
	break

playersRoleList = []

# Randomly choose roles from the role list
while playersNumber > 0:
	role = random.choice(allRolesList)
	playersRoleList.append(role)
	allRolesList.remove(role)
	playersNumber -= 1


# Round counter
round = 0
while True:
	raw_input("Press enter for testing round counter")
	round += 1
	# print round

	# print first 4 round
	if round <= 4:
		print "Swap card? [Y/N]"
		action = raw_input()
		if action == "Y":
			# swap card function define in managerFunction.py
			managerFunction.swapCard(playersRoleList[0], playersRoleList[1])
		elif action == "N":
			continue
		else:
			"Please enter a valid option."
	# after 4 round
	else:
		print "Choose an action:\n1.Swap card\n2.Secretly look at the card.\n3.Announce their character.\n"
		action = raw_input()
		if action == "1":
			managerFunction.swapCard(playersRoleList[0], playersRoleList[1])
		elif action == "2":
			managerFunction.glance()
		elif action == "3":
			managerFunction.announce()
		else:
			"Please enter a valid option."
