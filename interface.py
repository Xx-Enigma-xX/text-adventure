import sys
sys.path.insert(0, 'places')

curRoom = 'home'

variables = {'hunger': 0, 'curRoom': curRoom}

while True:
	curRoomObj = __import__(variables['curRoom'])
	variables = curRoomObj.configure(variables)
	print(curRoomObj.statement, end='\n\n')
	if curRoomObj.jumpable:
		print("You can jump from this place.\n")
	else:
		print("\nYou can not jump from this place.\n")
	while input("Do you want to do something?(D) Or, do you want to go some where?(G) ").lower() == "d":
		print("\nWhat will you do?\nYou can do the following activities:\n")
		for i in curRoomObj.actions:
			print(i[0] + "(" + i[1] + ")")
		print()
		choice = input("Enter your choice: ")
		actionFunc = [i[2] for i in curRoomObj.actions if i[1] == choice][0]
		funcReturn = actionFunc(variables)
		print()
		print(funcReturn[0], end="\n\n")
		variables = funcReturn[1]
	print("\nWhere will you go?\nYou can go to:\n")
	possibleDest = [i[1] + "(" + i[0] + ")" for i in curRoomObj.neighbors if not i[0] == None]
	for i in possibleDest:
		print(i)
	print()
	choice = input("Enter your choice: ")
	if curRoomObj.jumpable:
		print("\nYou perform a time-space jump.\n")
		variables['curRoom'] = choice
	else:
		if choice in [i[0] for i in curRoomObj.neighbors if not i[0] == None]:
			variables['curRoom'] = choice
		else:
			print("\nYou can't go there! You are now going back to your previous room.\n")

	variables['hunger'] -= 3
	if variables['hunger'] > 100:
		print("You die from hunger... :(")
		break