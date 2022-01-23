# Scenes
# Contributors: Jacob Nettleship
# Date edited: 23/01/22
"""
Init file for scenes package containing SceneManager
"""

from .game import GameScene
from .menu import MenuScene


class SceneManager:
    """
    Objects created from the scene manager are responsible for keeping track of the current scene,
    global data, initialising, updating and rendering scenes
    """

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.scenes = {
            'game': GameScene,
            'menu': MenuScene
        }
        self.data = {}
        self.scene = None

    def init(self, scene):
        """
        This tells the current scene to load all assets and data and reset everything to initial places
        """

        self.scene = self.scenes[scene](self)

    def handle_event(self, event):
        """
        When an event occurs this is used to pass it to the current scene to handle
        """

        self.scene.handle_event(event)

    def update(self):
        """
        This tells the current scene to update itself
        """

        self.scene.update()

    def render(self):
        """
        This tells the current scene to render itself on the screen. How this is done is specified by the scene object
        """

        self.scene.render()
