from array import *

class Board:
    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    # Prints current board
    def print_board(self):
        print('---------------')
        print('     1 2 3')
        row = 1
        for i in self.board:
            print(str(row) + '   ', end ='')
            row = row + 1
            for j in i:
                if j == 0:
                    print('  ', end = '')
                elif j == 1:
                    print(' X', end = '')
                elif j == 2:
                    print(' O', end = '')
            print('')
        print('---------------')
    
    # Returns true if board is full
    def moves_remain(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    return True
        return False

    # Places num at row, col
    def fill_space(self, row, col, num):
        self.board[row][col] = num

    # Removes a value from row, col
    def remove_space(self, row, col):
        self.board[row][col] = 0

    # Checks if spot is full
    def spot_is_full(self, row, col):
        if self.board[row][col] == 0:
            return False
        else:
            return True

    # Returns value based on who is winning
    def evaluate(self, player_sign, comp_sign):
        # Check for row win
        for i in self.board:
            if i[0] == i[1] and i[1] == i[2]:
                if i[0] == player_sign:
                    return 10
                elif i[0] == comp_sign:
                    return -10
        
        # Check for col win
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == player_sign:
                    return 10
                elif self.board[0][i] == comp_sign:
                    return -10

        # Bottom left to top right
        if self.board[2][0] != 0 and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            if self.board[1][1] == player_sign:
                return 10
            elif self.board[1][1] == comp_sign:
                return -10
            return True

        # Top left to bottom right
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if self.board[1][1] == player_sign:
                return 10
            elif self.board[1][1] == comp_sign:
                return -10

        # Return 0 is nobody wins
        return 0
