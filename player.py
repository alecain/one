import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.sprite import Sprite

from locals import *

from event import (
    HandlesEvents
    )

# represents a player...not necessarily ours though!
class Player(Sprite, HandlesEvents):
    def __init__(self, character, color, location):
        super(Player, self).__init__()

        self.character = character
        self.color = color
        self.font = Font(pygame.font.get_default_font(), PLAYER_SIZE)
        self.location = location

        self.regen_sprite()

    def _gen_surface(self):
        return self.font.render(self.character, True, self.color)

    def regen_sprite(self):
        self.image = self._gen_surface()
        self.rect = Rect(self.image.get_size(), self.location)

class HumanPlayer(Player):
    pass

class AIPlayer(Player):
    pass
