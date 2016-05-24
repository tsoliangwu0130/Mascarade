from player import Player
import random
import time
import signal
import sys

# initial properties
availableRolesList   = ['Beggar', 'Bishop', 'Cheat', 'Fool', 'Inquisitor', 'Judge', 'King', 'Peasant', 'Peasant', 'Queen', 'Spy', 'Thief', 'Widow', 'Witch']  # 14 roles available
availableActionsList = ['Swap', 'Glance', 'Announce']  # three basic actions player can do each round


roundCount = 0  # current round number
courtCoins = 0  # current coins in the court
playerList = []  # current players list

deck             = availableRolesList[:]  # current roles deck
possibleRoleList = availableRolesList[:]  # current possible role list

playersNum = int(raw_input("Please enter the number of players: "))
userOrder  = random.randint(0, playersNum - 1)
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


# interrupter for interrupt timer
def interrupter(signum, frame):
	print "time out!"
	sys.exit()


# time limited input
def timerInput():
	try:
		output = raw_input()
		return output
	# timeout
	except SystemExit:
		return


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
	global courtCoins

	# swap cards
	if action == 'Swap':
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
	elif action == 'Glance':
		player.glance()
		if player.order != userOrder:
			print "*** Glance! ***"
		else:
			print "*** Glance: you are the", player.actualRole, "! ***"

	# announce role's ability
	elif action == 'Announce':
		print "*** Announce! ***"

		# announcing roles
		if player.order == userOrder:
			claimedIdentity = raw_input("Who are you? ")
		else:
			claimedIdentity = random.choice(possibleRoleList)

		print "*** Player", player.order, "announce! >>>", claimedIdentity, "<<<"

		# wait 5 seconds for challenges from other players
		signal.signal(signal.SIGALRM, interrupter)  # set alarm
		signal.alarm(5)

		# if there are other players who's suspectedRole are as same as the announcement, challenge it
		# the manager only accpet the closest play's challenge if there are more than one player challenge
		if player.order == len(playerList) - 1:
			nextPlayerOrder = 0
		else:
			nextPlayerOrder = player.order + 1

		while nextPlayerOrder != player.order:
			if nextPlayerOrder == userOrder:
				print "Do you want to challenge this player (Y/N)?"
				challenge = timerInput()
				if challenge == "Y":
					print ">>> Player", nextPlayerOrder, "Challenge! <<<"
					break
				if nextPlayerOrder == len(playerList) - 1:
					nextPlayerOrder = 0
				else:
					nextPlayerOrder += 1
			else:
				if playerList[nextPlayerOrder].suspectedRole == claimedIdentity:
					print ">>> Player", nextPlayerOrder, "Challenge! <<<"
					break
				else:
					if nextPlayerOrder == len(playerList) - 1:
						nextPlayerOrder = 0
					else:
						nextPlayerOrder += 1

		signal.alarm(0)  # disable alarm while successfully get response
		player.announce(claimedIdentity)

		# role abilityies
		if claimedIdentity == "Beggar":
			pass

		if claimedIdentity == "Bishop":
			maxCoin         = player.coin
			richPlayerCount = 0
			richestPlayers  = []

			# get the max coin
			for tempPlayer in playerList:
				if tempPlayer.coin > maxCoin:
					maxCoin = tempPlayer.coin

			# get the richest player(s)
			for tempPlayer in playerList:
				if tempPlayer.coin >= maxCoin:
					richestPlayers.append(tempPlayer)

			if len(richestPlayers) > 1:
				# print all richest players
				print "There are more than one player are richest: "
				for richPlayer in richestPlayers:
					if richPlayer.order != player.order:
						richPlayerCount += 1
						sys.stdout.write("  " + str(richPlayerCount) + ". Player " + str(richPlayer.order))
						print ""

				if player.order == userOrder:
					richestPlayerOrder = int(raw_input("Which player do you want to take 2 coins from? ")) - 1
					richestPlayer      = richestPlayers[richestPlayerOrder]
				else:
					richestPlayer = random.choice(richestPlayers)
			elif len(richestPlayers) == 1:
				print "You are the richest player!"
				richestPlayer = richestPlayers[0]
			else:
				richestPlayer = richestPlayers[0]

			player.coin        += 2
			richestPlayer.coin -= 2

		if claimedIdentity == "Cheat":
			pass

		if claimedIdentity == "Fool":
			if player.order == userOrder:
				print "Assign the orders of two players to swap their roles (or enter N not to swap):"
				fstTarget = raw_input("Target 1: ")
				sndTarget = raw_input("Target 2: ")
			else:
				# randomly pick two players without repeat
				fstTarget = random.choice(playerList).order
				sndTarget = random.choice(playerList).order
				while fstTarget == sndTarget:
					sndTarget = random.choice(playerList).order

			if fstTarget == "N" or sndTarget == "N":
				print ">>> Not swap anyone! <<<"
				pass
			else:
				fstTarget = int(fstTarget)
				sndTarget = int(sndTarget)
				playerList[fstTarget].actualRole, playerList[sndTarget].actualRole = playerList[sndTarget].actualRole, playerList[fstTarget].actualRole
				print ">>> Swap player", fstTarget, "and player", sndTarget, "<<<"
				# after swapping roles, players should re-guess their actual identities
				playerList[fstTarget].suspectedRole = random.choice(possibleRoleList)
				playerList[sndTarget].suspectedRole = random.choice(possibleRoleList)

			player.coin += 1

		if claimedIdentity == "Inquisitor":
			pass

		if claimedIdentity == "Judge":
			player.coin += courtCoins
			courtCoins  = 0

		if claimedIdentity == "King":
			player.coin += 3

		if claimedIdentity == "Peasant":
			pass

		if claimedIdentity == "Queen":
			player.coin += 2

		if claimedIdentity == "Spy":
			pass

		if claimedIdentity == "Thief":
			stolenCoins = 0
			# find the left player and the right player
			if player.order == 0:
				leftPlayerOrder  = len(playerList) - 1
				rightPlayerOrder = player.order + 1
			elif player.order == len(playerList) - 1:
				leftPlayerOrder  = player.order - 1
				rightPlayerOrder = 0
			else:
				leftPlayerOrder  = player.order - 1
				rightPlayerOrder = player.order + 1

			# if the player doesn't have any coin, get 0 coin
			if playerList[leftPlayerOrder].coin > 0:
				stolenCoins += 1
				playerList[leftPlayerOrder].coin -= 1
				print ">>> Steal 1 coin from player", leftPlayerOrder, "<<<"
			if playerList[rightPlayerOrder].coin > 0:
				stolenCoins += 1
				playerList[rightPlayerOrder].coin -= 1
				print ">>> Steal 1 coin from player", rightPlayerOrder, "<<<"

			player.coin += stolenCoins

		if claimedIdentity == "Widow":
			player.coin = 10

		if claimedIdentity == "Witch":
			moreCoinPlayers = []

			if player.order == userOrder:
				target = int(raw_input("Which player's fortune do you want to swap with? "))
				targetPlayer = playerList[target]
			else:
				# get the list of player who has more coin
				for moreCoinPlayer in playerList:
					if moreCoinPlayer.order != player.order and moreCoinPlayer.coin >= player.coin:
						moreCoinPlayers.append(moreCoinPlayer)
				targetPlayer = random.choice(moreCoinPlayers)

			print "Swap with player", target
			player.coin, targetPlayer.coin = targetPlayer.coin, player.coin
			print ">>> Swap the fortune with player", target, "<<<"


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
	showInfo(currentPlayer)
	print "=========="

	# for testing purpose
	if roundCount > 40:
		break
