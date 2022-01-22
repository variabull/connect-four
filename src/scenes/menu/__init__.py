# Menu Scene
# Contributors: Jacob Nettleship
# Date edited: 22/01/22
"""
File containing instructions on the menu scene
"""

import pygame
from ui_elements import TextInput, Button


class MenuScene:
    """
    Objects created from the game scene class are responsible for loading game assets,
    updating game objects, detecting collisions, rendering and loading and storing game data
    """

    def __init__(self, manager):
        self.manager = manager
        self.screen = manager.screen
        self.data = {}
        self.font = pygame.font.Font(None, self.screen.get_width() // 20)
        self.game_button = Button(self.font, (self.screen.get_width() / 2) - self.screen.get_width() / 10,
                                  self.screen.get_height() / 4, self.screen.get_width() / 5,
                                  self.screen.get_width() / 20, 'Play',
                                  lambda: self.manager.init('game'))

    def update(self):
        self.game_button.update(self)

    def render(self):
        self.game_button.render(self)
