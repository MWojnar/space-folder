from Entity import Entity
from Button import Button

class Victory(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
        super().__init__(world, x, y, depth)
        if sprite == None:
            self.sprite = self.world.assetLoader.victory
        else:
            self.sprite = sprite
        self.scale = 0
        self.scaleChange = 0.02
        self.lastButtonState = False
        self.scaled = False
            
    def update(self):
        super().update()
        self.scale += self.scaleChange
        if (self.scale > 1):
            self.scale = 1
            if not self.scaled:
                self.scaled = True
                dribbleButton = Button(self.world, self.world.screenWidth / 2, self.world.screenHeight * 3 / 4, self.world.assetLoader.dribblePromo, self.world.assetLoader.dribblePromoSelected, self.world.dribbleURL, self.world.cursor)
                self.world.addEntity(dribbleButton)
        if not self.world.buttonState[0] and self.lastButtonState and not self.world.alreadyClicked:
            self.world.loadMenu()
        self.lastButtonState = self.world.buttonState[0]
        
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation, self.sprite.width * self.scale, self.sprite.height * self.scale)