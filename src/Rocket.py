from Entity import Entity

class Rocket(Entity):

    def __init__(self, world=None, x=0, y=0, sprite=None, depth=-1, player=None):
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.endRocket
        else:
            self.sprite = sprite
        self.player = player
        self.speed = 0
        self.acceleration = 0.1
        self.circleMaskRadius = 16
            
    def update(self):
        super().update()
        if self.sprite == self.world.assetLoader.endRocket and self.isColliding(self.player):
            self.sprite = self.world.assetLoader.endRocketTakeoff
            self.frame = 0
            self.player.visible = False
            self.player.vSpeed = 0
            self.player.hSpeed = 0
            self.world.assetLoader.sndRocket.play()
        if (self.sprite == self.world.assetLoader.endRocketTakeoff):
            self.speed += self.acceleration
        self.y -= self.speed
        if self.y < -300:
            self.world.nextLevel()

        def __init__(self, world=None, x=0, y=0, sprite=None, depth=-1, player=None):
            super().__init__(world, x, y, depth=depth)
            if sprite == None:
                self.sprite = world.assetLoader.endRocket
            else:
                self.sprite = sprite
            self.player = player
            self.speed = 0
            self.acceleration = 0.1
            self.circleMaskRadius = 16
                
        def update(self):
            super().update()
            if self.sprite == self.world.assetLoader.endRocket and self.isColliding(self.player):
                self.sprite = self.world.assetLoader.endRocketTakeoff
                self.frame = 0
                self.player.visible = False
                self.player.vSpeed = 0
                self.player.hSpeed = 0
                self.world.assetLoader.sndRocket.play()
            if (self.sprite == self.world.assetLoader.endRocketTakeoff):
                self.speed += self.acceleration
            self.y -= self.speed
            if self.y < -300:
                self.world.nextLevel()

