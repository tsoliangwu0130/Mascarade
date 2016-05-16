from player import Player
import random

# initial properties
availableRolesList = ['beggar', 'bishop', 'cheat', 'fool', 'inquisitor', 'judge', 'king', 'peasant', 'peasant', 'queen', 'spy', 'thief', 'widow', 'witch']
roundCount = 0 # current round number
courtCoins = 0 # current coins in the court
deck       = availableRolesList # current roles deck
playerList = [] # current players list

playersNum  = int(raw_input("Please enter the number of players: "))
for i in xrange(playersNum):
	randomRole = random.choice(deck)
	player     = Player(i, availableRolesList, randomRole)
	playerList.append(player)
	deck.remove(randomRole)

def askInfo(player):
	print ">>> player", player.number, "<<<"
	print "Coin:  ", player.coin
	print "Status:", player.status
	if player.status == "public":
		print "Role:  ", player.actualRole
	else:
		print "Role:   unknown"
	print "==================="

for player in playerList:
	askInfo(player)