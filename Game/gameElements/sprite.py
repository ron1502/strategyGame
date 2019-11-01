import pygame

class sprite:
	screen = None
	clock = None
	
	def __init__(self):
		print("I'm alive")
	
	@staticmethod
	def init(width, height, caption):
		pygame.init()
		screen = pygame.display.set_mode((width,height))
		pygame.display.set_caption(caption)
		clock = pygame.timing.clock()