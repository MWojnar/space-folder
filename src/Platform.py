from Entity import Entity

class Platform(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=-1, player=None):
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.satellitePlatform
        else:
            self.sprite = sprite
        self.animationSpeedTimer = 0
        self.frame = 0
        self.player = player
        self.isRectMask = True
        self.rectMask = (-self.sprite.width / 2, -self.sprite.height / 2, self.sprite.width, self.sprite.height)
        
    def update(self):
        super().update()
        if not(self.frame == 0 or self.frame == 4 or self.frame == 5 or self.frame == 9):
            if not self.player.isStable and self.isColliding(self.player):
                difference = (self.x - self.player.x, self.y - self.player.y)
                if difference[0] > 0:
                    if abs(difference[1]) < difference[0]:
                        self.stabilizePlayer(0)
                    elif difference[1] > 0:
                        self.stabilizePlayer(1)
                    else:
                        self.stabilizePlayer(3)
                else:
                    if abs(difference[1]) < abs(difference[0]):
                        self.stabilizePlayer(2)
                    elif difference[1] > 0:
                        self.stabilizePlayer(1)
                    else:
                        self.stabilizePlayer(3)
                    
    def stabilizePlayer(self, side):
            if side == 0: #left
                self.player.stabilize((self.x - self.sprite.width / 2 - self.player.circleMaskRadius, self.y), 90)
            elif side == 1: #top
                self.player.stabilize((self.x, self.y - self.sprite.height / 2 - self.player.circleMaskRadius), 0)
            elif side == 2: #right
                self.player.stabilize((self.x + self.sprite.width / 2 + self.player.circleMaskRadius, self.y), 270)
            else: #bottom
                self.player.stabilize((self.x, self.y + self.sprite.height / 2 + self.player.circleMaskRadius), 180)