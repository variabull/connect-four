# UI elements
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
General elements such as buttons and text boxes that can be used anywhere in the application
"""

import pygame
from pygame.locals import *
from globals.constants import *


class TextInput:

    def __init__(self, font, x, y, width, height, text=''):
        self.font = font
        self.text = text
        self.text_surface = font.render(text, True, COLOURS['white'])

        self.x = x
        self.y = y
        self.width = width
        self.padding = 20

        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.active = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == KEYDOWN and self.active:
            if event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) < MAX_NAME_SIZE:
                self.text += event.unicode

    def update(self):
        self.text_surface = self.font.render(self.text, True, COLOURS['white'])
        self.rect.width = max(self.width, self.text_surface.get_width() + self.padding)
        self.rect.x = self.x - self.rect.width / 2

    def render(self, manager):
        pygame.draw.rect(manager.screen, COLOURS['red'], self.rect)
        manager.screen.blit(self.text_surface, (self.rect.x + (self.rect.width / 2 - self.text_surface.get_width() / 2),
                                            self.rect.y + (self.rect.height / 2 - self.text_surface.get_height() / 2)))


class Button:

    def __init__(self, font, x, y, width, height, text):
        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.text_surface = font.render(text, True, COLOURS['white'])
        self.active = True

    def render(self, manager):
        pygame.draw.rect(manager.screen, COLOURS['red'], self.rect)
        manager.screen.blit(self.text_surface, (self.rect.x + (self.rect.width / 2 - self.text_surface.get_width() / 2),
                                            self.rect.y + (self.rect.height / 2 - self.text_surface.get_height() / 2)))
