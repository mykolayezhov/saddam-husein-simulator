"""

MADE BY ROCKOBILSHIKI corp.

© All rights and patents reserved by ROCKOBILSHIKI corp.® 2024

QR-Code: No

"""

import pygame
from settings import screen
from settings import background_image
from saddam import saddam_h
from rubble import rubble
from settings import icon
from settings import background_image, background_image2, background_animation_count
from helps import help2, help1

pygame.init()

run = True

while run:
    pygame.display.flip()
    pygame.display.set_caption("SADDAM HUSEIN SIMULATOR")
    pygame.display.set_icon(icon)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button = pygame.mouse.get_pressed(num_buttons=3)
            if mouse_button[0] == True:
                mouse_pos = pygame.mouse.get_pos()
                if rubble.check_mouse(mouse_pos):
                    rubble.click_check = True
                    help2.needed = False
        
    screen.fill("white")
    screen.blit(background_image, (0, 150))
    saddam_h.update()
    rubble.update()
    help2.update()
    help1.upgrade()

    
    if saddam_h.in_dip and rubble.is_closed:
        background_animation_count += 10
        if background_animation_count < 255:
            background_image2.set_alpha(background_animation_count)
        screen.blit(background_image2, (0, 150))
    pygame.display.flip()