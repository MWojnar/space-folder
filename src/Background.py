import pygame

class Background():
        
    def draw(self, surface, image):
        windowWidth, windowHeight = surface.get_size()
        imageWidth, imageHeight = image.get_size()
        tileGridWidth = windowWidth / imageWidth
        tileGridHeight = windowHeight / imageHeight
        for y in range (int(tileGridHeight) + 1):
            for x in range(int(tileGridWidth) + 1):
                surface.blit(image, (x * imageWidth, y * imageHeight))
            
        
    