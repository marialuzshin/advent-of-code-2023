sumOfWinningMatches = 0
cardInstances = []

winningCardNumbers = []

def findWinning(card, numberOfInstances, winnedCards, roundN):
    cardNumbers = card.split(": ")

    cardNumber = int(cardNumbers[0].split("Card ")[1].strip())
    #print("Card number: {} --- cardInstances: {}".format(cardNumber, cardInstances))
    #cardInstances[cardNumber - 1] += 1
    numberOfInstances += 1

    numbers = cardNumbers[1].split(" | ")
    PlayingNumbers = numbers[0].split(" ")
    WinningNumbers = numbers[1].split(" ")

    winnedNumbers = 0

    if (len(winningCardNumbers) > cardNumber - 1 :
    for playingNumber in PlayingNumbers:
        secondTimeAround = 0
        if (not playingNumber == ""):
            #print("Round {} - Playing number: {} on card {}".format(roundN, playingNumber, cardNumbers[0]))
            for winningNumberS in WinningNumbers:
                winningNumber = winningNumberS.strip()

                #print("Checking Playing number: {} with Winning Number {} on card {}".format(playingNumber, winningNumber, cardNumbers[0]))
                if (playingNumber == winningNumber):
                    winnedNumbers += 1
                    #print("Winning number: {} on card {}".format(playingNumber, cardNumbers[0]))
                    #numberOfWinnedMatchs += 1
                    #secondTimeAround += 1
                    #findWinning(, numberOfInstances)
                    
    for i in range(winnedNumbers):
        winnedCards.append(Lines[cardNumber - 1])

with open("input_day4", "r") as file:

	Lines = file.readlines()

lineNumber = 0

numberOfInstances = 0

Cards = Lines

roundN = 1
while (not len(Cards) == 0):
    print ("Round {}".format(roundN))
    
    print("Cards: {} on round {} ".format(len(Cards), roundN))

    nextWinnedCards = []
    for card in Cards:
        cardInstances.append(0)
        findWinning(card, numberOfInstances, nextWinnedCards, roundN)
    
    Cards = nextWinnedCards
    roundN += 1
    #print("On card {} - Winned Matchs: {} - Match Points: {} - Total Match Points: {}".format(cardNumbers[0], numberOfWinnedMatchs, matchPoints, sumOfWinningMatches))
print(" numberOfInstances: {} ".format(numberOfInstances))
    #lineNumber += 1
    #sumOfWinningMatches += matchPoints
    #matchPoints = 0

