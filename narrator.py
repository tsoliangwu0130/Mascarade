# Description for every character's ability.
def ability(role):
	roleDescription = {
	'Beggar':'The beggar has no ability',
	'Bishop':'The bishop takes two gold coins from the richest of the other players. In case of a tie, the bishop chooses from which player the two coins are taken.',
	'Cheat':'If they have 10 gold coins or more, the cheat wins the game.',
	'Fool':'The fool receives a gold coin from the bank and swaps-or not - the cards of two other players, under the table and without looking at them.', 
	'Inquisitor':'The inquisitor points at another player. That player must then announce what they believe to be their character, and then reveal their card. If they are wrong, they must pay four gold coins to the inquisitor. If they aren\'t wrong, the power has no effect.', 
	'Judge':'The judge takes all the coin currently on the courthouse board.',
	'king':'The king receives three gold coins from the bank.', 
	'Peasant':'The peasant receives a gold coin from the bank. But if both peasants are revealed during a given turn, they both receive two gold coins from the bank.', 
	'Queen':'The queen receives two gold coins from the bank.', 
	'Spy':'The spy secretly looks at their card and another player\'s card before swapping their card or not.',  
	'Thief':'The thief takes one gold coin from the player to their left and one gold coin from the player to their right.',
	'Widow':'The widow receives coins from the bank to bring her fortune up to 10 coins in total.', 
	'Witch':'The witch can swap all of her fortune with that of another player of their choice.'}

	# An option for list every character's ability.
	if role == "blank": 
		for key,value in roleDescription.items():
			print "["+key+"]" 
			print value
	else:
		try:
			print roleDescription[role]
		except:
			print "No character found."

# Description for game rule
def rule(rule):
	ruleDescription = {
	'1':'Setup: Each player starts with 6 gold coins and one card. Play the proceeds in a clockwise direction.',
	'2':'First four turn: 1. Swap their card. 2. Glance their card.',
	'3':'Fifth turn: 1. Swap card. 2. Glance their card. 3. Announce their character.',
	'4':'Swap: To swap their card or not.',
	'5':'Glance: Secretly look at their character card.',
	'6':'Announce: When a player announce they are a character, the other players, in turn, starting from the one on their left and going clockwise, have the option of calling the active players announcement by claiming to be the same character as well.',
	'7':'Announce successfully: If no one else claims to be the character, the player applies the power of the character without revealing their card.',
	'8':'Multiple Claim: If one or more other player\'s also claim to be that character, all concerned players reveal their cards. If one of the player is indeed the announced character, that player immediately uses the characters power. All the other players who had falsely claimed to be the announced character pay one gold coin to the courthouse.',
	'9':'End of Game: As soon as a player has 13 or more gold coins, the game ends and that player wins. If any player loses their last gold coin, the game ends and the richest player wins. Tied victories are sometimes possible.'}

	if rule == "category":
		print "Rule Category:"
		print "1. Setup"
		print "2. First four Turn"
		print "3. Fifth Turn"
		print "4. Action Swap" 
		print "5. Action Glance" 
		print "6. Announcement" 
		print "7. Announce successfully"
		print "8. Multiple Claim"
		print "9. End of Game"

	else:
		try:
			print ruleDescription[rule]
		except:
			print "No rule found."

# test
print "Game Rule:"
print "ability: for all the ability description."
print "ability character: for specific character description." 
print "rule: for game rule description."
print "->"
input  = raw_input()
option = input.split() # Get the option of ability or rule

# An option of ability
if option[0] == "ability": 
	# An option of all the character's ability.
	if len(option) == 1:  
		ability("blank")
	# An option of specific character's ability.
	else: 
		ability(option[1])
# An option of rule
elif option[0] == "rule": 
	rule("category")
	print "Enter a number: " # Enter a number to get a specific rule description.. 
	ruleOption = raw_input()
	rule(ruleOption)
else:
	print "Please enter a valid option."
