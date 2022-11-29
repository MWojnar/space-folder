from Entity import Entity
import Utility
import math
class RepelOrbTether(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=-2, player=None, repelOrb = None):
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.repelTether
        else:
            self.sprite = sprite
        self.visible = False
        self.player = player
        self.repelOrb = repelOrb
        self.scale = 1
        
    def update(self):
        super().update()
        self.x = (self.player.x + self.repelOrb.x) / 2
        self.y = (self.player.y + self.repelOrb.y) / 2
        self.scale = int(Utility.getDistance((self.player.x, self.player.y), (self.repelOrb.x, self.repelOrb.y)))
        self.rotation = -math.degrees(math.atan2(self.player.y - self.repelOrb.y, self.player.x - self.repelOrb.x)) + 90
        
    def draw(self, surface):
        if self.visible:
            self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation, vScale=self.scale)