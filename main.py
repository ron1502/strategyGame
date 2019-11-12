from Game.Menu import *
from Game.Game import Game
from Game.gameElements.sprite import sprite
import os

def main():
        # Eliminate Duplicate operations
        sprite.init(1080, 720, "Best game ever")

        print("Initializing game")
        game = Game()
        game_intro(1080, 720, game.run)
        
        while game.model.run:
                game.run()
                sprite.clock.tick(60)

main()
