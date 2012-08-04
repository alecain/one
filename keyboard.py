from event import (
    PygameHandler,
    TargettedEvent,
    )

from pygame.locals import *
from locals import *

class MovementEvent(TargettedEvent):
    def __init__(self, target, dx, dy):
       super(MovementEvent,self).__init__(None,target)
       self.dx=dx
       self.dy=dy

class WASDHandler(PygameHandler):
    def __init__(self, player):
        super(WASDHandler, self).__init__(KEYDOWN)
        self.player = player
    def handle_event(self, event):
        loop = get_loop()
        if event.payload.key == K_w:
            loop.enqueue(MovementEvent(self.player, 0 , -MOVEMENT_INC))
        elif event.payload.key == K_a:
            loop.enqueue(MovementEvent(self.player, -MOVEMENT_INC , 0))
        elif event.payload.key == K_s:
            loop.enqueue(MovementEvent(self.player, 0 , MOVEMENT_INC))
        elif event.payload.key == K_d:
            loop.enqueue(MovementEvent(self.player, MOVEMENT_INC , 0))
