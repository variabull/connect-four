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

    def __init__(self, manager):
        self.board = []
        for x in range(0, 7):
            self.board.append([])
            for y in range(0, 6):
                self.board[x].append('empty')

        self.width = manager.screen.get_width() / 1.5
        self.height = manager.screen.get_height() - 150
        self.x = (manager.screen.get_width() / 2) - (self.width / 2)
        self.y = manager.screen.get_height() - self.height
        self.radius = manager.screen.get_width() / 30

    def update(self, manager):
        self.checkfour('yellow')

    def checkfour(self, colour):
        pass

    def render(self, manager):
        pygame.draw.rect(manager.screen, (0, 0, 190), (self.x, self.y, self.width, self.height), 0, 10)
        for x in range(0, 7):
            for y in range(0, 6):
                pygame.draw.circle(manager.screen, COLOURS[self.board[x][y]],
                                   (((self.width / 7) * (x + 0.5)) + self.x,
                                    ((self.height / 6) * (y + 0.5)) + self.y), self.radius)


class Player:
    """
    Class that defines a player object
    """

    def __init__(self, manager, controls, colour, x, square_size):
        self.controls = controls
        self.column = 0
        self.square_size = square_size
        self.colour = colour
        self.radius = manager.screen.get_width() / 30
        self.x = x
        self.y = (manager.screen.get_height() - manager.board.height) / 2

    def update(self, manager):
        data = manager.data
        if data['turn'] == self.colour and 'event_key' in data.keys():
            if data['event_key'] == self.controls[0] and self.column > 0:
                self.x -= self.square_size[0]
                self.column -= 1
                data.pop('event_key')
            elif data['event_key'] == self.controls[1] and self.column < 6:
                self.x += self.square_size[0]
                self.column += 1
                data.pop('event_key')
            elif data['event_key'] == self.controls[2]:
                if self.colour == 'red':
                    data['turn'] = 'yellow'
                else:
                    data['turn'] = 'red'

    def render(self, manager):
        pygame.draw.circle(manager.screen, COLOURS[self.colour], (self.x, self.y), self.radius)
