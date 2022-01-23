# Helper Functions
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
Objects for the menu
"""

from pygame.locals import *
from globals.ui_elements import Button


class PlayButton(Button):

    def __init__(self, font, x, y, width, height, text):
        super().__init__(font, x, y, width, height, text)

    def handle_event(self, scene_manager, manager, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.active:
                scene_manager.data['player_names'] = (manager.player1.text, manager.player2.text)
                scene_manager.init('game')

    def update(self, manager):
        if len(manager.player1.text) > 0 and len(manager.player2.text) > 0:
            self.active = True
        else:
            self.active = False
