import pygame
import os
from settings import screen

pygame.init()

class Saddam():
    def __init__(self) -> None:
        self.x = 20
        self.y = 120
        # self.x = 680
        # self.y = 500
        self.size = (50, 320)
        self.image_path = os.path.abspath(__file__ + "/../images/saddam90.png")
        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(self.image_path), self.size)
        self.image_fin = self.image
        self.rotation = 0
        
        self.animation_count = 0
        
        self.dip_x = 572
        self.reached_dip = False
        self.in_dip = False

    def blit_sprite(self):
        if self.image_fin != None:
            screen.blit(self.image_fin, self.image_fin.get_rect(center = self.image.get_rect(topleft = (self.x, self.y)).center))

    def keys_pressed(self):
        return pygame.key.get_pressed()
    
    def move(self):
        if self.keys_pressed()[pygame.K_RIGHT] and not self.reached_dip:
            self.x += 3

    def check_if_reached_dip(self):
        if self.x >= self.dip_x:
            self.reached_dip = True

    def falling_animation(self):
        self.animation_count += 1
        if self.animation_count <= 100:
            self.x = pygame.math.lerp(572, 680, self.animation_count / 100)
            self.y = pygame.math.lerp(120, 500, self.animation_count / 100)
        elif self.animation_count <= 200:
            self.rotation = pygame.math.lerp(0, 90, (self.animation_count-100) / 100)
            self.image_fin = pygame.transform.rotate(self.image, self.rotation)
            self.x = pygame.math.lerp(680, 845, (self.animation_count-100) / 100)
            self.y = pygame.math.lerp(500, 635, (self.animation_count-100) / 100)
        elif self.animation_count > 200:
            self.in_dip = True

    def update(self):
        self.move()
        self.check_if_reached_dip()
        if self.reached_dip:
            self.falling_animation()
        # pygame.draw.rect(screen, (0, 0, 255), self.image_fin.get_rect())
        self.blit_sprite()


saddam_h = Saddam()