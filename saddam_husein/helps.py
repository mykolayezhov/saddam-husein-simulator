import pygame
import os
from settings import screen
from saddam import saddam_h

pygame.init()

class Help1():
    def __init__(self) -> None:
        self.image_path = os.path.abspath(__file__ + "/../images/right_arrow.png")
        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(self.image_path), (400, 400))
        self.image.set_alpha(0)
        self.animation_count = 0
        self.needed = True

    def show(self):
        self.animation_count += 15
        self.image.set_alpha(self.animation_count)

    def hide(self):
        self.animation_count -= 15
        if self.animation_count >= 255:
            self.animation_count = 255
        self.image.set_alpha(self.animation_count)
    
    def blit_sprite(self):
        if self.image != None:
            screen.blit(self.image, (200, 60))

    def keys_pressed(self):
        return pygame.key.get_pressed()
    
    def upgrade(self):
        if self.keys_pressed()[pygame.K_RIGHT]:
            self.needed = False
        if self.needed:
            self.show()
        else:
            self.hide()
        self.blit_sprite()
        

class Help2():
    def __init__(self) -> None:
        self.image_path = os.path.abspath(__file__ + "/../images/cursor.png")
        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(self.image_path), (400, 400))
        self.image.set_alpha(0)
        self.animation_count = 0
        self.needed = True

    def show(self):
        self.animation_count += 15
        if self.animation_count >= 255:
            self.animation_count = 255
        self.image.set_alpha(self.animation_count)
    
    def hide(self):
        self.animation_count -= 15
        self.image.set_alpha(self.animation_count)

    def blit_sprite(self):
        if self.image != None:
            screen.blit(self.image, (800, 20))
    
    def update(self):
        if self.needed:
            if saddam_h.in_dip:
                self.show()
        else:
            self.hide()
        self.blit_sprite()

help1 = Help1()
help2 = Help2()

    