from Entity import Entity

def emptyFunc():
    pass

class Button(Entity):
    def __init__(self, world=None, x=0, y=0, defaultSprite=None, hoverSprite=None, clickEvent=emptyFunc, cursor=None):
        super().__init__(world, x, y, depth=-5)
        self.sprite = defaultSprite
        self.defaultSprite = defaultSprite
        self.hoverSprite = hoverSprite
        self.lastButtonState = False
        self.clickEvent = clickEvent
        self.cursor = cursor
        
    def update(self):
        super().update()
        if self.pointInImage(self.world.mousePos):
            self.cursor.canClick = True
            self.sprite = self.hoverSprite
            if not self.world.buttonState[0] and self.lastButtonState:
                self.clickEvent()
                self.world.alreadyClicked = True
        else:
            self.sprite = self.defaultSprite
        self.lastButtonState = self.world.buttonState[0]
        
    def pointInImage(self, pos):
        return (pos[0] > self.x - self.sprite.width / 2 and pos[0] < self.x + self.sprite.width / 2 and
            pos[1] > self.y - self.sprite.height / 2 and pos[1] < self.y + self.sprite.height / 2)