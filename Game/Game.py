from Game.gameElements.controller import controller
from Game.gameElements.model import model
from Game.gameElements.view import view
from pygame import mixer

mixer.music.load("lastencounter.wav")
mixer.music.set_volume(0.25)
mixer.music.play(-1)

class Game:
	def __init__(self):
		self.model = model()
		self.view = view(self.model)
		self.controller = controller(self.model)


	def run(self):
		while self.model.run:
			self.controller.update()
			self.model.update()
			self.view.update()
	