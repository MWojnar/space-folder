from World import World
import pygame
import random

pygame.mixer.pre_init(44100, -16, 20, 2048)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption("In Space No One Can Hear You Jump")
pygame.mouse.set_visible(False)
random.seed()
width = 960
height = 540
windowSize = (width, height)
screen = pygame.display.set_mode(windowSize)
world = World(screen, width, height)
world.run()