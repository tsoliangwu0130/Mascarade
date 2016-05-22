import random

# initial properties
initialCoin   = 6
initialStatus = "private"


class Player():
	# each player must to be created by giving an actual role
	def __init__(self, order, availableRolesList, actualRole):
		self.order         = order  # player's order number
		self.coin          = initialCoin  # current holding coins
		self.status        = initialStatus  # player status (public / private)
		self.actualRole    = actualRole  # actual role identity
		self.suspectedRole = random.choice(availableRolesList)  # suspected role identity

	def swap(self, newRole):
		self.actualRole = newRole

	def glance(self):
		self.suspectedRole = self.actualRole

	def announce(self, claimedIdentity):
		print "used", claimedIdentity, "ability"

		if claimedIdentity == "king":
			print "You are the king. Obtain 3 coins from the bank."
			self.coin += 3
		if claimedIdentity == "Queen":
			print "You are the king. Obtain 2 coins from the bank."
			self.coin += 2
