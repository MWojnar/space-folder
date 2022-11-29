import json
from pathlib import Path
from AssetLoader import AssetLoader
from Platform import Platform
from Spike import Spike
from Checkpoint import Checkpoint
from PullOrb import PullOrb
from PullOrbTether import PullOrbTether
from Rocket import Rocket
from Bouncy import Bouncy
from Player import Player
from RepelOrb import RepelOrb

class LevelLoader():
    def __init__(self, world, fileName, cursor=None):
        self.world = world
        self.fileName = fileName
        self.levelObjects = []
        self.roomWidth = 960
        self.roomHeight = 540
        self.cursor = cursor
        
    def loadLevel(self):
        levelFile = open(self.fileName, "r")
        jsonString = levelFile.read()
        parsedJson = json.loads(jsonString)

        player = None
        for instance in parsedJson["Level"]:
            for item in instance:
                if item == "Name" and instance[item] == "Player":
                    y = instance["Y"]
                    x = instance["X"]
                    angle = instance["Angle"]
                    player = Player(self.world, x, y, cursor=self.cursor)
                    player.rotation = angle
                    player.stableRotation = angle
                    self.world.addEntity(player)
        for instance in parsedJson["Level"]:
            for item in instance:
                if item == "Room":
                    self.world.roomHeight = instance[item]["Height"]
                    self.world.roomWidth = instance[item]["Width"]
                    
                if item == "Name":
                    y = instance["Y"]
                    x = instance["X"]
                    angle = instance["Angle"]
                    if instance[item] == "Satellite Platform":
                        imageIndex = instance["Image Index"]
                        
                        platform = Platform(self.world, x, y, player=player)
                        platform.frame = imageIndex
                        self.levelObjects.append(platform)
                        
                    elif instance[item] == "Spikes":
                        imageIndex = instance["Image Index"]
                        
                        sprite = None
                        if imageIndex == 0:
                            sprite = self.world.assetLoader.smallSpikes
                        elif imageIndex == 2:
                            sprite = self.world.assetLoader.bigSpikes
                        spike = Spike(self.world, x, y, sprite=sprite, player=player)
                        self.levelObjects.append(spike)
                        
                    elif instance[item] == "Checkpoint":
                        
                        checkpoint = Checkpoint(self.world, x, y, player=player)
                        self.levelObjects.append(checkpoint)
                        
                    elif instance[item] == "Pull Orb":
                        
                        pass
                        pullOrb = PullOrb(self.world, x, y, player=player, cursor=self.cursor)
                        self.levelObjects.append(pullOrb)
                              
                    elif instance[item] == "Attract Tether":
                        
                        pass
                        pullOrbTether = PullOrbTether(self.world, x, y, player=player)
                        self.levelObjects.append(pullOrbTether)
                              
                    elif instance[item] == "End Rocket":
                        
                        rocket = Rocket(self.world, x, y, player=player)
                        self.levelObjects.append(rocket)
                              
                    elif instance[item] == "Earth":
                        pass
                              
                    elif instance[item] == "Bouncy":
                        
                        bouncy = Bouncy(self.world, x, y, player=player)
                        self.levelObjects.append(bouncy)
                    
                    elif instance[item] == "Repel Orb":
                        
                        repelOrb = RepelOrb(self.world, x, y, player=player, cursor=self.cursor)
                        self.levelObjects.append(repelOrb)
                        
        return self.levelObjects
                
        
        
