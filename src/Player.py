'''
Created on Aug 31, 2018

@author: Seanzee
'''
import pygame
import math
import Utility
from Entity import Entity

class Player(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0, cursor=None):
        # Can't set the sprite as a default value, as I need before
        # I can access assetLoader
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.spaceguyStand
        else:
            self.sprite = sprite
        self.animationSpeedTimer = 0
        self. frame = 0
        self.world = world
        self.x = x
        self.y = y
        self.depth = depth
        self.isStable = True
        self.stableRotation = 0
        self.angleLimit = 60
        self.maxPower = 10
        self.power = 1
        self.crouching = False
        self.hSpeed = 0
        self.vSpeed = 0
        self.maxSpeed = 5
        self.pullSpeed = 0.1
        self.float = False
        self.floatRotation = 1
        self.circleMaskRadius = self.sprite.width / 4
        self.dying = False
        self.checkpoint = None
        self.checkpointData = (self.x, self.y, self.rotation)
        self.respawning = False
        self.visible = True
        self.mouseOffset = [0, 0]
        self.createdHelmet = False
        self.cursor = cursor
        
    def update(self):
        if self.animating:
            self.incrementFrame()
        if not(self.x > -self.sprite.height and self.x < self.world.roomWidth + self.sprite.height and self.y > -self.sprite.height and self.y < self.world.roomHeight + self.sprite.height):
            self.die()
        
        if not self.dying and not self.respawning:
            if self.isStable:
                if self.world.buttonState[0] and (not self.lastLeftDown or self.crouching):
                    self.sprite = self.world.assetLoader.spaceguyCrouch
                    if not self.crouching:
                        self.cursor.visible = False
                        pygame.event.set_grab(True)
                        pygame.mouse.get_rel()
                        self.mouseOffset[0] = Utility.lengthDirXDegrees(5, self.stableRotation + 90)
                        self.mouseOffset[1] = Utility.lengthDirYDegrees(5, self.stableRotation + 90)
                    offset = pygame.mouse.get_rel()
                    self.mouseOffset[0] += offset[0]
                    self.mouseOffset[1] += offset[1]
                    self.crouching = True
                else:
                    self.cursor.visible = True
                    pygame.event.set_grab(False)
                    if self.crouching:
                        self.crouching = False
                        self.isStable = False
                        self.sprite = self.world.assetLoader.spaceguyJump
                        self.rotation = self.arrowRotation
                        self.hSpeed = Utility.lengthDirXDegrees(self.power / 2, self.rotation + 90)
                        self.vSpeed = Utility.lengthDirYDegrees(self.power / 2, self.rotation + 90)
                        self.world.assetLoader.sndJump.play()
                        self.world.updateMousePos((int(self.x + self.mouseOffset[0] / 2), int(self.y + self.mouseOffset[1] / 2)))
                    else:
                        self.sprite = self.world.assetLoader.spaceguyStand
                self.float = False
                dist = Utility.getDistance((0, 0), self.mouseOffset)
                if dist > 255:
                    self.mouseOffset[0] = self.mouseOffset[0] * 255 / dist
                    self.mouseOffset[1] = self.mouseOffset[1] * 255 / dist
                    dist = 255
                self.arrowRotation = math.degrees(math.atan2(-self.mouseOffset[0], -self.mouseOffset[1]))
                self.arrowRotation = Utility.getRelativeRotation(self.stableRotation, self.arrowRotation)
                if self.arrowRotation > self.stableRotation + self.angleLimit:
                    self.arrowRotation = self.stableRotation + self.angleLimit
                    if dist != 0:
                        self.mouseOffset[0] = Utility.lengthDirXDegrees(dist, self.arrowRotation + 90)
                        self.mouseOffset[1] = Utility.lengthDirYDegrees(dist, self.arrowRotation + 90)
                elif self.arrowRotation < self.stableRotation - self.angleLimit:
                    self.arrowRotation = self.stableRotation - self.angleLimit
                    if dist != 0:
                        self.mouseOffset[0] = Utility.lengthDirXDegrees(dist, self.arrowRotation + 90)
                        self.mouseOffset[1] = Utility.lengthDirYDegrees(dist, self.arrowRotation + 90)
            dist = Utility.getDistance((0, 0), self.mouseOffset)
            self.power = dist // 25 + 1
            if self.power < 1:
                self.power = 1
            if self.power > self.maxPower:
                self.power = self.maxPower
            if self.float:
                self.rotation += self.floatRotation
            self.move()
            for event in self.world.events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.die()
                
        #elif self.frame == 3:
            #create dead head
        self.lastLeftDown = self.world.buttonState[0]
        if self.dying and self.frame == 3 and not self.createdHelmet:
            self.createHelmet()
            self.createdHelmet = True

    def move(self):
        speed = Utility.getDistance((0, 0), (self.hSpeed, self.vSpeed))
        if speed > self.maxSpeed:
            self.hSpeed *= self.maxSpeed / speed
            self.vSpeed *= self.maxSpeed / speed
        self.x += self.hSpeed
        self.y += self.vSpeed
        
        
    def draw(self, surface):
        if self.visible:
            self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation)
            if not self.dying and not self.respawning and self.isStable and self.world.buttonState[0] and self.crouching:
                self.drawArrow(surface)
            
    def drawArrow(self, surface):
        arrowSeg = self.world.assetLoader.arrowSegment
        arrowTip = self.world.assetLoader.arrowTip
        segLen = 10
        for i in range(int(self.power)):
            x = self.x + Utility.lengthDirXDegrees(i * segLen + segLen / 2 + self.sprite.height / 4, self.arrowRotation + 90)
            y = self.y + Utility.lengthDirYDegrees(i * segLen + segLen / 2 + self.sprite.height / 4, self.arrowRotation + 90)
            arrowSeg.draw(surface, x, y, 0, self.arrowRotation)
        x = self.x + Utility.lengthDirXDegrees(self.power * segLen + segLen / 2 + self.sprite.height / 4 + 2, self.arrowRotation + 90)
        y = self.y + Utility.lengthDirYDegrees(self.power * segLen + segLen / 2 + self.sprite.height / 4 + 2, self.arrowRotation + 90)
        arrowTip.draw(surface, x, y, 0, self.arrowRotation)
        
    def pull(self, pullPos):
        if not self.dying and not self.respawning:
            angle = math.atan2(self.x - pullPos[0], self.y - pullPos[1]) + math.pi / 2
            self.hSpeed += Utility.lengthDirX(self.pullSpeed, angle)
            self.vSpeed += Utility.lengthDirY(self.pullSpeed, angle)
            self.startFloat()
        
    def push(self, pullPos):
        if not self.dying and not self.respawning:
            angle = math.atan2(self.x - pullPos[0], self.y - pullPos[1]) + math.pi / 2
            self.hSpeed -= Utility.lengthDirX(self.pullSpeed, angle)
            self.vSpeed -= Utility.lengthDirY(self.pullSpeed, angle)
            self.startFloat()
        
    def startFloat(self):
        self.float = True
        self.sprite = self.world.assetLoader.spaceguyFloat
        
        
    def stabilize(self, pos, angle):
        self.x = pos[0]
        self.y = pos[1]
        self.rotation = angle
        self.stableRotation = angle
        self.sprite = self.world.assetLoader.spaceguyStand
        self.isStable = True
        self.vSpeed = 0
        self.hSpeed = 0
        if self.checkpoint != None:
            self.checkpoint = None
            self.checkpointData = (self.x, self.y, self.rotation)
        self.world.assetLoader.sndLand.play()
        
    def die(self):
        if not self.dying:
            self.dying = True
            self.sprite = self.world.assetLoader.spaceguyDie
            self.vSpeed = 0
            self.hSpeed = 0
            self.world.assetLoader.sndDie.play()
            
    def animationEnd(self):
        super().animationEnd()
        if self.dying:
            self.x = self.checkpointData[0]
            self.y = self.checkpointData[1]
            self.rotation = self.checkpointData[2]
            self.stableRotation = self.checkpointData[2]
            self.sprite = self.world.assetLoader.spaceguyRespawn
            self.frame = 0
            self.respawning = True
            self.dying = False
            self.vSpeed = 0
            self.hSpeed = 0
            self.isStable = True
            self.createdHelmet = False
            if self.checkpoint != None:
                self.checkpoint.untrigger()
                self.checkpoint = None
        elif self.respawning:
            self.respawning = False
            self.sprite = self.world.assetLoader.spaceguyStand
            
    def hitCheckpoint(self, checkpoint):
        self.checkpoint = checkpoint
        
    def createHelmet(self):
        angle = self.rotation + 90
        helmet = Entity(self.world, self.x + Utility.lengthDirXDegrees(self.sprite.height / 4, angle), self.y + Utility.lengthDirYDegrees(self.sprite.height / 4, angle), 
                        self.world.assetLoader.spaceguyDieHead, 0)
        helmet.hSpeed = Utility.lengthDirXDegrees(1, angle)
        helmet.vSpeed = Utility.lengthDirYDegrees(1, angle)
        helmet.rotationSpeed = 1
        helmet.rotation = self.rotation
        self.world.addEntity(helmet)