from Entity import Entity

class Cursor(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=1000000):
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.mouse
        else:
            self.sprite = sprite
        self.canClick = False
        self.visible = True
        
    def update(self):
        super().update()
        self.x = self.world.mousePos[0] + self.sprite.width / 2
        self.y = self.world.mousePos[1] + self.sprite.height / 2
        if self.canClick:
            self.sprite = self.world.assetLoader.mouseCanClick
        else:
            self.sprite = self.world.assetLoader.mouse
        self.canClick = False
        
    def draw(self, surface):
        if self.visible:
            super().draw(surface)