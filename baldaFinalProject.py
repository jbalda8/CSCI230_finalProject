import random

# Define lists and row and column values for later purposes
allCoordinates = []
coordinateBoard = []
rowValues = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
columnValues = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')


# define function that adds all grid values to list in order
def setCoordinates():
    for a in rowValues:
        for b in columnValues:
            allCoordinates.append(a + b)

    for c in range(0, 10):
        row = allCoordinates[c*10:c*10 + 10]
        coordinateBoard.append(row)


# Create game board of all zeros
# https://stackoverflow.com/questions/4056768/how-to-declare-array-of-zeros-in-python-or-an-array-of-a-certain-size
gameBoard = [[0 for column in range(10)] for row in range(10)]

# This list will eventually be a list of all grid values that are made up of pieces. Pieces are removed from this
# list as the user guesses that spot. Once all pieces are gone, this means the user wins
usedShipLocation = []

# Will eventually be a list of grid location for each piece
carrier = []
battleship = []
cruiser = []
submarine = []
destroyer = []


# Placement of five piece. Easiest piece as no other pieces are on board
def placeCarrier():
    # Picks horizontal or vertical orientation for the piece
    orientation = random.randint(1, 2)

    # For horizontal piece
    if orientation == 1:
        startingRow = random.randint(0, 9)
        startingColumn = random.randint(0, 5)

        # Adds Piece to gameBoard
        for j in range(0, 5):
            placeValue = coordinateBoard[startingRow][startingColumn + j]
            carrier.append(placeValue)
            gameBoard[startingRow][startingColumn + j] = 1

    # For vertical piece
    if orientation == 2:
        startingRow = random.randint(0, 5)
        startingColumn = random.randint(0, 9)

        # Adds piece to gameBoard
        for j in range(0, 5):
            placeValue = coordinateBoard[startingRow + j][startingColumn]
            carrier.append(placeValue)
            gameBoard[startingRow + j][startingColumn] = 1


# Create and place battleship piece. The next four pieces follow the same algorithm since pieces are not on the board
def placeBattleship():
    # battleship list is cleared. This is for when the added spots are not available, the function can restart
    battleship.clear()
    orientation = random.randint(1, 2)

    if orientation == 1:
        startingRow = random.randint(0, 9)
        startingColumn = random.randint(0, 6)

        for j in range(0, 4):
            placeValue = coordinateBoard[startingRow][startingColumn + j]
            battleship.append(placeValue)

    if orientation == 2:
        startingRow = random.randint(0, 6)
        startingColumn = random.randint(0, 9)

        for j in range(0, 4):
            placeValue = coordinateBoard[startingRow + j][startingColumn]
            battleship.append(placeValue)

    # check if pieces are available
    a = set(battleship)
    b = set(usedShipLocation)
    overlap = b.intersection(a)
    numberOverlap = len(overlap)

    # If spots are used, redo function until they are
    if numberOverlap > 0:
        placeBattleship()

    # when piece is finally able to be put, change location spots to 1 to denote that piece.
    else:
        for x in range(0, 4):

            if orientation == 1:
                # My algorithm is a little different than the first piece, since I can't call the starting point
                # I need to redefine it
                startingPointIndex = allCoordinates.index(battleship[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10*startingRow

                for u in range(0, 4):
                    gameBoard[startingRow][startingColumn + u] = 1

            elif orientation == 2:
                startingPointIndex = allCoordinates.index(battleship[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10 * startingRow

                for u in range(0, 4):
                    gameBoard[startingRow + u][startingColumn] = 1


# Place cruiser piece, same algorithm as battleship but with slightly tweaked values. Check my comments in battleship
def placeCruiser():
    cruiser.clear()
    orientation = random.randint(1, 2)

    if orientation == 1:
        startingRow = random.randint(0, 9)
        startingColumn = random.randint(0, 7)

        for j in range(0, 3):
            placeValue = coordinateBoard[startingRow][startingColumn + j]
            cruiser.append(placeValue)

    if orientation == 2:
        startingRow = random.randint(0, 7)
        startingColumn = random.randint(0, 9)

        for j in range(0, 3):
            placeValue = coordinateBoard[startingRow + j][startingColumn]
            cruiser.append(placeValue)

    a = set(cruiser)
    b = set(usedShipLocation)
    overlap = b.intersection(a)
    numberOverlap = len(overlap)

    if numberOverlap > 0:
        placeCruiser()

    else:
        for x in range(0, 3):

            if orientation == 1:
                startingPointIndex = allCoordinates.index(cruiser[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10 * startingRow

                for u in range(0, 3):
                    gameBoard[startingRow][startingColumn + u] = 1

            elif orientation == 2:
                startingPointIndex = allCoordinates.index(cruiser[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10 * startingRow

                for u in range(0, 3):
                    gameBoard[startingRow + u][startingColumn] = 1


# Place submarine piece, same algorithm as battleship but with slightly tweaked values. Check my comments in battleship
def placeSubmarine():
    submarine.clear()
    orientation = random.randint(1, 2)

    if orientation == 1:
        startingRow = random.randint(0, 9)
        startingColumn = random.randint(0, 7)

        for j in range(0, 3):
            placeValue = coordinateBoard[startingRow][startingColumn + j]
            submarine.append(placeValue)

    if orientation == 2:
        startingRow = random.randint(0, 7)
        startingColumn = random.randint(0, 9)

        for j in range(0, 3):
            placeValue = coordinateBoard[startingRow + j][startingColumn]
            submarine.append(placeValue)

    a = set(submarine)
    b = set(usedShipLocation)
    overlap = b.intersection(a)
    numberOverlap = len(overlap)

    if numberOverlap > 0:
        placeSubmarine()

    else:
        for x in range(0, 3):

            if orientation == 1:
                startingPointIndex = allCoordinates.index(submarine[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10 * startingRow

                for u in range(0, 3):
                    gameBoard[startingRow][startingColumn + u] = 1

            elif orientation == 2:
                startingPointIndex = allCoordinates.index(submarine[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10 * startingRow

                for u in range(0, 3):
                    gameBoard[startingRow + u][startingColumn] = 1


# Place destroyer piece, same algorithm as battleship but with slightly tweaked values. Check my comments in battleship
def placeDestroyer():
    destroyer.clear()
    orientation = random.randint(1, 2)

    if orientation == 1:
        startingRow = random.randint(0, 9)
        startingColumn = random.randint(0, 8)

        for j in range(0, 2):
            placeValue = coordinateBoard[startingRow][startingColumn + j]
            destroyer.append(placeValue)

    if orientation == 2:
        startingRow = random.randint(0, 8)
        startingColumn = random.randint(0, 9)

        for j in range(0, 2):
            placeValue = coordinateBoard[startingRow + j][startingColumn]
            destroyer.append(placeValue)

    a = set(destroyer)
    b = set(usedShipLocation)
    overlap = b.intersection(a)
    numberOverlap = len(overlap)

    if numberOverlap > 0:
        placeDestroyer()

    else:
        for x in range(0, 2):

            if orientation == 1:
                startingPointIndex = allCoordinates.index(destroyer[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10 * startingRow

                for u in range(0, 2):
                    gameBoard[startingRow][startingColumn + u] = 1

            elif orientation == 2:
                startingPointIndex = allCoordinates.index(destroyer[0])
                startingRow = startingPointIndex // 10
                startingColumn = startingPointIndex - 10 * startingRow

                for u in range(0, 2):
                    gameBoard[startingRow + u][startingColumn] = 1


# Define function to print user board after guesses
def printBoard():

    # Column values
    print(Colors.COLUMNS + "  1 2 3 4 5 6 7 8 9 10" + Colors.RESET)

    # This next part takes each instance in rowValues list defined in the very first few lines, and prints each element
    # of the userBoard for each row value
    # I found some information on how to do this, but changed it a lot to work for what I wanted
    # https://www.geeksforgeeks.org/python-printing-list-vertically/
    for x in rowValues:
        print(Colors.ROWS + x + Colors.RESET, end=' ')
        y = rowValues.index(x)

        for z in range(0, 10):
            listRow = userBoard[y]
            print(listRow[z], end=' ')
        print()


# Define userBoard with original values of '-'
# https://stackoverflow.com/questions/4056768/how-to-declare-array-of-zeros-in-python-or-an-array-of-a-certain-size
userBoard = [['-' for x in range(10)] for y in range(10)]


# Create class colors to use for print statements. Makes things flow better
# Retrieved from DelftStack in article title "Python Print Colored Text"
class Colors:
    HIT = '\u001b[32m'
    MISS = '\u001b[31m'
    RESET = '\u001b[0m'
    TITLE = '\u001b[34m'
    SINK = '\u001b[33m'
    ROWS = '\u001b[33m'
    COLUMNS = '\u001b[35m'


# Define menu where user chooses difficulty
def menu():
    print("Welcome to a BASIC BATTLESHIP GAME")
    # Put instructions here formatted to look nice
    print("Choose your difficulty")
    print("""
    1) Easy (80 Attempts) 
    2) Medium (65 Attempts)
    3) Hard (50 Attempts)
    4) Impossible (35 Attempts)
    """)

    response = str(input("What is your choice: "))
    responseChoices = ['1', '2', '3', '4']
    while response not in responseChoices:
        print("That is not an option!")
        response = str(input("Please choose single integer values (such as 2 for 'Medium' difficulty): "))
        if response in responseChoices:
            break

    # Next lines set attempts value based on user choice for difficulty
    if response == '1':
        attempts = 80

    elif response == '2':
        attempts = 65

    elif response == '3':
        attempts = 50

    elif response == '4':
        attempts = 35

    return attempts


# Define user guesses as a list of all valid user guesses
userGuesses = []

# This list actually checks to see if the guess was already guessed
tempGuess = []


# Define game
def game():
    attempts = menu()
    gameWinCheck = []
    gameWinCheck.extend(usedShipLocation)
    # For each individual attempt

    while attempts > 0:
        tempGuess.clear()
        print(Colors.TITLE + 'Here is your current battleship board:' + Colors.RESET)
        printBoard()
        userGuess = str(input("Guess a spot (Use Grid values such as A5): "))

        # Check user input
        while userGuess in userGuesses:
            print("You have already guessed that spot!")
            userGuess = str(input("Please guess another spot (Use Grid values such as A5): "))

            while userGuess not in allCoordinates:
                print("That is not a correct value!")
                userGuess = str(input("Guess a spot (Use Grid values such as A5): "))
                if userGuess in allCoordinates:
                    break

            if userGuess not in userGuesses:
                break

        # Check user input
        while userGuess not in allCoordinates:
            print("That is not a correct value!")
            userGuess = str(input("Guess a spot (Use Grid values such as A5): "))
            if userGuess in allCoordinates:
                break

        # Checks for hit pieces and adds X to update board
        if userGuess in usedShipLocation:
            print(Colors.HIT + "HIT!")

            tempGuess.append(userGuess)
            Index = allCoordinates.index(tempGuess[0])
            Row = Index // 10
            Column = int(Index - 10 * Row)
            userBoard[Row][Column] = 'X'

        # Checks for missed pieces and adds m to update board
        elif userGuess not in usedShipLocation:
            print(Colors.MISS + "MISS!")

            tempGuess.append(userGuess)
            Index = allCoordinates.index(tempGuess[0])
            Row = Index // 10
            Column = Index - 10 * Row
            userBoard[Row][Column] = 'm'

        # Next 5 if statements check for hit pieces and removes that spot from individual piece
        if userGuess in carrier:
            carrier.remove(userGuess)
            gameWinCheck.remove(userGuess)
            if not carrier:
                print("You have sunk my carrier ship!! Good job (:")

        if userGuess in battleship:
            battleship.remove(userGuess)
            gameWinCheck.remove(userGuess)
            if not battleship:
                print("You have sunk my battleship ship!! Good job (:")

        if userGuess in cruiser:
            cruiser.remove(userGuess)
            gameWinCheck.remove(userGuess)
            if not cruiser:
                print("You have sunk my cruiser ship!! Good job (:")

        if userGuess in submarine:
            submarine.remove(userGuess)
            gameWinCheck.remove(userGuess)
            if not submarine:
                print("You have sunk my submarine ship!! Good job (:")

        if userGuess in destroyer:
            destroyer.remove(userGuess)
            gameWinCheck.remove(userGuess)
            if not destroyer:
                print("You have sunk my destroyer ship!! Good job (:")

        # If user sinks all ships
        if not gameWinCheck:
            print(Colors.HIT + '')
            print("CONGRATS!! YOU HAVE SUNK ALL MY SHIPS!!")
            print("YOU HAD {} ATTEMPTS REMAINING!!".format(attempts))
            print("THANK YOU MY PLAYING MY BATTLESHIP GAME!! PLAY AGAIN SOON!!" + Colors.RESET)
            break

        # If user does not have enough remaining attempts
        if attempts <= len(gameWinCheck):
            print(Colors.MISS + "YOU LOSE!! YOU DO NOT HAVE ENOUGH ATTEMPTS TO SINK ALL MY SHIPS!!")
            print("THANKS FOR PLAYING MY BATTLESHIP GAME!! PLAY AGAIN SOON!!" + Colors.RESET)
            break

        # Decrement attempts and print out new value
        attempts -= 1
        print(Colors.TITLE + "You have {} attempts left".format(attempts) + Colors.RESET)
        userGuesses.append(userGuess)


# Define main
def main():

    setCoordinates()

    placeCarrier()
    # once piece is placed, added piece grid values to all location list
    usedShipLocation.extend(carrier)

    placeBattleship()
    # once piece is placed, added piece grid values to all location list
    usedShipLocation.extend(battleship)

    placeCruiser()
    # once piece is placed, added piece grid values to all location list
    usedShipLocation.extend(cruiser)

    placeSubmarine()
    # once piece is placed, added piece grid values to all location list
    usedShipLocation.extend(submarine)

    placeDestroyer()
    # once piece is placed, added piece grid values to all location list
    usedShipLocation.extend(destroyer)

    # Start game
    game()


# call main
main()
