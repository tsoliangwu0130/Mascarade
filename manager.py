import random
import characterDescription
import function
import player

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
	print "round: ", round

	# get the action feedback from every player (the first argument is still modify)
	getRequest = player.player(playersRoleList[0], round)
	print getRequest
	if getRequest == "Swap":
		print "Who do you want to swap with? (please enter player number)"
		swapPlayer = int(raw_input())
		playersRoleList = function.swapCard(0, swapPlayer, playersRoleList)
	else:
		continue
