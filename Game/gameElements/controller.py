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
                # Unit movement
                if event.key == pygame.K_w:
                elif event.key == pygame.K_s:
                elif event.key == pygame.K_a:
                elif event.key == pygame.K_d:
            elif event.type == pygame.MOUSEBUTTONUP:
                self.model.checkClick(event.pos[0], event.pos[1])
                #if model.tiles.objectToMove == none:
		    #model.tiles.setObjectToMove(pos(x,y))
		#elif model.tiles.moveObject(pos(x,y)):
		    #model.tiles.objectMoved()
		#else
		    #print("Object can't be moved to this tile")
