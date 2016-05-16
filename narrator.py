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
	'Peasant':'The peasent receives a gold coin from the bank. But if both peasents are revealed during a given turn, they both receive two gold coins from the bank. From unity lies strngth', 
	'Queen':'The queen receives two gold coins from the bank.', 
	'Spy':'The spy secretly looks at their card and another player\'s card before swapping their card or not.',  
	'Thief':'The thief takes one gold coin from the player to their left and one gold coin from the player to their right.',
	'Widow':'The widow receives coins from the bank to bring her fortune up to 10 coins in total.', 
	'Witch':'The witch can swap all of her fortune with that of another player of their choice.'}

	if role == "blank": # An option for list every character's ability.
		for key,value in roleDescription.items():
			print "["+key+"]" 
			print value
	elif role == "beggar":
		print roleDescription['Beggar']
	elif role == "bishop":
		print roleDescription['Bishop']
	elif role == "cheat":
		print roleDescription['Cheat']
	elif role == "fool":
		print roleDescription['Fool']
	elif role == "inquisitor":
		print roleDescription['Inquisitor']
	elif role == "judge":
		print roleDescription['Judge']
	elif role == "king":
		print roleDescription['King']
	elif role == "peasant":
		print roleDescription['Peasant']
	elif role == "queen":
		print roleDescription['Queen']
	elif role == "spy":
		print roleDescription['Spy']
	elif role == "thief":
		print roleDescription['Thief']
	elif role == "widow":
		print roleDescription['Widow']
	elif role == "witch":
		print roleDescription['Witch']
	else:
		print "No character found."

# Description for game rule
def rule(rule):
	category = "Rule Category:\n 1.Setup\n 2.Game Turn\n 3.Action Swap\n 4.Action Glence\n 5.Action Announcment\n 6.End of Game"
	ruleDescription = {
	'setup':'Each player starts with 6 gold coins. The character cards are shuffled, and each player receive one, in front of them. With 4 or 5 players, the remaining cards are placed, face up, in the middle of the table. When all players have taken a good look at the cards, they are all turned over so that they are face down. The character tokens are used to keep track of which character are present in the game. Play the proceeds in a clockwise direction.',
	'gameTurn':'The first four turn are preparation turn. The player can:\n 1. Swap their card.\n 2. Glence their card.\n\nFrom the fifth turn on, the game begins in earnest and each player, on their turn, must perform, only one action from the following three:\n 1. Swap their card - or not.\n 2. Secretly look at their card.\n 3. Announce their character.\n',
	'action-swap':'This action allow player to swap their card or not.',
	'action-glance':'This action allows the player to secretly look at their character card.',
	'action-announcment':'This action is the main activity of the game, as if allows players to active the powers of the characters. When a player announce they are a character, the other players, in turn, starting from the one on their left and going clockwise, have the option of calling the active players announcement by claiming to be the same character as well.\n\n * If no one else claims to be the character, the player applies the power of the character without revealing their card. Therefore, it is possible to use the power of any character in the game without being that character, even without knowing who you are.\n\n * If one or more other player\'s also claim to be that character, all concerned players(the one who made the annoucement as well as any other claimants) reveal their cards.\n\n * If one of the player is indeed the anounced character, that player immediately uses the characters power(which can happen outside of their turn).\n\nThen, all the other players who had falsely claimed to be the announced character pay a fine of one gold coin to the courthouse. Finally, all players turn over their cards so that they are again facedown.',
	'endOfGame':'As soon as a player has 13 or more gold coins, the game ends and that player wins. If any player loses their last gold coin, the game ends and the richest player wins. Tied victories are sometimes possible.'}

	if   rule == "category":
		print category
	elif rule == "1":
		print ruleDescription['setup']
	elif rule == "2":
		print ruleDescription['gameTurn']
	elif rule == "3":
		print ruleDescription['action-swap']
	elif rule == '4':
		print ruleDescription['action-glance']
	elif rule == '5':
		print ruleDescription['action-announcment']
	elif rule == '6':
		print ruleDescription['endOfGame']
	else:
		print "No character found."

# test
print "Game Rule :\n ability: for all the ability description.\n ability character: for specific character description.\n rule: for game rule description."
print "->"
input  = raw_input()
option = input.split() # Get the option of ability or rule

if option[0] == "ability": # An option of ability
	if len(option) == 1: # An option of all the character's ability. 
		ability("blank")
	else: # An option of specific character's ability.
		ability(option[1])
elif option[0] == "rule": # An option of rule
	rule("category")
	print "Enter a number: " # Enter a number to get a specific rule description.. 
	ruleOption = raw_input()
	rule(ruleOption)
else:
	print "Please enter a valid option."
