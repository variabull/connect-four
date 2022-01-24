# Game Scene
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
File containing instructions on the game scene
"""

import time
import pygame
from random import choice
from pygame.locals import *
from globals.constants import *
from globals.ui_elements import Text
from .objects import Board, Player


class GameScene:
    """
    Objects created from the game scene class are responsible for loading game assets,
    updating game objects, detecting collisions, rendering and loading and storing game data
    """

    def __init__(self, manager):
        self.manager = manager
        self.screen = manager.screen
        self.data = {
            'turn': 'red',
            'won': False,
            'names': self.manager.data['player_names'],
            'move': 1
        }
        self.font = pygame.font.Font(None, self.screen.get_width() // FONT_SIZE_FACTOR_2)

        self.player1_text = Text(self.font, 0, self.screen.get_height() / 10,
                                 self.screen.get_width() / 8, self.screen.get_width() / 20, self.data['names'][0],
                                 'red', 'white', 0)
        self.player2_text = Text(self.font, self.screen.get_width(), self.screen.get_height() / 10,
                                 self.screen.get_width() / 8, self.screen.get_width() / 20, self.data['names'][1],
                                 'yellow', 'grey', 1)

        # Specify time 15 seconds from now and create element to display a count down
        self.move_end = time.time() + 15
        self.timer = Text(self.font, 0, self.screen.get_height() / 10 + self.screen.get_width() / 20,
                          self.screen.get_width() / 8, self.screen.get_width() / 20, '15', 'grey', 'white', 0)

        self.move = Text(self.font, self.screen.get_width(),
                         self.screen.get_height() / 10 + self.screen.get_width() / 20,
                         self.screen.get_width() / 8, self.screen.get_width() / 20, '15', 'grey', 'white', 1)

        self.board = Board(self.manager)

        # Creates player with arrow key controls
        self.player = Player(self, [K_LEFT, K_RIGHT, K_DOWN],
                             ((self.board.width / 7) * 0.5) + self.board.x,
                             (self.board.width / 7, self.board.height / 6))

        self.victory_banner = Text(self.font, self.board.x,
                                   (self.screen.get_height() - self.board.height) / 2, self.board.width,
                                   self.screen.get_width() / (TOKEN_RADIUS_FACTOR * 1/2), 'stalemate', 'grey', 'white', 0)

    def handle_event(self, event):
        if not self.data['won']:
            self.player.handle_event(self, event)

    def update(self):
        if not self.data['won'] and not self.data['move'] == 22:
            if time.time() >= self.move_end:
                self.board.play(self, self.player.column, self.player)
            else:
                if time.time() >= self.move_end - 5:
                    self.timer.bg_colour = 'red'
                else:
                    self.timer.bg_colour = 'grey'
                self.timer.change_text(str(int((self.move_end - time.time()) * 10) / 10))
                self.move.change_text(f"Move {self.data['move']}")
        else:
            if self.data['won']:
                self.victory_banner.bg_colour = self.data['turn']
                self.victory_banner.text_colour = {'red': 'white', 'yellow': 'grey'}[self.data['turn']]
                self.victory_banner.change_text(self.data['turn'] + ' wins')

    def render(self):
        if not self.data['won'] and not self.data['move'] == 22:
            self.player.render(self)
        else:
            self.victory_banner.render(self)
        self.board.render(self)
        self.player1_text.render(self)
        self.player2_text.render(self)
        self.timer.render(self)
        self.move.render(self)
