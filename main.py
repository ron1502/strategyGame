from Game.Menu import Menu
from Game.Game import Game
from Game.gameElements.sprite import sprite
import os

def main():
        sprite.init(480, 480, "Best game ever")
        
        menu = Menu()
        game = Game()
        
        while game.model.run:
                game.run()
                sprite.clock.tick(60)

main()
