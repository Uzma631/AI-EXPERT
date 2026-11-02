
import random

def show_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def check_win(board, symbol):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False


def player_move(board, symbol):
    move = int(input("Choose a position (1-9): ")) - 1

    while move not in range(9) or not board[move].isdigit():
        move = int(input("Invalid! Choose an empty position (1-9): ")) - 1

    board[move] = symbol


def ai_move(board, ai, player):
    # Win if possible; otherwise block the player
    for symbol in [ai, player]:
        for i in range(9):
            if board[i].isdigit():
                copy_board = board.copy()
                copy_board[i] = symbol

                if check_win(copy_board, symbol):
                    board[i] = ai
                    return

    # Otherwise, choose a random empty position
    empty = [i for i in range(9) if board[i].isdigit()]
    board[random.choice(empty)] = ai


def play_game():
    board = list("123456789")
    player = input("Choose X or O: ").upper()
    ai = "O" if player == "X" else "X"

    while True:
        show_board(board)
        player_move(board, player)

        if check_win(board, player):
            show_board(board)
            print("You win!")
            break

        if all(not cell.isdigit() for cell in board):
            print("It's a tie!")
            break

        ai_move(board, ai, player)

        if check_win(board, ai):
            show_board(board)
            print("AI wins!")
            break

        if all(not cell.isdigit() for cell in board):
            show_board(board)
            print("It's a tie!")
            break

    show_board(board)


play_game()
