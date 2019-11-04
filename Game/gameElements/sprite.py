import pygame
import os
import random

class sprite:
	screen = None
	clock = None
	
	def __init__(self, x, y, w, h, sprtPath = None):
		self.rect = pygame.Rect(x, y, w, h)
		#------------------------------------------------
		# TE: Rectangle color to simulate sprite
		self.rectColor = pygame.Color(random.randint(0, 255),
					       random.randint(0, 255),
					       random.randint(0, 255))
		#-----------------------------------------------
		if(sprtPath != None): self.loadImg(sprtPath)
		print("I'm alive")
	
	@staticmethod
	def init(width, height, caption):
		pygame.init()
		sprite.screen = pygame.display.set_mode((width,height))
		pygame.display.set_caption(caption)
		sprite.clock = pygame.time.Clock()
		print("Sprite initialized")

	def collide(self, colideSprite):
                # Returns True if collition takes place
                return self.rect.colliderect(colideSprite.rect)

		
	def loadImg(self, imgPath):
                # Turns image path into an absolute path using the current working directory
                # Loads image and rescale using the dimension defined in self.rect
		imgPath = os.getcwd() + imgPath
		self.img = pygame.image.load(imgPath).convert()
		self.img = pygame.transform.scale(self.img, (self.rect.w, self.rect.h))
	
	def getX(self):
		return self.rect.x
	
	def getY(self):
		return self.y

	def drawSquare(self, color = None):
		if color == None: color = self.rectColor 
		pygame.draw.rect(sprite.screen, color, self.rect)

	def drawImg(self):
		sprite.screen.blit(self.img, self.rect)
