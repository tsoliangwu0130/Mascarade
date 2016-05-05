#!/usr/bin/python
total = 0

# courthouse function: manage the coin in couthouse
def courtHouse(coin):
	global total
	total += coin
	return total

# swap two card
def swapCard(myCard, otherCard):
	myCard, otherCard = otherCard, myCard
