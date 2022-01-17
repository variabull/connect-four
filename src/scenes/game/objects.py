# Game Players
# Contributors: Jacob Nettleship
# Date edited: 04/01/22
"""
File defining player objects and controllers
"""

import pygame
from pygame.locals import *

RADIUS = 45
COLOURS = {
    'empty': (70, 70, 70),
    'red': (255, 0, 0),
    'yellow': (255, 255, 0)
}


class Board:

    def __init__(self, scene_manager):
        self.board = []
        for x in range(0, 7):
            self.board.append([])
            for y in range(0, 6):
                self.board[x].append('empty')

        self.width = scene_manager.screen.get_width() / 1.5
        self.height = scene_manager.screen.get_height() - 150
        self.x = (scene_manager.screen.get_width() / 2) - (self.width / 2)
        self.y = scene_manager.screen.get_height() - self.height

    def update(self, scene_manager):
        self.checkfour('yellow')

    def checkfour(self, colour):
        pass

    def render(self, scene_manager):
        pygame.draw.rect(scene_manager.screen, (0, 0, 190), (self.x, self.y, self.width, self.height), 0, 10)
        for x in range(0, 7):
            for y in range(0, 6):
                pygame.draw.circle(scene_manager.screen, COLOURS[self.board[x][y]],
                                   (((self.width / 7) * (x + 0.5)) + self.x,
                                    ((self.height / 6) * (y + 0.5)) + self.y), RADIUS)


class Player:
    """
    Class that defines a player object
    """

    def __init__(self, scene_manager, controls, colour, x, y):
        self.controls = controls
        self.x = x
        self.y = y
        self.colour = colour

    def update(self, data):
        if data['turn'] == self.colour:
            if data['pressed_keys'][self.controls[0]]:
                self.x -= 1
            if data['pressed_keys'][self.controls[1]]:
                self.x += 1

    def render(self, scene_manager):
        pygame.draw.circle(scene_manager.screen, COLOURS[self.colour], (self.x, self.y), RADIUS)
