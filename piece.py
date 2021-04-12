import pygame 

#class containing information realted to the pieces
class piece():
	def __init__(self):
		self.piece_img = {
		'wP': pygame.image.load('Images/wP.png'),
		'wR': pygame.image.load('Images/wR.png'),
		'wN': pygame.image.load('Images/wN.png'),
		'wB': pygame.image.load('Images/wB.png'),
		'wQ': pygame.image.load('Images/wQ.png'),
		'wK': pygame.image.load('Images/wK.png'),
		'bP': pygame.image.load('Images/bP.png'),
		'bR': pygame.image.load('Images/bR.png'),
		'bN': pygame.image.load('Images/bN.png'),
		'bB': pygame.image.load('Images/bB.png'),
		'bQ': pygame.image.load('Images/bQ.png'),
		'bK': pygame.image.load('Images/bK.png')
		}