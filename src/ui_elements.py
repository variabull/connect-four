# UI elements
# Contributors: Jacob Nettleship
# Date edited: 22/01/22
"""
General elements such as buttons and text boxes that can be used anywhere in the application
"""

import pygame


class TextInput:

    def __init__(self, rect):
        self.rect = rect

    def update(self, manager):
        pass


class Button:

    def __init__(self, font, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = font.render(text, True, (255, 255, 255))
        self.callback = callback

    def update(self, manager):
        data = manager.data
        if 'mouse_click' in data.keys():
            if self.rect.collidepoint(data['mouse_click']):
                self.callback()

    def render(self, manager):
        pygame.draw.rect(manager.screen, (255, 0, 0), self.rect)
        manager.screen.blit(self.text, (self.rect.x + (self.rect.width / 2 - self.text.get_width() / 2),
                                        self.rect.y + (self.rect.height / 2 - self.text.get_height() / 2)))
