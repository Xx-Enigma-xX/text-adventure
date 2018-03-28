def nothing(variables):
	return ("You do nothing.", variables)

def eat(variables):
	variables['hunger'] -= 10
	if variables['hunger'] < 0:
		variables['hunger'] = 0
	return ('You eat.', variables)

neighbors = []
actions = []
statement = ""
jumpable = False

def configure(variables):
	global neighbors
	global actions
	global statement
	neighbors = [(None, 'wall'), (None, 'wall'), (None, 'wall'), ('home', 'home')]
	actions = [('Do nothing and become a couchpotato', 'nothing', nothing), ('Eat', 'eat', eat)]
	statement = 'There is nothing in this room.\nYou can go south to go back to your home.'
	return variables