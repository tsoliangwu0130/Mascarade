import random
import narrator

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
		print ">>> Used", claimedIdentity, "ability <<<"
		print narrator.ability(claimedIdentity)

		if claimedIdentity == "Beggar":
			pass

		if claimedIdentity == "Bishop":
			pass

		if claimedIdentity == "Cheat":
			pass

		if claimedIdentity == "Fool":
			pass

		if claimedIdentity == "Inquisitor":
			pass

		if claimedIdentity == "Judge":
			pass

		if claimedIdentity == "King":
			self.coin += 3

		if claimedIdentity == "Peasant":
			self.coin += 1

		if claimedIdentity == "Queen":
			self.coin += 2

		if claimedIdentity == "Spy":
			pass

		if claimedIdentity == "Thief":
			pass

		if claimedIdentity == "Widow":
			self.coin = 10

		if claimedIdentity == "Witch":
			pass
