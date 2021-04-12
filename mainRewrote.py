#import features 
import pygame  
import engine
import piece 
import sys

# screen config
height = 500 #edit to change screen height 
width = 500
dimension = 8 #dimension of an 8x8 chess board
square_size = height//dimension
FPS = 30

#pygame settings 
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tapton Chess Club')
clock = pygame.time.Clock()
screen.fill(pygame.Color("white"))
board_format = engine.game_logic()
pieces = piece.piece()

#calls functions to draw the board
def draw_board(screen, board_format, pieces):
	draw_squares(screen)
	create_pieces(screen, board_format.board, pieces.piece_img)

#draw squares on screen using 2d array
def draw_squares(screen):
        square_colours = [pygame.Color("#ffdbdc"), pygame.Color("#f25a5c")]
        for row in range(dimension):
                for column in range(dimension):
                        sq_colour = square_colours[((row+column)%2)] #used to find the colour of the square
                        pygame.draw.rect(screen, sq_colour, pygame.Rect(row*square_size, column*square_size, square_size, square_size))

# draw pieces on the board 
def create_pieces(screen, board, piece_img):
	for row in range(dimension):
		for column in range(dimension):
			piece = board[row][column]
			if piece != "--":
				for i in piece_img:
					resized_img = pygame.transform.scale(piece_img[i], (square_size, square_size)) #fits image to square
					if i == piece:
						screen.blit(resized_img, pygame.Rect(column*square_size, row*square_size, square_size, square_size))


#pygame main loop
running = True 
previous_square = () #stores the square clicked (row and column)
player_clicks = [] #stores both of the clicked coordinates 
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                	location = pygame.mouse.get_pos()
                	col_clicked = location[0]//square_size
                	row_clicked = location[1]//square_size
                	previous_square = (row_clicked, col_clicked)
                	player_clicks.append(previous_square)

                	if len(player_clicks) == 2:
                		move_piece = engine.move(player_clicks[0], player_clicks[1], board_format.board)
                		board_format.move_made(move_piece)
                		previous_square = () #resets stored clicks for new move
                		player_clicks = [] #resets stored coordinates for new move

        draw_board(screen, board_format, pieces)
        clock.tick(FPS)
        pygame.display.flip()

