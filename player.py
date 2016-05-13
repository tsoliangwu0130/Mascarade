import random

# initial variables
initialCoin        = 6
initialStatus      = "private"
availableRolesList = ["spy", "bishop", "fool", "inquisitor", "judge", 
                      "peasant", "peasant", "queen", "king", "witch", 
                      "cheat", "widow", "thief", "beggar"]

class Player():	
	def __init__(self, actualRole):
		self.coin          = initialCoin # current holding coins
		self.suspectedRole = random.choice(availableRolesList) # suspected role identity
		self.actualRole    = actualRole # actual role identity
		self.status        = initialStatus # player status (public / private)

	def swap(self):
		pass
	def glance(self):
		pass
	def declare(self):
		pass

# testing
player = Player(random.choice(availableRolesList))
print "play coin:", player.coin
print "play suspectedRole:", player.suspectedRole
print "play actualRole:", player.actualRole
print "play status:", player.status