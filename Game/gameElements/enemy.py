from Game.gameElements.sprite import sprite
class worm(sprite):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.attack = 10
        self.idle = [self.loadImg(r"\resources\sprites\worm\idle\00.png"), self.loadImg(r"\resources\sprites\worm\idle\01.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\02.png"), self.loadImg(r"\resources\sprites\worm\idle\03.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\04.png"), self.loadImg(r"\resources\sprites\worm\idle\05.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\06.png"), self.loadImg(r"\resources\sprites\worm\idle\07.png")]

        self.animationCount = 0

        self.img = idle[0]

        self.idle = True

        def update(self):
            if(self.idle):
                
        def draw(self):
            self.drawImg()

