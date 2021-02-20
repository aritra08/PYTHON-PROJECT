import random


def drawBoard(board):
    print(board[7] + '|' + board[8] + ' |' + board[9])
    print('-+--+-')
    print(board[4] + '|' + board[5] + ' |' + board[4])
    print('-+--+-')
    print(board[1] + '|' + board[2] + ' |' + board[3])


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):

        print('Do you want to be X or O?')
        letter = input().upper()
        return 'X', 'O' if letter == 'X' else letter == 'O'

def whoGoesFirst():
    if random.randint(0, 1) == 'O':
        return 'computer'
    else:
        return 'player'
    # return 'computer', 'player' if random.randint(0, 1) == 'O' else 'X'


def makeMove(board, letter, choice):  # The variable move is stored on a particular position on the board
    board[choice] = letter


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter)
            )


def getBoardCopy(board):  # For the purpose of AI
    boardCopy = [i for i in board]
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '  # It returns true if an empty string is vacant for a move otherwise false


def getPlayerMove(board):  # Let the player enter the move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Whats your next move ? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moveslist):
    possibleMove = [i for i in moveslist if isSpaceFree(board, i) == True]
    if len(possibleMove) != 0:
        return random.choice(possibleMove)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = '0'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        boardcopy = getBoardCopy(board)
        if isSpaceFree(boardcopy, i):
            makeMove(boardcopy, computerLetter, i)
            if isWinner(boardcopy, computerLetter):
                return i
    for i in range(1, 10):
        boardcopy = getBoardCopy(board)
        if isSpaceFree(boardcopy, i):
            makeMove(boardcopy, playerLetter, i)
            if isWinner(boardcopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != ' ':
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic-Tac-Toe!")
while True:
    theboard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The' + turn + 'will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theboard)
            move = getPlayerMove(theboard)
            makeMove(theboard, playerLetter, move)
            if isWinner(theboard, playerLetter):
                drawBoard(theboard)
                print('Hoorayy ! You have won the match')
                gameIsPlaying = False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print('The game is tie')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theboard, computerLetter)
            makeMove(theboard, computerLetter, move)
            if isWinner(theboard, computerLetter):
                drawBoard(theboard)
                print('OOPS ! You have lost the match')
                gameIsPlaying = False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print('The game is tie')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (YES or NO)')
    if not input().lower().startswith('y'):
        break
