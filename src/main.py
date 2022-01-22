# Mountain Rescue
# Contributors: Jacob Nettleship
# Date edited: 22/01/22
"""
Main file that is run when app is opened
"""

import pygame, sys
from pygame.locals import *
import scenes

pygame.init()
pygame.display.set_caption('Connect Four')
# This creates the scene manager and registers the screen and clock
manager = scenes.SceneManager(
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN),
    pygame.time.Clock()
)

screen = manager.screen
clock = manager.clock
manager.init('menu')  # Start menu scene

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            manager.scene.data['event_key'] = event.key
        if event.type == MOUSEBUTTONDOWN:
            manager.scene.data['mouse_click'] = event.pos

    # Update the current scene's data with the keys being pressed
    manager.scene.data['pressed_keys'] = pygame.key.get_pressed()

    screen.fill((70, 70, 70))
    manager.update()
    manager.render()

    pygame.display.update()
