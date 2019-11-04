import pygame

class controller:
    def __init__(self, model):
        self.model = model
        pygame.key.set_repeat(60)
        self.keyPressed = {"a" : False, "s" : False,
                           "d" : False, "w" : False}

    def update(self):
        # Does not allow diagonal movements
        ## If diagonals movements desired, pygamey.key.get_pressed() tuple can be used instead
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.model.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # Move up
                    self.model.mainSprite.rect. y-= 10
                elif event.key == pygame.K_s:
                     # Move down
                    self.model.mainSprite.rect.y += 10
                elif event.key == pygame.K_a:
                    # Move left
                    self.model.mainSprite.rect.x -= 10
                elif event.key == pygame.K_d:
                    # Move right
                    self.model.mainSprite.rect.x += 10
            elif event.type == pygame.MOUSEBUTTONUP:
                #if model.tiles.objectToMove == none:
                    #model.tiles.setObjectToMove(pos(x,y))
                #elif model.tiles.moveObject(pos(x,y)):
                    #model.tiles.objectMoved()
                #else
                    #print("Object can't be moved to this tile")
                print("Detect source or destiny tile using event.pos")
