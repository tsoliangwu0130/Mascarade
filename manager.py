from player import Player
import random
import time

# initial properties
availableRolesList = ['beggar', 'bishop', 'cheat', 'fool', 'inquisitor', 'judge', 'king', 'peasant', 'peasant', 'queen', 'spy', 'thief', 'widow', 'witch']
roundCount = 0 # current round number
courtCoins = 0 # current coins in the court
deck       = availableRolesList # current roles deck
playerList = [] # current players list

playersNum = int(raw_input("Please enter the number of players: "))
userOrder  = random.randint(0, playersNum)
print "Your playing order is", userOrder

for i in xrange(playersNum):
	randomRole = random.choice(deck)
	player     = Player(i, availableRolesList, randomRole)
	playerList.append(player)
	deck.remove(randomRole)

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

# ask response from the player
def askResponse(player):
 	player.glance()

# start the game
while True:
	roundCount += 1
	print "Round", roundCount
	currentOrder  = (roundCount-1) % len(playerList)
	currentPlayer = playerList[currentOrder]

	if currentOrder == userOrder:
		request = raw_input("What do you want to do? ")
	else:
		print "player", currentPlayer.order, "is thinking..."
		time.sleep(random.randint(1, 5))
		playerResponse = askResponse(currentPlayer)
	print "=========="

	if roundCount > 10:
		break 
