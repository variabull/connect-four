# Game Scene
# Contributors: Jacob Nettleship
# Date edited: 04/01/22
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
        self.data = {'turn': 'red'}
        self.board = Board(self.manager)

        # Creates a local player with WASD controls
        self.l_player = Player(self, [K_a, K_d, K_s], 'red',
                               ((self.board.width/7) * 0.5) + self.board.x,
                               (self.board.width/7, self.board.height/6))

        # Creates local player with arrow key controls
        self.r_player = Player(self, [K_LEFT, K_RIGHT, K_DOWN], 'yellow',
                               ((self.board.width/7) * 0.5) + self.board.x,
                               (self.board.width/7, self.board.height/6))

    def update(self):
        self.l_player.update(self)
        self.r_player.update(self)
        self.board.update(self)

    def render(self):
        self.l_player.render(self)
        self.r_player.render(self)
        self.board.render(self)
