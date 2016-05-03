import random

# All roles available
allRolesList = ["spy", "bishop", "fool", "inquisitor", "judge", "peasant", "queen", "king", "witch", "cheat", "widow", "thief", "beggar"]

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
	print round
