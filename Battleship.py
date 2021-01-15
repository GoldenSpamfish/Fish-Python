from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(boardIn):
    for row in boardIn:
        print(" ".join(row))


print_board(board)


def random_row(boardIn):
    return randint(0, len(boardIn) - 1)


def random_col(boardIn):
    return randint(0, len(boardIn[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)


def guess(turnNum):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        return -99
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turnNum == 3:
            print("Game Over")
        else:
            print_board(board)


for turn in range(4):
    print("Turn " + str(turn + 1))
    if guess(turn) == -99:
        break
