import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.sprite import Sprite

from locals import *

from event import (
    HandlesEvents,
    )

# represents a player...not necessarily ours though!
class Player(HandlesEvents, Sprite):
    def __init__(self, character, color, location):
        HandlesEvents.__init__(self, [])
        Sprite.__init__(self)

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

    def toggle(self):
        if self.character == "0":
            self.character = "1"
        else:
            self.character = "0"

    def shoot(self):
        self.toggle()

class HumanPlayer(Player):
    def __init__(self, character, color, location):
        super(HumanPlayer, self).__init__(character, color, location)

class AIPlayer(Player):
    def __init__(self, character, color, location):
        super(AIPlayer, self).__init__(character, color, location)
