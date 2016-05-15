def ability(role):
	description = {
	'Beggar':'The beggar has no ability',
	'Bishop':'The bishop takes two gold coins from the richest of the other players. In case of a tie, the bishop shooses from which player the two coins are taken.',
	'Cheat':'If they have 10 gold coins or more, the cheat wins the game.',
	'Fool':'The fool receives a gold coin from the bank and swaps-or not - the cards of two other players, under the table and without looking at them.', 
	'Inquisitor':'The inquisitor points at another player. That player must then announce what they believe to be their character, and then reveal their card. If they are wrong, they must pay four gold coins to the inquisitor. If they arent wrong, the power has no effect.', 
	'Judge':'The judge takes all the coin currently on the courthouse board.',
	'king':'The king receives three gold coins from the bank.', 
	'Peasant':'The peasent receives a gold coin from the bank. But if both peasents are revealed during a given turn, they both receive two gold coins from the bank. From unity lies strngth', 
	'Queen':'The queen receives two gold coins from the bank.', 
	'Spy':'The spy secretly looks at their card and anotherplyer card before swapping their card or not.',  
	'Thief':'The thief takes one gold coin from the player to their left and one gold coin from the player to their right.',
	'Widow':'The widow receives coins from the bank to bring her fortune up to 10 coins in total.', 
	'Witch':'The witch can swap all of her fortune with that of another player of their choice.'}

	if role == "blank":
		print description
	elif role == "beggar":
		print description['Beggar']
	elif role == "bishop":
		print description['Bishop']
	elif role == "cheat":
		print description['Cheat']
	elif role == "fool":
		print description['Fool']
	elif role == "inquisitor":
		print description['Inquisitor']
	elif role == "judge":
		print description['Judge']
	elif role == "king":
		print description['King']
	elif role == "peasant":
		print description['Peasant']
	elif role == "queen":
		print description['Queen']
	elif role == "spy":
		print description['Spy']
	elif role == "thief":
		print description['Thief']
	elif role == "widow":
		print description['Widow']
	elif role == "witch":
		print description['Witch']
	else:
		print "No character found."

def rule(rule):
	category = "Rule Category:\n 1.setup\n 2.gameTurn\n 3.action-swap\n 4.action-glence\n 5.action-announce\n"
	ruleDescription = {
	'setup':'Each player starts with 6 gold coins. The character cards are shuffled, and each player receive one, in front of them. With 4 or 5 players, the remaining cards are placed, face up, in the middle of the table. When all players have taken a good look at the cards, they are all turned over so that they are face down. The character tokens are used to keep track of which character are present in the game. Play the proceeds in a clockwise direction.',
	'gameTurn':'The first four turn are preparation turn. The player can:\n 1. Swap their card.\n 2. Glence their card.\n\nFrom the fifth turn on, the game begins in earnest and each player, on their turn, must perfor, only one action from the following three:\n 1. Swap their card - or not.\n 2. Secretly look at their card.\n 3. announce their character.\n',
	'action-swap':'This action allow player to swap their card or not.',
	'action-glence':'This action allows the player to secretly look at their character card.',
	'action-announce':'This action is the main activity of the game, as if allows players to active the powers of the characters. When a player announce they are a character, the other players, in turn, starting from the one on their left and going clockwise, have the option of calling the active players announcement by claiming to be the same character as well.\n * If no one else claims to be the character, the player applies the power of the character maned without revealing their card. Therefore, it is possible to use the power of any character in the game withour being that character, even without knowing who you are.'}
	if   rule == "blank":
		print ruleDescription
	elif rule == "setup":
		print ruleDescription['setup']
	elif rule == "gameTurn":
		print ruleDescription['gameTurn']
	elif rule == "action-swap":
		print ruleDescription['action-swap']
	elif rule == 'action-glence':
		print ruleDescription['action-glence']
	elif rule == 'action-announce':
		print ruleDescription['action-announce']
	elif rule == "category":
		print category
	else:
		print "No character found."


# test
print "Game Rule :\n ability: for all the ability description.\n ability character: for specific character description.\n rule: for game rule description.\n "
input  = raw_input()
option = input.split()

if option[0] == "ability":
	if len(option) == 1:
		ability("blank")
	else:
		ability(option[1])
elif option[0] == "rule":
	rule("category")
	print "Enter a item: "
	ruleOption = raw_input()
	rule(ruleOption)
else:
	print "Please enter a valid option."
