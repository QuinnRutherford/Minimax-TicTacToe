from board import Board
from game_data import Game_Data

# Quinn Rutherford
# 18/07/2020
# Tic Tak Toe AI using Minimax Algorithm

# Get players choice
def ask_player():
    row = -1
    while row < 1 or row > 3:
        row = int(input('Choose a row between 1-3: '))

    print(str(row))
    col = -1    
    while col < 1 or col > 3:
        col = int(input('Choose a colum between 1-3: '))
    
    if board.spot_is_full(row-1, col-1):
        print('That spot is full!')
        ask_player()
    else:
        board.fill_space(row-1, col-1, game_data.player_sign)

# Gets and places comp choice
def ask_comp():
    # choose the spot which is the best move
    spot = find_best_move()
    print('Computer chooose ' + str(spot[0] + 1) + ', ' + str(spot[1]+1))
    board.fill_space(spot[0], spot[1], game_data.computer_sign)

# Recursivly checks the outcome of each possible play
def minimax(depth, isMax):
    score = board.evaluate(game_data.player_sign, game_data.computer_sign)
 
    # If game is won return score
    if score == 10 or score == -10:
        return score
    # If board is full and no winner return 0    
    if board.moves_remain() == False:
        return 0
    
    # Maximizers turn
    if(isMax):
        best = -1000
        # Traverse all spots
        for i in range(0, 3):
            for j in range(0, 3):
                if not board.spot_is_full(i, j):
                    # Make the move
                    board.fill_space(i, j, game_data.player_sign)
                    # Call minimax recursivly and choose max
                    best = max(best, minimax(depth+1, not isMax))
                    # Remove spot from board
                    board.remove_space(i, j)
        return best
    else:
        best = 1000
        # Traverse all spots
        for i in range(0, 3):
            for j in range(0, 3):
                if not board.spot_is_full(i, j):
                    # Make the move
                    board.fill_space(i, j, game_data.computer_sign)
                    # call Minimax recursivly and choose min
                    best = min(best, minimax(depth+1, not isMax))
                    # Remove spot from board
                    board.remove_space(i, j)
        return best

# Returns an array coordinates for best spot
def find_best_move():
    best_val = 1000
    row = -1
    col = -1
    # Traverse all spots
    for i in range(0, 3):
        for j in range(0, 3):
            if not board.spot_is_full(i, j):
                board.fill_space(i, j, game_data.computer_sign)
                # true because it is now the player move
                move_val = minimax(0, True)
                board.remove_space(i, j)
                # check for lower val (comp is minimizer)
                if move_val < best_val:
                    row = i
                    col = j
                    best_val = move_val
    return [row, col]

# One player take a turn
def turn():
    if game_data.players_turn:
        ask_player()
    else:
        ask_comp()

    game_data.players_turn = not game_data.players_turn

# make turns until there is a winner or a tie
def run():
    board.print_board()
    while board.moves_remain():
        turn()
        board.print_board()
        if board.evaluate(game_data.player_sign, game_data.computer_sign) == 10:
            print('Player wins!')
            break
        elif board.evaluate(game_data.player_sign, game_data.computer_sign) == -10:
            print('Computer wins!')
            break
    if board.evaluate(game_data.player_sign, game_data.computer_sign) == 0:
        print('The game was a tie!')

print('Start')
board = Board()
game_data = Game_Data()
run()
