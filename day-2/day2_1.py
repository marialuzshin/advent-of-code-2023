import re

class Game:
	def __init__(self, number, originalValue):
		self.number = number
		self.originalValue = originalValue

red = 12
green = 13
blue = 14

sumIds = 0

with open("input_day2", "r") as file:

	Lines = file.readlines()

ValidGames = []

for line in Lines:
	
	game = line.strip().split(": ")
	gameNumber = game[0].split("Game ")[1]
	Sets = re.split("; ", game[1])

	validGame = True

	for colorSet in Sets:
		Colors = colorSet.split(", ")

		validSet = True

		for color in Colors:
			colorValue = color.split(" ")
			if colorValue[1] == "red" and int(colorValue[0]) > red:
				validSet = False
				print("Gotcha--> red 12 - [{}] {}".format(gameNumber, Colors))
			if colorValue[1] == "green" and int(colorValue[0]) > green:
				validSet = False
				print("Gotcha--> green 13 - [{}] {}".format(gameNumber, Colors))
			if colorValue[1] == "blue" and int(colorValue[0]) > blue:
				validSet = False
				print("Gotcha--> blue 14 - [{}] {}".format(gameNumber, Colors))

		if not validSet:
			validGame = False

	if validGame:
		#Game(gameNumber, line)
		ValidGames.append(gameNumber)	
		sumIds += int(gameNumber)
		print("{}: <- {}".format(sumIds, gameNumber))

	

print("{}: ---- {}".format(sumIds, ValidGames))