import pygame
import os.path
from sys import exit
from Entity import Entity
from AssetLoader import AssetLoader
from Background import Background
from LevelLoader import LevelLoader
from Button import Button
from Victory import Victory
from Cursor import Cursor
import webbrowser

class World(object):
    clock = pygame.time.Clock()
    FPS = 60
    entityList = []
    running = True
    mainSurface = None
    camPos = [0, 0]

    def __init__(self, mainSurface, width, height):
        self.roomWidth = width
        self.roomHeight = height
        self.screenWidth = width
        self.screenHeight = height
        self.assetLoader = AssetLoader(self)
        self.mainSurface = mainSurface
        self.background = Background()
        self.level = 1
        self.cursor = Cursor(self)
        self.loadMenu()
        self.events = []
        self.fullscreen = False
        self.alreadyClicked = False
        pygame.mixer.music.play(-1)
        
    def loadCurrentLevel(self):
        self.loadLevel("Level" + str(self.level) + ".txt")
        
    def loadLevel(self, name):
        self.entityList.clear()
        self.addEntity(self.cursor)
        self.cursor.visible = True
        levelTest = LevelLoader(self, name, self.cursor)
        for object in levelTest.loadLevel():
            self.addEntity(object)
            
    def nextLevel(self):
        self.level += 1
        if (os.path.isfile("Level" + str(self.level) + ".txt")):
            self.loadCurrentLevel()
        else:
            self.loadVictory()
            
    def loadMenu(self):
        self.entityList.clear()
        self.addEntity(self.cursor)
        self.cursor.visible = True
        self.level = 1
        tutorial = Entity(self, self.screenWidth / 2, self.screenHeight / 2, self.assetLoader.tutorial)
        self.addEntity(tutorial)
        wojWorks = Entity(self, self.screenWidth / 2, self.assetLoader.wojWorks.height / 2 - 20, self.assetLoader.wojWorks)
        self.addEntity(wojWorks)
        title = Entity(self, self.screenWidth / 2, self.screenHeight / 4 + 52, self.assetLoader.title)
        self.addEntity(title)
        startButton = Button(self, self.screenWidth / 2, self.screenHeight / 2 + 48, self.assetLoader.start, self.assetLoader.startSelected, self.start, self.cursor)
        self.addEntity(startButton)
        quitButton = Button(self, self.screenWidth / 2, self.screenHeight * 3 / 4, self.assetLoader.quit, self.assetLoader.quitSelected, exit, self.cursor)
        self.addEntity(quitButton)
        
    def start(self):
        self.level = 1
        self.loadCurrentLevel()
        
    def loadVictory(self):
        self.entityList.clear()
        self.addEntity(self.cursor)
        self.cursor.visible = True
        victory = Victory(self, self.screenWidth / 2, self.screenHeight / 2, self.assetLoader.victory)
        self.addEntity(victory)
        
    def dribbleURL(self):
        webbrowser.open("www.wojworks.com/dribble/")
        
    def run(self):
        while self.running:
            self.update()
            self.render()
            
    def update(self):
        self.events = pygame.event.get()
        self.alreadyClicked = False
        for event in self.events:
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F4:
                if self.fullscreen:
                    self.mainSurface = pygame.display.set_mode((960, 540))
                    self.fullscreen = False
                else:
                    self.mainSurface = pygame.display.set_mode((960, 540), pygame.FULLSCREEN)
                    self.fullscreen = True
        self.clock.tick(self.FPS)
        self.buttonState = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        self.mousePos = (pos[0] + self.camPos[0], pos[1] + self.camPos[1])
        for entity in self.entityList:
            entity.update()
    
    def render(self):
        self.mainSurface.fill((255, 255, 255))
        self.background.draw(self.mainSurface, self.assetLoader.bgSpace)
        self.assetLoader.bgEarth.draw(self.mainSurface, self.roomWidth / 2, self.roomHeight / 2, 0)
        for entity in self.entityList:
            entity.draw(self.mainSurface)
        pygame.display.flip()
        
            
    def addEntity(self, entity):
        found = False
        for i in range(len(self.entityList)):
            if entity.depth < self.entityList[i].depth:
                self.entityList.insert(i, entity)
                found = True
                break
        if not found:
            self.entityList.append(entity)
            
    def removeEntity(self, entity):
        try:
            self.entityList.remove(entity)
        except:
            print("Error, trying to remove entity that does not exist!")
            
    def updateMousePos(self, pos):
        pygame.mouse.set_pos(pos)
        self.mousePos = pos