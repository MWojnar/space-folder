import pygame
import math
from pygame import Surface

class Sprite(object):
    def __init__(self, world, spriteSheet, frameCount=1, animationSpeed=15):
        self.world = world
        self.frameCount = frameCount
        self.animationSpeed = animationSpeed
        size = spriteSheet.get_size()
        self.height = size[1]
        self.width = size[0] / frameCount
        self.frameList = []

        for frame in range(frameCount):
            x = self.width * frame
            self.frameList.append(spriteSheet.subsurface(x, 0, self.width, self.height))

    def draw(self, surface, x, y, frame, angle=0, hScale = -1, vScale = -1):
        tempSurface = self.frameList[frame]
        if hScale != -1 or vScale != -1:
            if hScale == -1:
                hScale = self.width
            if vScale == -1:
                vScale = self.height
            tempSurface = pygame.transform.scale(tempSurface, (int(hScale), int(vScale)))
        size = tempSurface.get_size()
        width = size[0]
        height = size[1]
        if angle == 0:
            surface.blit(tempSurface, (x - width / 2 - self.world.camPos[0], y - height / 2 - self.world.camPos[1]))
        else:
            tempSurface = self.squarify(tempSurface)
            tempSurface = self.rot_center(tempSurface, angle)
            tempSize = tempSurface.get_size()
            surface.blit(tempSurface, (x - tempSize[0] / 2 - self.world.camPos[0], y - tempSize[1] / 2 - self.world.camPos[1]))
            
    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    
    def squarify(self, surface):
        size = surface.get_size()
        if (size[0] == size[1]):
            return surface
        newSize = max(size[0], size[1])
        tempSurface = Surface((newSize, newSize), pygame.SRCALPHA)
        tempSurface.blit(surface, (newSize / 2 - size[0] / 2, newSize / 2 - size[1] / 2))
        return tempSurface