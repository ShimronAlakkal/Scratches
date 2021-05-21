
def sortLetter(name):
	dataDict = {}
	temp = []
	for i in name:
		dataDict[ord(i)] = i
		temp.append(ord(i))
	return dataDict,temp

def formatLetter(dataDict,tempList):
	name = ''
	tempList.sort()
	for i in tempList:
		name += dataDict[i]
	print(name)


dataDict, tempList = sortLetter(input('Enter your name').upper())

formatLetter(dataDict,tempList)