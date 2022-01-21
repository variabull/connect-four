# Game Players
# Contributors: Jacob Nettleship
# Date edited: 21/01/22
"""
File defining player objects and controllers
"""

import pygame

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

    def play(self, manager, col):
        colour = manager.data['turn']
        for i in range(len(self.board[col]) - 1, -1, -1):
            if self.board[col][i] == 'empty':
                self.board[col][i] = colour

                if colour == 'red':
                    manager.data['turn'] = 'yellow'
                else:
                    manager.data['turn'] = 'red'
                self.check_four((col, i), colour)
                break

    def check_four(self, coords, colour):
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

    def __init__(self, manager, controls, x, square_size):
        self.controls = controls
        self.column = 0
        self.square_size = square_size
        self.radius = manager.screen.get_width() / 30
        self.x = x
        self.y = (manager.screen.get_height() - manager.board.height) / 2

    def update(self, manager):
        data = manager.data
        if 'event_key' in data.keys():
            if data['event_key'] == self.controls[0] and self.column > 0:
                self.x -= self.square_size[0]
                self.column -= 1
                data.pop('event_key')
            elif data['event_key'] == self.controls[1] and self.column < 6:
                self.x += self.square_size[0]
                self.column += 1
                data.pop('event_key')
            elif data['event_key'] == self.controls[2]:
                manager.board.play(manager, self.column)
                data.pop('event_key')

    def render(self, manager):
        pygame.draw.circle(manager.screen, COLOURS[manager.data['turn']], (self.x, self.y), self.radius)
