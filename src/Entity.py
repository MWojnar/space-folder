import Utility
class Entity(object):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
        self.frame = 0
        self.animationSpeedTimer = 0
        self.world = world
        self.sprite = sprite
        self.x = x
        self.y = y
        self.vSpeed = 0
        self.hSpeed = 0
        self.rotationSpeed = 0
        self.depth = depth
        self.rotation = 0
        self.animating = True
        self.isRectMask = False
        self.circleMaskRadius = 0
        self.circleMaskCenter = (0, 0)
        self.rectMask = (0, 0, 0, 0)
        
    def update(self):
        if self.animating:
            self.incrementFrame()
        self.move()
    
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation)
        
    def incrementFrame(self):
        if self.sprite != None and self.sprite.animationSpeed != 0:
            self.animationSpeedTimer += self.sprite.animationSpeed / self.world.FPS
            if self.animationSpeedTimer >= 1:
                self.frame += 1
                self.animationSpeedTimer = 0
            if self.frame >= self.sprite.frameCount:
                self.frame = 0
                self.animationEnd()
                
    def isColliding(self, entity):
        if not self.isRectMask and not entity.isRectMask:
            return (Utility.getDistance((self.x + self.circleMaskCenter[0], self.y + self.circleMaskCenter[1]),
                                       (entity.x + entity.circleMaskCenter[0], entity.y + entity.circleMaskCenter[1])) <
                                       self.circleMaskRadius + entity.circleMaskRadius)
        elif self.isRectMask and entity.isRectMask:
            rect1 = (self.x + self.rectMask[0], self.y + self.rectMask[1], self.x + self.rectMask[0] + self.rectMask[2], self.y + self.rectMask[1] + self.rectMask[3])
            rect2 = (entity.x + entity.rectMask[0], entity.y + entity.rectMask[1], entity.x + entity.rectMask[0] + entity.rectMask[2], entity.y + entity.rectMask[1] + entity.rectMask[3])
            return Utility.rectsColliding(rect1, rect2)
        else:
            rect = []
            circle = []
            if self.isRectMask and not entity.isRectMask:
                rect = (self.x + self.rectMask[0], self.y + self.rectMask[1], self.x + self.rectMask[0] + self.rectMask[2], self.y + self.rectMask[1] + self.rectMask[3])
                circle = ((entity.x + entity.circleMaskCenter[0], entity.y + entity.circleMaskCenter[1]), entity.circleMaskRadius)
            else:
                rect = (entity.x + entity.rectMask[0], entity.y + entity.rectMask[1], entity.x + entity.rectMask[0] + entity.rectMask[2], entity.y + entity.rectMask[1] + entity.rectMask[3])
                circle = ((self.x + self.circleMaskCenter[0], self.y + self.circleMaskCenter[1]), self.circleMaskRadius)
            return Utility.rectCircleColliding(rect, circle)
    
    def animationEnd(self):
        pass
    
    def move(self):
        self.x += self.hSpeed
        self.y += self.vSpeed
        self.rotation += self.rotationSpeed