import TicTacToe as TTT

def game():

    game_running = True
    board = TTT.start_game()

    while(game_running):
        TTT.display_board(board)
        board = TTT.enter_move(board)

        if TTT.victory_for(board):
            game_running = False

        board = TTT.draw_move(board)

        if TTT.victory_for(board):
            game_running = False

    rematch = input("Do you want to rematch? (Y/N) ")
    if rematch == "Y" or rematch == "y":
        game()

game()
