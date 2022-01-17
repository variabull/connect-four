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

    def __init__(self, scene_manager):
        screen = scene_manager.screen
        self.data = {'turn': 'red'}
        self.board = Board(scene_manager)

        # Creates a local player with WASD controls
        self.l_player = Player(scene_manager, [K_a, K_d], 'red',
                                    ((self.board.width / 7) * 0.5) + self.board.x, 52.5)
        # Creates local player with arrow key controls
        self.r_player = Player(scene_manager, [K_LEFT, K_RIGHT], 'yellow',
                                    ((self.board.width / 7) * 0.5) + self.board.x, 52.5)

    def update(self, scene_manager):
        self.l_player.update(self.data)
        self.r_player.update(self.data)

    def render(self, scene_manager):
        self.l_player.render(scene_manager)
        self.r_player.render(scene_manager)
        self.board.render(scene_manager)
