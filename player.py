import pygame
from pygame.sprite import DirtySprite

from locals import *

from event import (
    HandlesEvents,
    )

from keyboard import (
    MovementEvent
    )

from mouse import (
    MouseEvent
    )

from drawable import Drawable

# represents a player...not necessarily ours though!
class Player(HandlesEvents, Drawable):
    def __init__(self, character, color, location):
        Drawable.__init__(self, character, color, location, PLAYER_SIZE)
        HandlesEvents.__init__(self, [])
        self.events.append(MovementEvent)

    def toggle(self):
        if self.string == "0":
            self.string = "1"
        else:
            self.string = "0"

    def shoot(self):
        self.toggle()

    def handle_event(self, event):
        if isinstance(event, MovementEvent):
            self.location = (self.location[0] + event.dx, self.location[1] + event.dy)
            self.regen_sprite()

class HumanPlayer(Player):
    def __init__(self, character, color, location):
        super(HumanPlayer, self).__init__(character, color, location)
        self.events.append(MouseEvent)

    def handle_event(self, event):
        super(HumanPlayer, self).handle_event(event)

        if isinstance(event, MouseEvent):
            loop = get_loop()
            print event
            loop.enqueue(ProjectileCreationEvent(self.location, event.payload.pos, self))

class AIPlayer(Player):
    def __init__(self, character, color, location):
        super(AIPlayer, self).__init__(character, color, location)
