# Menu Scene
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
File containing instructions on the menu scene
"""

import pygame
from globals.constants import *
from globals.ui_elements import TextInput, Text
from .objects import PlayButton, LeaderboardButton


class MenuScene:
    """
    Objects created from the game scene class are responsible for loading game assets,
    updating game objects, detecting collisions, rendering and loading and storing game data
    """

    def __init__(self, manager):
        self.manager = manager
        self.screen = manager.screen
        self.data = {}
        self.title_font = pygame.font.Font(None, self.screen.get_width() // TITLE_FONT_SIZE_FACTOR)
        self.font = pygame.font.Font(None, self.screen.get_width() // FONT_SIZE_FACTOR_1)
        self.font_2 = pygame.font.Font(None, self.screen.get_width() // FONT_SIZE_FACTOR_2)

        self.title = Text(self.title_font, self.screen.get_width() / 2, self.screen.get_height() / 6,
                          self.screen.get_width() / 1.5, self.screen.get_width() / 10, 'Connect Four',
                          'grey', 'white')

        self.play_button = PlayButton(self.font, self.screen.get_width() / 2,
                                      self.screen.get_height() / 3, self.screen.get_width() / 5,
                                      self.screen.get_width() / 20, 'Play', 'blue', 'white')

        self.leaderboard_button = LeaderboardButton(self.font_2, self.screen.get_width() / 2,
                                                    self.screen.get_height() / 3 + (self.screen.get_width() / 20) + 20,
                                                    self.screen.get_width() / 5,
                                                    self.screen.get_width() / 20, 'Leaderboard', 'blue', 'white')

        self.player1 = TextInput(self.font, self.screen.get_width() * 1 / 4,
                                 self.screen.get_height() / 3, self.screen.get_width() / 5,
                                 self.screen.get_width() / 20, 'blue', 'white')

        self.player2 = TextInput(self.font, self.screen.get_width() * 3 / 4,
                                 self.screen.get_height() / 3, self.screen.get_width() / 5,
                                 self.screen.get_width() / 20, 'blue', 'white')

    def handle_event(self, event):
        self.play_button.handle_event(self.manager, self, event)
        self.leaderboard_button.handle_event(self.manager, event)
        self.player1.handle_event(event)
        self.player2.handle_event(event)

    def update(self):
        self.play_button.update(self)
        self.player1.update()
        self.player2.update()

    def render(self):
        self.play_button.render(self)
        self.leaderboard_button.render(self)
        self.player1.render(self)
        self.player2.render(self)
        self.title.render(self)
