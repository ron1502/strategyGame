import pygame

class controller:
    
    def __init__(self, model):
        self.model = model
        pygame.key.set_repeat(60)

    def update(self):
        # Does not allow diagonal movements
	## If diagonals movements desired, pygamey.key.get_pressed() tuple can be used instead
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.model.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.model.mainSprite.rect. y-= 10
                    self.model.mainSprite.moveDir = "UP"
                elif event.key == pygame.K_s:
                    self.model.mainSprite.rect.y += 10
                    self.model.mainSprite.moveDir = "DOWN"
                elif event.key == pygame.K_a:
                    self.model.mainSprite.rect.x -= 10
                    self.model.mainSprite.moveDir = "LEFT"
                elif event.key == pygame.K_d:
                    self.model.mainSprite.rect.x += 10
                    self.model.mainSprite.moveDir = "RIGHT"
            elif event.type == pygame.MOUSEBUTTONUP:
                print("Detect source or destiny tile using event.pos")
                #if model.tiles.objectToMove == none:
		    #model.tiles.setObjectToMove(pos(x,y))
		#elif model.tiles.moveObject(pos(x,y)):
		    #model.tiles.objectMoved()
		#else
		    #print("Object can't be moved to this tile")
