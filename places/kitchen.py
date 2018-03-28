def nothing(variables):
	return ("You do nothing.", variables)

neighbors = []
actions = []
statement = ""

def configure(variables):
	global neighbors
	global actions
	global statement
	neighbors = [(None, 'wall'), (None, 'wall'), (None, 'wall'), ('home', 'home')]
	actions = [('Do nothing and become a couchpotato', 'nothing', nothing)]
	statement = 'There is nothing in this room.\nYou can go south to go back to your home.'
	return variables