from Entity import Entity

class Bouncy(Entity):
        def __init__(self, world=None, x=0, y=0, sprite=None, depth=-1, player=None):
            super().__init__(world, x, y, depth=depth)
            if sprite == None:
                self.sprite = world.assetLoader.bouncy
            else:
                self.sprite = sprite
            self.player = player
            self.animating = False
            
        def update(self):
            super().update()
            if not self.player.isStable and self.isColliding(self.player):
                difference = (self.x - self.player.x, self.y - self.player.y)
                if difference[0] > 0:
                    if abs(difference[1]) < difference[0]:
                        self.player.hSpeed = -abs(self.player.hSpeed)
                    elif difference[1] > 0:
                        self.player.vSpeed = -abs(self.player.vSpeed)
                    else:
                        self.player.vSpeed = abs(self.player.vSpeed)
                else:
                    if abs(difference[1]) < abs(difference[0]):
                        self.player.hSpeed = abs(self.player.hSpeed)
                    elif difference[1] > 0:
                        self.player.vSpeed = -abs(self.player.vSpeed)
                    else:
                        self.player.vSpeed = abs(self.player.vSpeed)
                if not self.animating:
                    self.world.assetLoader.sndBouncy.play()
                self.animating = True
                self.player.startFloat()
        
        def animationEnd(self):
            super().animationEnd()
            self.animating = False