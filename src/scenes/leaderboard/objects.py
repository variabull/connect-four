# Leaderboard Objects
# Contributors: Jacob Nettleship
# Date edited: 25/01/22
"""
Objects for the menu
"""

import pygame
from pygame.locals import *
from globals.constants import *
from globals.ui_elements import Button, Text


class BackButton(Button):

    def __init__(self, font, x, y, width, height, text, bg_colour, text_colour, positioning=1/2):
        super().__init__(font, x, y, width, height, text, bg_colour, text_colour, positioning)

    def handle_event(self, scene_manager, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and self.active:
            scene_manager.init('menu')


class Table:

    def __init__(self, manager, leaderboard):
        self.leaderboard = leaderboard

        self.width = manager.screen.get_width() / 2.5
        self.height = manager.screen.get_height() / 1.5
        self.x = (manager.screen.get_width() / 2) - (self.width / 2)
        self.y = (manager.screen.get_height() / 2) - (self.height / 2)

    def render(self, manager):
        pygame.draw.rect(manager.screen, COLOURS['blue'], (self.x, self.y, self.width, self.height), 0, 10)
