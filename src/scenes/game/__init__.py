# Game Scene
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
File containing instructions on the game scene
"""

from .objects import Board, Player
from pygame.locals import *


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
            'names': self.manager.data['player_names']
        }

        self.board = Board(self.manager)

        # Creates player with arrow key controls
        self.player = Player(self, [K_LEFT, K_RIGHT, K_DOWN],
                             ((self.board.width / 7) * 0.5) + self.board.x,
                             (self.board.width / 7, self.board.height / 6))

    def handle_event(self, event):
        if not self.data['won']:
            self.player.handle_event(self, event)

    def update(self):
        pass

    def render(self):
        self.player.render(self)
        self.board.render(self)
