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
	playerActualRole = random.choice(deck)
	player = Player(availableRolesList, playerActualRole)
	playerList.append(player)
	deck.remove(playerActualRole)
