# Mountain Rescue
# Contributors: Jacob Nettleship
# Date edited: 03/01/22
"""
Main file that is run when app is opened
"""

import pygame, sys
from pygame.locals import *
import scenes

pygame.init()
pygame.display.set_caption('Connect Four')
# This creates the scene manager and registers the screen and clock
scene_manager = scenes.SceneManager(
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN),
    pygame.time.Clock()
)

screen = scene_manager.screen
clock = scene_manager.clock
scene_manager.init(scene_manager, 'game')  # Start game scene

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # Update the current scene's data with the keys being pressed
    scene_manager.scene.data['pressed_keys'] = pygame.key.get_pressed()

    screen.fill((70, 70, 70))
    scene_manager.update(scene_manager)
    scene_manager.render(scene_manager)

    pygame.display.update()
