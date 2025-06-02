def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Reihen
    for row in board:
        if all(s == player for s in row):
            return True
    # Spalten
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Diagonalen
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(
            f"Spieler {current_player}, gib deine Position ein (Zeile und Spalte, z. B. '0 2'):")
        try:
            row, col = map(int, input().split())
            if row not in range(3) or col not in range(3):
                print("Ungültige Eingabe. Nur Werte von 0 bis 2 erlaubt.")
                continue
            if board[row][col] != ' ':
                print("Feld bereits belegt! Versuch es nochmal.")
                continue
        except ValueError:
            print("Ungültige Eingabe. Bitte zwei Zahlen eingeben.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Spieler {current_player} hat gewonnen!")
            break

        if check_draw(board):
            print_board(board)
            print("Unentschieden!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()
