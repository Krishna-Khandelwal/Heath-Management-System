# Heath Management System
# Harry, Rohan, Hammad

# Total 6 files

# write a function that when executed takes as input client name
# write one more function to retrieve exercise or food for any client
from datetime import date

def getdate():
	import datetime
	presentDate = date.today()
	presentTime = datetime.datetime.now()
	currentTime = str(presentDate) + " / " + presentTime.strftime("%H:%M:%S")
	return currentTime


def clientName(name):
	activity(name)


def activity(name):
	actList = []
	count = 10
	choice = input("What do you want to record? (Exercise/Food) Press(E/F): ")
	if choice == "E" or choice == "e":
		f = open(f"{name}-Exercise.txt", "a")
		for i in range(count):
			record = input("Which Exercises did you do?\n")
			actList.insert(i, record)
			count = i + 1

			if actList[i] == "":
				actList.pop()
				break

		f.write(f"{[getdate()]}" + " - " f"{actList}" + "\n")
		f.close()
	else:
		f = open(f"{name}-Food.txt", "a")
		for i in range(count):
			record = input("What did you eat?\n")
			actList.insert(i, record)
			count = i + 1

			if actList[i] == "":
				actList.pop()
				break

		f.write(f"{[getdate()]}" + " - " f"{actList}" + "\n")
		f.close()



name = input("Enter your name: ")
clientName(name)