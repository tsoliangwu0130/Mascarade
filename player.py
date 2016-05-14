import random

# initial properties
initialCoin        = 6
initialStatus      = "private"
availableRolesList = ["spy", "bishop", "fool", "inquisitor", "judge", 
                      "peasant", "peasant", "queen", "king", "witch", 
                      "cheat", "widow", "thief", "beggar"]

def sendRequest(request):
	print "send", request

def receiveRequest(request):
	print "receive", request

class Player():	
	# each player must to be created by giving an actual role
	def __init__(self, actualRole):
		self.coin          = initialCoin # current holding coins
		self.suspectedRole = random.choice(availableRolesList) # suspected role identity
		self.actualRole    = actualRole # actual role identity
		self.status        = initialStatus # player status (public / private)

	def swap(self):
		sendRequest(1)
		receiveRequest(2)

	def glance(self):
		print "*** Glance: You are the " + self.actualRole + " ! ***"
		self.suspectedRole = self.actualRole

	def declare(self):
		pass

# testing
player = Player("king")
player.swap()
