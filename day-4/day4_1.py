sumOfWinningMatches = 0

with open("input_day4", "r") as file:

	Lines = file.readlines()

lineNumber = 0
winningTimes = 0

for line in Lines:

    cardNumbers = line.split(": ")
    numbers = cardNumbers[1].split(" | ")
    PlayingNumbers = numbers[0].split(" ")
    WinningNumbers = numbers[1].split(" ")

    matchPoints = 0
    numberOfWinnedMatchs = 0
    
    for playingNumber in PlayingNumbers:
        secondTimeAround = 0
        if (not playingNumber == ""):
            print("Playing number: {} on line {}".format(playingNumber, lineNumber))
            for winningNumberS in WinningNumbers:
                winningNumber = winningNumberS.strip()

                print("Checking Playing number: {} with Winning Number {} on line {}".format(playingNumber, winningNumber, lineNumber))
                if (playingNumber == winningNumber):
                    print("Winning number: {} on line {}".format(playingNumber, lineNumber))
                    numberOfWinnedMatchs += 1
                    secondTimeAround += 1
                    winningTimes += 1
                    if (matchPoints == 0):
                        matchPoints = 1
                    else:
                        if (not secondTimeAround == 0):
                            matchPoints *= 2
                        else:
                            print("Gotcha! number: {} on line {} - {} times around.".format(winningNumber, lineNumber, secondTimeAround))

    print("On card {} - Winned Matchs: {} - Match Points: {} - Total Match Points: {} - Winned times: {}".format(cardNumbers[0], numberOfWinnedMatchs, matchPoints, sumOfWinningMatches, winningTimes))

    lineNumber += 1
    sumOfWinningMatches += matchPoints
    matchPoints = 0

