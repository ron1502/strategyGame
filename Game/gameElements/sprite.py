import pygame
import os
import random

class sprite:
	screen = None
	clock = None
	sWidth = 0
	sHeight = 0
	
	def __init__(self, x, y, w, h, sprtPath = None):
		self.rect = pygame.Rect(x, y, w, h)
		#------------------------------------------------
		# TE: Rectangle color to simulate sprite
		self.rectColor = pygame.Color(random.randint(0, 255),
					       random.randint(0, 255),
					       random.randint(0, 255))
		#-----------------------------------------------
		if(sprtPath != None): self.loadImg(sprtPath)
	
	@staticmethod
	def init(width, height, caption):
		pygame.init()
		print("Sprite init")
		sprite.screen = pygame.display.set_mode((width,height))
		print("Sprite in sprite " + str(sprite.screen))
		pygame.display.set_caption(caption)
		sprite.sHeight = height
		sprite.sWidth = width
		sprite.clock = pygame.time.Clock()
		print("Sprite initialized")

	def collide(self, collideSprite, restorePos = False):
		# Returns True if collition takes place
		collide = self.rect.colliderect(collideSprite.rect)
		if collide and restorePos:
			if self.moveDir == "LEFT":
				self.rect.x = collideSprite.rect.x + collideSprite.rect.w + 1
			elif self.moveDir == "RIGHT":
				self.rect.x = collideSprite.rect.x -1 - self.rect.w
			elif self.moveDir == "UP":
				self.rect.y = collideSprite.rect.y + collideSprite.rect.h + 1
			elif self.moveDir == "DOWN":
				self.rect.y = collideSprite.rect.y -1 - self.rect.h
		return collide


		
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
		
	def draw(self):
		self.drawImg()
	
	def printData(self):
		print("SpriteData: \nX: " + str(self.rect.x) + "\nY: " + str(self.rect.y) + "\nW:" + str(self.rect.w) + "\nH: " + str(self.rect.w))
