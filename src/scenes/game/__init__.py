# Game Scene
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
File containing instructions on the game scene
"""

import time
import pygame
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
                                 'yellow', 'black', 1)

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

    def handle_event(self, event):
        if not self.data['won']:
            self.player.handle_event(self, event)

    def update(self):
        if not self.data['won']:
            if time.time() >= self.move_end:
                if self.data['turn'] == 'red':
                    self.data['turn'] = 'yellow'
                else:
                    self.data['turn'] = 'red'
                self.move_end = time.time() + 15
            else:
                self.timer.change_text(str(int((self.move_end - time.time()) * 10) / 10))
                self.move.change_text(f"Move {self.data['move']}")
        else:
            pass

    def render(self):
        self.player.render(self)
        self.board.render(self)
        self.player1_text.render(self)
        self.player2_text.render(self)
        self.timer.render(self)
        self.move.render(self)
