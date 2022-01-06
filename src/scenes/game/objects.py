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
        self.img = pygame.image.load('assets/board.png').convert_alpha()
        self.x = scene_manager.screen.get_width() / 2
        self.y = 0

    def render(self, scene_manager):
        scene_manager.screen.blit(self.img, (self.x, self.y))


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
