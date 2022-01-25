# Leaderboard Objects
# Contributors: Jacob Nettleship
# Date edited: 25/01/22
"""
Objects for the menu
"""

from pygame.locals import *
from random import shuffle
from globals.ui_elements import Button


class PlayButton(Button):

    def __init__(self, font, x, y, width, height, text, bg_colour, text_colour, positioning=1/2):
        super().__init__(font, x, y, width, height, text, bg_colour, text_colour, positioning)

    def handle_event(self, scene_manager, manager, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and self.active:
            player_order = [manager.player1.text, manager.player2.text]
            shuffle(player_order)
            scene_manager.data['player_names'] = player_order
            scene_manager.init('game')

    def update(self, manager):
        if len(manager.player1.text) > 0 and len(manager.player2.text) > 0:
            self.active = True
        else:
            self.active = False
