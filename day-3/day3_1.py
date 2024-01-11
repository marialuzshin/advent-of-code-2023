sumPartNumbers = []
sumOfAll = 0

def init(last, lastIndex):
	print("Init {}, {}".format(last, lastIndex))

	for i in range(last):
		line = []
		for f in range(lastIndex):
			line.append(0)
		sumPartNumbers.append(line)
		#print(sumPartNumbers)

def addToPartNumbers(line, index, number, last):

	numberOfDigits = len(number) + 2
	print("Adding {} of line {} - index: {}".format(number, line, index))

	for i in range(numberOfDigits):
		if (index - i) > - 1:
			print("to current line {} - index: {}".format(line, index - i))
			sumPartNumbers [line][index - i] += int(number)		
			if (line > 0):
			#if (index - i) > - 1:
				print("to previous line {} - index: {}".format(line - 1, index - i))
				sumPartNumbers [line - 1][index - i] +=	int(number)		
			if (line + 1 < last - 1):
			#if (index - i) > - 1:
				# print("Current - to next line {} - index: {}".format(line + 1, index - i))
				if (len(sumPartNumbers[line]) <  index - i):
					print("to next new line {} - index: {}".format(line - 1, index - i))
					sumPartNumbers [line + 1].insert(index - i, int(number))
				else: 
					print("to next line {} - index: {}".format(line - 1, index - i))
					#print("current line: {}, index: {} --> sumPartNumbers[line + 1]: {}".format(line, index, len(sumPartNumbers)))
					sumPartNumbers[line + 1][index - i] += int(number)		

with open("input_day3", "r") as file:

	Lines = file.readlines()

lineIndex = 0
last = len(Lines)

for line in Lines:
	print("Line: {}".format(line))

	chars = [*line.strip()];

	if (len(sumPartNumbers) == 0):
		init(last, len(chars))

	charIndex = 0
	currenNumber = ""
	
	for char in chars:
		if char.isdigit():
			currenNumber += char 
		elif char == ".":
			if (not currenNumber == ""):
				addToPartNumbers(lineIndex, charIndex, currenNumber, last)
				currenNumber = ""
		else:
			if (not currenNumber == ""):
				#It's a Symbol
				addToPartNumbers(lineIndex, charIndex, currenNumber, last)
				currenNumber = ""

		charIndex += 1
		
	if (not currenNumber == ""):
		addToPartNumbers(lineIndex, charIndex - 1, currenNumber, last)
		currenNumber = ""

	lineIndex += 1

lineIndex = 0
for line in Lines:
	chars = [*line.strip()];

	charIndex = 0
	currenNumber = ""
	print("Line {} -> {} ".format(lineIndex, line))
	for char in chars:
		if not char.isdigit() and not char == ".":
			#It's a Symbol
			partNumberSum = sumPartNumbers[lineIndex][charIndex]
			sumOfAll += partNumberSum
			print("Symbol {} on line {} and position: {} - partNumbers: {} - Sum: {}".format(char, lineIndex, charIndex, partNumberSum, sumOfAll))

		charIndex += 1
	lineIndex += 1



