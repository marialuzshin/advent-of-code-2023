digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

def isLetterDigit(chars, char, i):
    if char == "o":
        if len(chars) - i > 2 and chars[ i + 1 ] == "n" and chars[ i + 2 ] == "e":
            return 1
    elif char == "t": 
        if len(chars) - i > 2 and chars[ i + 1 ] == "w" and chars[ i + 2 ] == "o": 
            return 2
        elif len(chars) - i > 4 and chars[ i + 1 ] == "h" and chars[ i + 2 ] == "r" and chars[ i + 3 ] == "e" and chars[ i + 4 ] == "e":
            return 3
    elif char == "f":
        if len(chars) - i > 3: 
            if chars[ i + 1 ] == "o" and chars[ i + 2 ] == "u" and chars[ i + 3 ] == "r": 
                return 4
            elif chars[ i + 1 ] == "i" and chars[ i + 2 ] == "v" and chars[ i + 3 ] == "e": 
                return 5
    elif char == "s":
        if (len(chars) - i) > 2 and chars[ i + 1 ] == "i" and chars[ i + 2 ] == "x": 
            return 6
        elif (len(chars) - i) > 4 and chars[ i + 1 ] == "e" and chars[ i + 2 ] == "v" and chars[ i + 3 ] == "e" and chars[ i + 4 ] == "n":
            return 7
    elif char == "e" and (len(chars) - i) > 4 and chars[ i + 1 ] == "i" and chars[ i + 2 ] == "g" and chars [i + 3] == "h" and chars [i + 4] == "t":
        return 8
    elif char == "n" and (len(chars) - i) > 3 and chars[ i + 1 ] == "i" and chars[ i + 2 ] == "n" and chars [i + 3] == "e":  
        return 9

def isLetterDigitBack(chars, char, i):
    if char == "e":
        if i - 4 > 0 and chars[ i - 1 ] == "e" and chars[ i - 2 ] == "r" and chars[ i - 3 ] == "h" and chars[ i - 4 ] == "t":
            return 3
        elif i - 3 > 0 and chars[ i - 1 ] == "n" and chars[ i - 2 ] == "i" and chars[ i - 3 ] == "n": 
            return 9
        elif i - 3 > 0 and chars[ i - 1 ] == "v" and chars[ i - 2 ] == "i" and chars[ i - 3 ] == "f":
            return 5
        elif i - 2 > 0 and chars[ i - 1 ] == "n" and chars[ i - 2 ] == "o":
            return 1
    elif char == "o": 
         if i - 2 > 0 and chars[ i - 1 ] == "w" and chars[ i - 2 ] == "t":
            return 2
    elif char == "r" and i - 4 > 0 and chars[ i - 1 ] == "u" and chars[ i - 2 ] == "o" and chars[ i - 3 ] == "f":
        return 4
    elif i - 4 > 0 and char == "n" and chars[ i - 1 ] == "e" and chars[ i - 2 ] == "v" and chars[ i - 3 ] == "e" and chars[ i - 4 ] == "s":
        return 7
    elif char == "t" and i - 4 > 0 and chars[ i - 1 ] == "h" and chars[ i - 2 ] == "g" and chars [i - 3] == "i" and chars [i - 4] == "e":  
        return 8
    elif char == "x" and i - 2 > 0 and chars[ i - 1 ] == "i" and chars[ i - 2 ] == "s":  
        return 6

with open("input", "r") as file:

	Lines = file.readlines()

totalSum = 0
count = 0

# Strips the newline character
for line in Lines:
    chars = [*line.strip()];
    count += 1
    first = None
    last = None
    
    i = 0
    firstFound = False
    while i < len(chars) and not firstFound:
        if(chars[i].isdigit()):
            firstFound = True
            first = chars[i]
        else: 
            #print(chars[i])
            number = isLetterDigit(chars, chars[i], i)

            if number is not None:
                firstFound = True
                first = number
            else:
                i += 1

    i = len(chars) - 1
    lastFound = False
    while i > -1 and not lastFound:
        if(chars[i].isdigit()):
            lastFound = True
            last = chars[i]
        else: 
            number = isLetterDigitBack(chars, chars[i], i)

            if number is not None:
                lastFound = True
                last = number
            else:
                i -= 1

    sumLine = int("{}{}".format(first, last))
    totalSum += sumLine
    print("Line {} {} {}: {}".format(count, sumLine, totalSum, line.strip()))

