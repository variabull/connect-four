# Mountain Rescue
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
Main file that is run when app is opened
"""

import pygame, sys
from pygame.locals import *
from globals.constants import *
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
        else:
            manager.scene.handle_event(event)

    # Update the current scene's data with the keys being pressed
    manager.scene.data['pressed_keys'] = pygame.key.get_pressed()

    screen.fill(COLOURS['grey'])
    manager.update()
    manager.render()

    pygame.display.update()
