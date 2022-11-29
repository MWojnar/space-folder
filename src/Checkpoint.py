from Entity import Entity

class Checkpoint(Entity):
        def __init__(self, world=None, x=0, y=0, sprite=None, depth=-1, player=None):
            super().__init__(world, x, y, depth=depth)
            if sprite == None:
                self.sprite = world.assetLoader.checkpoint
            else:
                self.sprite = sprite
            self.player=player
            self.isRectMask = True
            self.rectMask = (-self.sprite.width / 4, -self.sprite.height / 2, self.sprite.width / 2, self.sprite.height)
            self.triggered = False
            
        def update(self):
            super().update()
            if not self.triggered and self.isColliding(self.player):
                self.player.hitCheckpoint(self)
                self.trigger()
            
        def trigger(self):
            self.triggered = True
            self.sprite = self.world.assetLoader.checkpointGet
            
        def untrigger(self):
            self.triggered = False
            self.sprite = self.world.assetLoader.checkpoint
            self.frame = 0
            
        def animationEnd(self):
            super().animationEnd()
            if self.sprite == self.world.assetLoader.checkpointGet:
                self.sprite = self.world.assetLoader.checkpointGot