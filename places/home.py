def tv(variables):
	return ("You try to watch the tv. It's broken... :(", variables)

neighbors = []
actions = []
statement = ""
jumpable = True

def configure(variables):
	global neighbors
	global actions
	global statement
	try:
		variables["home_visited_time"] += 1
	except:
		variables["home_visited_time"] = 0
	neighbors = [('kitchen', 'kitchen'), ('living_room', 'living room'), ('portal_1', 'portal'), ('yard', 'yard')]
	actions = [('Watch tv.', 'tv', tv)]
	statement = 'You visited this room ' + str(variables["home_visited_time"]) + ' times before.\nYou come to your home.\nYou see a kitchen to the north,\na living room to the east,\na wall to the south,\nand a door to the yard to the west.'
	return variables