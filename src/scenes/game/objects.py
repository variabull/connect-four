# Game Players
# Contributors: Jacob Nettleship
# Date edited: 04/01/22
"""
File defining player objects and controllers
"""

import pygame


class Board:

    def __init__(self, scene_manager):
        self.board = []
        self.width = scene_manager.screen.get_width() / 1.5
        self.height = scene_manager.screen.get_height()
        self.x = (scene_manager.screen.get_width() / 2) - (self.width / 2)
        self.y = (scene_manager.screen.get_height() / 2) - (self.height / 2)

    def render(self, scene_manager):
        pygame.draw.rect(scene_manager.screen, (0, 0, 190), (self.x, self.y, self.width, self.height))


class Player:
    """
    Class that defines a player object
    """

    def __init__(self, scene_manager, controls, colour, x, y):
        width = scene_manager.screen.get_width()
        self.width = width / 15
        self.height = width / 10
        self.controls = controls
        self.x = x
        self.y = y
        self.colour = colour

    def update(self, data):
        pass

    def render(self, scene_manager):
        pygame.draw.circle(scene_manager.screen, self.colour, (self.x, self.y), 40, 0)
