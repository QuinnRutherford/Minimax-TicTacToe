class Game_Data:
    def __init__(self):
        self.player_sign = self.get_player_sign()
        self.computer_sign = self.get_computer_sign()
        self.players_turn = self.player_starts()

    # Function for debugging
    def print_data(self):
        print('Player sign: ' + str(self.player_sign))
        print('Computer sign: ' + str(self.computer_sign))
        print('Players turn: ' + str(self.players_turn))

    # Returns true if player starts
    def player_starts(self):
        answer = 'a'
        while answer != 'Y' and answer != 'N':
            answer = input('Would you like to start? (Y/N): ')
        if answer == 'Y':
            return True
        elif answer == 'N':
            return False

    # Returns 1 if plays is X and 2 if O
    def get_player_sign(self):
        sign = 'a'
        while sign != 'X' and sign != 'O':
            sign = input('Would you like to be X or O? ')
        if sign == 'X':
            return 1
        elif sign == 'O':
            return 2

    # Returns opposite sign of players
    def get_computer_sign(self):
        if self.player_sign == 1:
            return 2
        elif self.player_sign == 2:
            return 1
