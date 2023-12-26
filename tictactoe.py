import random

board = ["-", "-", "-",     # Empty board of Tic Tac Toe
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"         # You are player X
winner = None               
gameRunning = True          # Global variable assigned true to run the game until it is tie or a player wins

def printBoard(board):      # Print the Board                    
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):     # Ask player for the input position
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")

def checkHorizontle(board): # Check if any horizontal line has three X's or O's that makes a player win
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):        # Check if any vertical line has three X's or O's that makes a player win
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

def checkDiag(board):       # Check if any diagonal line has three X's or O's that makes a player win
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):          # Calling check horizontal looking for a winner
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):               # Calling check vertial looking for a winner
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):              # Calling check diagonal looking for a winner
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):                  # If all "-" are eliminated from the board, then it is a tie.
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def switchPlayer():                     # Switches player from computer to user after every turn.
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):                    # Picks a random number to for computer's turn to enter.
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:                      
    printBoard(board)                   # Print Board
    playerInput(board)                  # Ask player for input position
    checkIfWin(board)                   # Check if winning in Horizontal, Vertical, Diagonal
    checkIfTie(board)                   # Check if there is no winner
    switchPlayer()                      # Switch players
    computer(board)                     # Computer's turn to input
    checkIfWin(board)                   # Check if winning in Horizontal, Vertical, Diagonal
    checkIfTie(board)                   # Check if there is no winner