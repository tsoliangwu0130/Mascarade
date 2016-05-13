# Mascarade
Mascarade card game in Python version

### Rule References
-------------------
* [Mascarade Rule](http://rprod.com/uploads/file/MASCARADE_RULES_EN.pdf)

### Authors
-----------
* [Tso-Liang Wu](https://github.com/tsoliangwu0130)
* [Tien-Lung Chang](https://github.com/ShannaChang)

### Tasks
---------
* manager.py 
	1. count round, decide which player is able to act
	2. send requests to player, either get players' current coins or ask for reaction
	3. record players public status
	4. manage deck and court
	5. terminate game

* narrator.py
	1. describe the game rules
	2. describe each role's ability
	3. show the help info of this application

* player.py
	1. all player must extend the Player class, which has a action list:
		- swap: swap a card either to another player or to the deck
		- glance: glance the role identity
		- declare: execute the role's ability
	2. suspected role identity (for A.I. purpose)
	3. actual role identity
	4. status: current holding coins, public identity or not, etc.
