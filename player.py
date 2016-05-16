import random

# initial properties
initialCoin   = 6
initialStatus = "private"

class Player():	
	# each player must to be created by giving an actual role
	def __init__(self, order, availableRolesList, actualRole):
		self.order         = order # player's order number
		self.coin          = initialCoin # current holding coins
		self.status        = initialStatus # player status (public / private)
		self.actualRole    = actualRole # actual role identity
		self.suspectedRole = random.choice(availableRolesList) # suspected role identity

	def swap(self, newRole):
		print "*** Swap! ***"
		self.actualRole = newRole

	def glance(self):
		print "*** Glance: You are the " + self.actualRole + " ! ***"
		self.suspectedRole = self.actualRole

	def announce(self):
		print "*** Announce! ***"
