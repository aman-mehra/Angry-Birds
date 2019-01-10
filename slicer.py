import pygame

class blocks(object):
    def wooden_block(self):
        img=pygame.image.load("wood.png")
        img=pygame.transform.scale(img,(232,208))
        img=img.subsurface(0,0,42,42)
        return img
