from Game.Menu import *
from Game.Game import Game
from Game.gameElements.sprite import sprite
import os

def main():
        sprite.init(480, 480, "Best game ever")
        
        game = Game()
        game_intro(480, 480, game.run)
        
        while game.model.run:
                game.run()
                sprite.clock.tick(60)

main()
