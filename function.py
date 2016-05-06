# courthouse function: manage the coin in couthouse
def courtHouse(coin):
	global courtTotalCoins
	courtTotalCoins += coin
	return courtTotalCoins

# swap two card
def swapCard(myCard, otherCard, playersRoleList):
	playersRoleList[myCard], playersRoleList[otherCard] = playersRoleList[otherCard], playersRoleList[myCard]
	return playersRoleList

def glance():
	print "glance"

def announce():
	print "announce"