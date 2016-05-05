#!/usr/bin/python
total = 0

# courthouse function: manage the coin in couthouse
def courtHouse(coin):
	global total
	total += coin
	return total

# swap two card
def swapCard(myCard, otherCard, playersRoleList):
	playersRoleList[myCard], playersRoleList[otherCard] = playersRoleList[otherCard], playersRoleList[myCard]
	return playersRoleList

def glance():
	print "glance"

def announce():
	print "announce"