import re

class Game:
	def __init__(self, number, originalValue):
		self.number = number
		self.originalValue = originalValue

red = 12
green = 13
blue = 14

sumPower = 0

with open("input_day2", "r") as file:

	Lines = file.readlines()

for line in Lines:
	
	game = line.strip().split(": ")
	gameNumber = game[0].split("Game ")[1]
	Sets = re.split("; ", game[1])

	redMin = 1
	greenMin = 1
	blueMin = 1

	gamePower = 0
	for colorSet in Sets:
		Colors = colorSet.split(", ")

		validSet = True

		

		for color in Colors:
			colorValue = color.split(" ")
			colorNumber = int(colorValue[0])

			if colorValue[1] == "red" and colorNumber > redMin:
				redMin = colorNumber
				print("Red Min --> - [{}] - {} ----> {}".format(gameNumber, redMin, Colors))
			if colorValue[1] == "green" and colorNumber > greenMin:
				greenMin = colorNumber
				print("Green Min --> - [{}] - {} ----> {}".format(gameNumber, greenMin, Colors))
			if colorValue[1] == "blue" and colorNumber > blueMin:
				blueMin = colorNumber
				print("Blue Min --> - [{}] - {} ----> {}".format(gameNumber, blueMin, Colors))

		gamePower = redMin * greenMin * blueMin

	
	sumPower += gamePower
	print("{}: <- {} <- [r{} g{} b{}]".format(sumPower, gamePower, redMin, greenMin, blueMin))

	

print("----> {}".format(sumPower))