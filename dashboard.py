import random

# All roles available
allRolesList = ["spy", "bishop", "fool", "inquisitor", "judge", "peasant", "queen", "king", "witch", "cheat", "widow", "thief", "beggar"]

while True:
	try:
		playersNumber = int(raw_input("Number of players? (4-13) "))
		if playersNumber < 4 or playersNumber > 13:
			print "Please enter a number between 4 to 13."
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

