# Leaderboard Scene
# Contributors: Jacob Nettleship
# Date edited: 31/01/22
"""
File containing instructions on the leaderboard scene
"""

import pygame
from globals.constants import *
from globals.leaderboard_helper_functions import load_leaderboard, order_leaderboard
from .objects import BackButton, Table


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
        self.font = pygame.font.Font(None, self.screen.get_width() // FONT_SIZE_FACTOR_2)

        # Button to go back to main menu
        self.back_button = BackButton(self.font, 30, 30 + self.screen.get_width() / 40, self.screen.get_width() / 5,
                                      self.screen.get_width() / 20, 'Back', 'blue', 'white', 0)

        # Table to display data
        self.table = Table(self, self.leaderboard)

    def handle_event(self, event):
        self.back_button.handle_event(self.manager, event)

    def update(self):
        pass

    def render(self):
        self.table.render(self)
        self.back_button.render(self)
