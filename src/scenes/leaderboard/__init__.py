# Leaderboard Scene
# Contributors: Jacob Nettleship
# Date edited: 25/01/22
"""
File containing instructions on the leaderboard scene
"""

import pygame
from pygame.locals import *
from globals.constants import *
from globals.leaderboard_helper_functions import load_leaderboard, order_leaderboard
from .objects import Table


class LeaderboardScene:
    """
    Objects created from the game scene class are responsible for loading game assets,
    updating game objects, detecting collisions, rendering and loading and storing game data
    """

    def __init__(self, manager):
        self.manager = manager
        self.screen = manager.screen
        self.data = {}
        self.leaderboard = order_leaderboard(load_leaderboard())
        self.table = Table(self, self.leaderboard)

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self):
        self.table.render(self)
