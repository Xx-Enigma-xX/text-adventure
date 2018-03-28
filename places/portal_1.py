def nothing(variables):
	return ("You do nothing.", variables)

neighbors = []
actions = []
statement = ""
jumpable = False

def configure(variables):
	global neighbors
	global actions
	global statement
	try:
		variables["home_visited_time"] += 1
	except:
		variables["home_visited_time"] = 0
	neighbors = [('portal_1', 'nowhere'),(None, 'wall'),(None, 'wall'),(None, 'wall')]
	actions = [('Do nothing.', 'nothing', nothing)]
	statement = 'You go through the portal and you arrive at a place with nothing.'
	return variables