import pygame
from settings import screen
from saddam import saddam_h
import os

pygame.init()

class Rubble():
    def __init__(self) -> None:
        self.x = 844
        self.y = 408
        self.size = (350 ,30)
        self.animation_count = 0
        self.click_check = False
        self.image_path = os.path.abspath(__file__ + "/../images/rubble1.png")
        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(self.image_path), self.size)
        self.is_closed = False

    def blit_sprite(self):
        if self.image != None:
            screen.blit(self.image, (self.x, self.y))

    def animation_rubble(self):
        if saddam_h.in_dip:
            if self.click_check:
                self.animation_count += 1
                if self.animation_count < 100:
                    self.x = pygame.math.lerp(844, 525, self.animation_count / 100)
                    self.y = pygame.math.lerp(408, 408, self.animation_count / 100)
                else:
                    self.is_closed = True

    def check_mouse(self, pos):
        if self.x < pos[0] < self.x + 350:
            if self.y < pos[1] < self.y + 30:
                return True

    def update(self):
        self.blit_sprite()
        self.animation_rubble()
rubble = Rubble()