def_value = " "
v_line = "|"
h_line = "_"

board = [[def_value] * 3 for _ in range(3)]
current_player = 'X'

while True:

    for row in board:
        print(v_line.join(row))
        print(h_line * 6)

    row = int(input(f"Player {current_player}, enter the row number (0, 1 or 2): "))
    col = int(input(f"Player {current_player}, enter the column number (0, 1 or 2): "))

    if board[row][col] == ' ':
        board[row][col] = current_player

        for row in board:
            if all(cell == row[0] for cell in row) and row[0] != def_value:
                print(f"Player {current_player} won!")
                exit()

        for col in range(3):
            if all(board[row][col] == board[0][col] and board[0][col] != def_value for row in range(3)):
                print(f"Player {current_player} won!")
                exit()

        if all(board[i][i] == board[0][0] and board[0][0] != def_value for i in range(3)):
            print(f"Player {current_player} won!")
            exit()

        if all(board[i][2 - i] == board[0][2] and board[0][2] != def_value for i in range(3)):
            print(f"Player {current_player} won!")
            exit()

        if all(cell != def_value for row in board for cell in row):
            print("The game ended in a draw!")
            exit()

        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("This cell is already occupied. Try again.")
