# Game Players
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
File defining player objects and controllers
"""

import time
import pygame
from pygame.locals import *
from globals.constants import *
from globals.ui_elements import Button


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
        self.radius = manager.screen.get_width() / TOKEN_RADIUS_FACTOR

    def play(self, manager, col, player):
        colour = manager.data['turn']
        for i in range(len(self.board[col]) - 1, -1, -1):
            if self.board[col][i] == 'empty':
                self.board[col][i] = colour
                if self.check_win((col, i), colour):
                    manager.data['won'] = True
                elif colour == 'red':
                    manager.data['turn'] = 'yellow'
                else:
                    manager.data['turn'] = 'red'
                    manager.data['move'] += 1
                manager.move_end = time.time() + 15

                if i == 0:
                    empty = manager.board.find_empty(col)
                    player.x += player.tile_size[0] * (empty - player.column)
                    player.column = empty
                return True
        return False

    def find_empty(self, col=0, directions=(1, -1)):
        end = {
            -1: -1,
            1: len(self.board)
        }
        for direction in directions:
            for i in range(col + direction, end[direction], direction):
                if self.board[i][0] == 'empty':
                    return i
        return col

    def check_win(self, coords, colour):
        consecutive = 1
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                for i in range(1, 4):
                    if -1 < coords[0] + (x * i) < 7 and -1 < coords[1] + (y * i) < 6 and self.board[coords[0] + (x * i)][coords[1] + (y * i)] == colour:
                        consecutive += 1
                    else:
                        break
                for i in range(1, 4):
                    if -1 < coords[0] - (x * i) < 7 and -1 < coords[1] - (y * i) < 6 and self.board[coords[0] - (x * i)][coords[1] - (y * i)] == colour:
                        consecutive += 1
                    else:
                        break
                if consecutive > 3:
                    return True
                consecutive = 1
        return False

    def render(self, manager):
        pygame.draw.rect(manager.screen, COLOURS['blue'], (self.x, self.y, self.width, self.height), 0, 10)
        for x in range(0, 7):
            for y in range(0, 6):
                pygame.draw.circle(manager.screen, COLOURS[self.board[x][y]],
                                   (((self.width / 7) * (x + 0.5)) + self.x,
                                    ((self.height / 6) * (y + 0.5)) + self.y), self.radius)


class Player:
    """
    Class that defines a player object
    """

    def __init__(self, manager, controls, x, tile_size):
        self.controls = controls
        self.column = 0
        self.tile_size = tile_size
        self.radius = manager.screen.get_width() / TOKEN_RADIUS_FACTOR
        self.x = x
        self.y = (manager.screen.get_height() - manager.board.height) / 2

    def handle_event(self, manager, event):
        if event.type == KEYDOWN:
            if event.key == self.controls[0] and self.column > 0:
                empty = manager.board.find_empty(self.column, [-1])
                self.x -= self.tile_size[0] * (self.column - empty)
                self.column = empty
            elif event.key == self.controls[1] and self.column < 6:
                empty = manager.board.find_empty(self.column, [1])
                self.x += self.tile_size[0] * (empty - self.column)
                self.column = empty
            elif event.key == self.controls[2]:
                manager.board.play(manager, self.column, self)

    def render(self, manager):
        pygame.draw.circle(manager.screen, COLOURS[manager.data['turn']], (self.x, self.y), self.radius)


class VictoryBanner(Button):

    def __init__(self, font, x, y, width, height, text, bg_colour, text_colour, positioning=1/2):
        super().__init__(font, x, y, width, height, text, bg_colour, text_colour, positioning)

    def handle_event(self, scene_manager, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            scene_manager.init('menu')
