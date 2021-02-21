from random import randrange

def print_horizontal_divider():
    print("+-------"*3, end="+\n")

def print_vertical_divider():
        print("|       "*3, end="|\n")

def display_board(board):

    for row in board:
        print_horizontal_divider()
        print_vertical_divider()

        for entry in row:
            print("|   ", entry, "   ", sep="", end="")

        print("|")
        print_vertical_divider()
    print_horizontal_divider()

def empty_square(board, row, column):
    square = board[row][column]
    if square != "X" and square != "O":
        return True

def enter_move(board):

    not_selected = True
    while(not_selected):
        user_move = int(input("Select your position "))
        if user_move < 1 or user_move > 9:
            print("You must choose a number between 1 and 9")
            continue
        row = ((user_move-1) // 3)
        column = ((user_move-1) % 3)

        if empty_square(board, row, column):
            board[row][column] = "O"
        else:
            continue
        not_selected = False
    return board

def make_list_of_free_fields(board):
    list = []
    for row in range(3):
        for column in range(3):
            if empty_square(board, row, column):
                list.append((row, column))
    return list

def check_list(list, board):

    if list.count("X") == 3:
        display_board(board)
        print("Computer has won!")
        return True

    elif list.count("O") == 3:
        display_board(board)
        print("Player has won!")
        return True

def check_list_for_winner(board):
    for row in board:
        if check_list(row, board):
            return True

def check_column_for_winner(board):

    for column in range(3):
        vertical_list = []

        for row in range(3):
            result = board[row][column]
            vertical_list.append(result)

        if check_list(vertical_list, board):
            return True

def check_diagonals_for_winner(board):

    right_diagonal_list = []
    left_diagonal_list = []

    for i in range(3):
        result = board[i][i]
        right_diagonal_list.append(result)

        print(right_diagonal_list)

    if check_list(right_diagonal_list, board):
        return True
    
    for i in range(3):
        result = board[i][2-i]
        left_diagonal_list.append(result)

        print(left_diagonal_list)

    if check_list(left_diagonal_list, board):
        return True

def victory_for(board):

    if check_list_for_winner(board):
        return True
    
    if check_column_for_winner(board):
        return True

    if check_diagonals_for_winner(board):
        return True

    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Game was a draw!")
        return True

def draw_move(board):
    list = make_list_of_free_fields(board)
    random_empty_square = list[randrange(len(list))]
    board[random_empty_square[0]][random_empty_square[1]] = "X"
    return board

def reset_board(board):
    row_size = 3
    start_number = 1

    for i in range(row_size):
        for row in range(row_size):
            board[i][row] = start_number
            start_number+=1
        board[1][1] = "X"
    return board

def init_board():
    EMPTY = "EMPTY"
    board = []
    row_size = 3
    start_number = 1

    for i in range(row_size):
        row = [EMPTY for i in range(row_size)]
        board.append(row)
    return board

def start_game():
    empty_board = init_board()
    board = reset_board(empty_board)
    return board