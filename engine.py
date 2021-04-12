class game_logic(): # a class which stores everything about the game, change to tweak how the entire game functions
	def __init__(self):
		self.board = [ #a child that represents everything to do with the board, change info code here to change how the board functions
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'], # items in a list represent pieces in standard notation, e.g. bB = 'black Bishop'
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
		self.white_moves = True
	def move_made(self, move):
                self.board[move.initial_row][move.initial_column] = '--' #setting place to blank after move is made
                self.board[move.ending_row][move.ending_column] = move.starting_position
                self.white_moves = not self.white_moves

print(game_logic().board)
		
class move():
      def __init__(self, start, end, board):
            self.initial_row = start[0]
            self.initial_column = start[1]
            self.ending_row = end[0]
            self.ending_column = end[1]
            self.starting_position = board[self.initial_row][self.initial_column]
            self.ending_position = board[self.ending_row][self.ending_column]

 