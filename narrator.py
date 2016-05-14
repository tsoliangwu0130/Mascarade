def ability(role):
	description = [
	"Spy: The spy secretly looks at their card and anotherplyer's card before swapping their card or not.", 
	"Bishop: The bishop takes two gold coins from the richest of the other players. In case of a tie, the bishop shooses from which player the two coins are taken.", 
	"fool", "inquisitor", "judge", "peasant", "peasant", "queen", "king", "witch", "cheat", "widow", "thief", "beggar"]
	if role == "blank":
		print description
	elif role == "spy":
		print description[0]
	elif role == "bishop":
		print description[1]
	elif role == "fool":
		print description[2]
	elif role == "inquisitor":
		print description[3]
	elif role == "judge":
		print description[4]
	elif role == "bishop":
		print description[5]
	elif role == "peasant":
		print description[6]
	elif role == "queen":
		print description[7]
	elif role == "king":
		print description[8]
	elif role == "witch":
		print description[9]
	elif role == "cheat":
		print description[10]
	elif role == "widow":
		print description[11]
	elif role == "thief":
		print description[12]
	elif role == "beggar":
		print description[13]
	else:
		print "No character found."


def rule(rule):
	description = ["a", "b", "c"]
	if rule == "blank":
		print description
	elif rule == "a":
		print description[0]
	elif rule == "b":
		print description[1]
	else:
		print "No character found."


print "please enter a role or ability:"
input = raw_input()
option = input.split()

if option[0] == "ability":
	if len(option) == 1:
		ability("blank")
	else:
		ability(option[1])

elif option[0] == "rule":
	print rule(option[1])

else:
	print "Please enter a valid option."
