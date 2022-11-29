from Entity import Entity
import random

class Spike(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=-1, player=None):
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.mediumSpikes
        else:
            self.sprite = sprite
        self.animationSpeedTimer = 0
        self.frame = 0
        self.player = player
        self.circleMaskCenter = (0, 0)
        self.circleMaskRadius = self.sprite.width / 2 - 3
        self.rotationSpeed = random.random() - 0.5
        
    def update(self):
        super().update()
        if self.isColliding(self.player):
            self.player.die()