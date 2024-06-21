import pygame
import os

pygame.init()

screen = pygame.display.set_mode(size= (1488, 950))

background_image = pygame.image.load(os.path.abspath("images/background_first.png"))
background_image2 = pygame.image.load(os.path.abspath("images/background_second.png"))
background_image2.set_alpha(0)
icon = pygame.image.load(os.path.abspath("images/icon.ico"))
background_image = pygame.transform.scale(background_image, (1488, 800))
background_image2 = pygame.transform.scale(background_image2, (1488, 800))

background_animation_count = 0

