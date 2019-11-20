import pygame

class Light(Unit):
    def __init__(self):
        super("light.jpg", "Light", 100, 5, 10, 15, 20, 25, 0, 35)
        self.xpos = super.getX()
        self.ypos = super.getY()

    def update(self):
        self.xpos = super.getX()
        self.ypos = super.getY()
        self.pygame.display.update()

# Add getters for each variable