from player import Player
import random
import time

# initial properties
availableRolesList   = ['beggar', 'bishop', 'cheat', 'fool', 'inquisitor', 'judge', 'king', 'peasant', 'peasant', 'queen', 'spy', 'thief', 'widow', 'witch']  # 14 roles available
availableActionsList = ['swap', 'glance', 'announce']  # three basic actions player can do each round

roundCount   = 0  # current round number
courtCoins   = 0  # current coins in the court
playerList   = []  # current players list

deck             = availableRolesList[:]  # current roles deck
possibleRoleList = availableRolesList[:]  # current possible role list

playersNum = int(raw_input("Please enter the number of players: "))
userOrder  = random.randint(0, playersNum)
print "Your playing order is", userOrder

for i in xrange(playersNum):
	randomRole = random.choice(deck)
	player     = Player(i, availableRolesList, randomRole)
	playerList.append(player)
	deck.remove(randomRole)

# target list, including all player and the deck
targetList = playerList[:]
targetList.append("deck")

playerStatusList = ["private"] * len(playerList)  # current players status


# show the player information
def showInfo(player):
	print ">>> player", player.order, "<<<"
	print "Coin:  ", player.coin
	print "Status:", player.status
	if player.status == "public":
		print "Role:  ", player.actualRole
	else:
		print "Role:   unknown"
	print "==================="


# ask response from player
def askResponse(player, action):
	# swap cards
	if action == 'swap':
		oldRole = player.actualRole

		if player.order != userOrder:
			targetPlayer = random.choice(targetList)
			if targetPlayer == 'deck':
				target = targetPlayer
			else:
				target = targetPlayer.order
		else:
			target = raw_input('Who do you want to swap with (enter "deck" / player order number)? ')

		# swap from deck
		if target == 'deck':
			print "*** Swap from the deck! ***"
			newRole = random.choice(deck)
			deck.remove(newRole)
			player.swap(newRole)
			player.suspectedRole = random.choice(possibleRoleList)
			deck.append(oldRole)

		# swap from another player
		else:
			print "*** Swap with player", target, "! ***"
			newRole = playerList[int(target)].actualRole
			playerList[int(target)].swap(oldRole)
			playerList[int(target)].suspectedRole = random.choice(possibleRoleList)
			player.swap(newRole)
			player.suspectedRole = random.choice(possibleRoleList)

	# glance card
	elif action == 'glance':
		player.glance()
		if player.order != userOrder:
			print "*** Glance! ***"
		else:
			print "*** Glance: you are the", player.actualRole, "! ***"

	# announce role's ability
	elif action == 'announce':
		print "*** Announce! ***"

		if player.order == userOrder:
			claimedIdentity = raw_input("Who are you? ")
		else:
			claimedIdentity = random.choice(possibleRoleList)

		print "*** Player", player.order, "announce! >>>", claimedIdentity, "<<<"

		player.announce(claimedIdentity)


# start the game
while True:
	roundCount += 1
	print "Round", roundCount
	currentOrder  = (roundCount - 1) % len(playerList)
	currentPlayer = playerList[currentOrder]

	if currentOrder == userOrder:
		action         = raw_input("What do you want to do? ")
		playerResponse = askResponse(currentPlayer, action)
	else:
		print "player", currentPlayer.order, "is thinking..."
		time.sleep(random.randint(1, 3))
		action         = random.choice(availableActionsList)
		playerResponse = askResponse(currentPlayer, action)
	print "=========="

	# for testing purpose
	if roundCount > 10:
		break
