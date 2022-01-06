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
        self.data = {}

        # Creates a local player with WASD controls
        self.l_player = Player(scene_manager, [K_a, K_d], (255, 0, 0),
                                    (screen.get_width() * 2/6), screen.get_height()/2)
        # Creates local player with arrow key controls
        self.r_player = Player(scene_manager, [K_LEFT, K_RIGHT], (255, 255, 0),
                                    (screen.get_width() * 4/6), screen.get_height()/2)

        self.board = Board(scene_manager)

    def update(self, scene_manager):
        self.l_player.update(self.data)
        self.r_player.update(self.data)

    def render(self, scene_manager):
        self.l_player.render(scene_manager)
        self.r_player.render(scene_manager)
        self.board.render(scene_manager)
