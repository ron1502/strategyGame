from Game.gameElements.controller import controller
from Game.gameElements.model import model
from Game.gameElements.view import view


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
	