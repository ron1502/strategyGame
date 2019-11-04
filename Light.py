class Light(Project):
    def __init__(self):
        super("light.jpg", "Light", 100, 5, 10, 15, 20, 25, 0, 35)
        self.xpos = super.getX()
        self.ypos = super.getY()

    #def update(Graphics g):
        #xpos = super.getX()
        #ypos = super.getY()
        # Movement Function
        #super.update(g)