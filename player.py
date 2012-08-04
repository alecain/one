import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.sprite import DirtySprite

from locals import *

from event import (
    HandlesEvents,
    )

from keyboard import (
    MovementEvent
    )

# represents a player...not necessarily ours though!
class Player(HandlesEvents, DirtySprite):
    def __init__(self, character, color, location):
        HandlesEvents.__init__(self, [])
        DirtySprite.__init__(self)
        self.events.append(MovementEvent)

        self.character = character
        self.color = color
        self.font = Font(pygame.font.get_default_font(), PLAYER_SIZE)
        self.location = location

        self.regen_sprite()

    def _gen_surface(self):
        return self.font.render(self.character, True, self.color)

    def regen_sprite(self):
        self.image = self._gen_surface()
        self.rect = Rect(self.location, self.image.get_size())
        self.dirty = 1

    def toggle(self):
        if self.character == "0":
            self.character = "1"
        else:
            self.character = "0"

    def shoot(self):
        self.toggle()

    def handle_event(self, event):
        if isinstance(event, MovementEvent):
            self.location = (self.location[0] + event.dx, self.location[1] + event.dy)
            self.regen_sprite()

class HumanPlayer(Player):
    def __init__(self, character, color, location):
        super(HumanPlayer, self).__init__(character, color, location)

class AIPlayer(Player):
    def __init__(self, character, color, location):
        super(AIPlayer, self).__init__(character, color, location)
