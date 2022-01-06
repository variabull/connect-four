# Scenes
# Contributors: Jacob Nettleship
# Date edited: 04/01/22
"""
Init file for scenes package containing SceneManager
"""

from .game import GameScene


class SceneManager:
    """
    Objects created from the scene manager are responsible for keeping track of the current scene,
    global data, initialising, updating and rendering scenes
    """

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.scenes = {
            'game': GameScene
        }
        self.data = {}

    def init(self, scene_manager, scene):
        """
        This tells the current scene to load all assets and data and reset everything to intial places
        """

        self.scene = self.scenes[scene](scene_manager)

    def update(self, scene_manager):
        """
        This tells the current scene to update itself
        """

        self.scene.update(scene_manager)

    def render(self, scene_manager):
        """
        This tells the current scene to render itself on the screen. How this is done is specified by the scene object
        """

        self.scene.render(scene_manager)
