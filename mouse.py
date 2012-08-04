import pygame.mouse
from pygame.locals import *

from locals import *

from event import (
    Event,
    PygameHandler
    )

class MouseEvent(Event):
    def __init__(self, position):
        super(MouseEvent, self).__init__(position)

class MouseHandler(PygameHandler):
    def __init__(self):
        super(MouseHandler, self).__init__(MOUSEBUTTONDOWN)

    def handle_event(self, event):
        loop = get_loop()
        loop.enqueue(MouseEvent(pygame.mouse.get_pos()))
