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
            #print 'w'
            loop.enqueue(MovementEvent(player, 0 , -1))
        if event.payload.key == K_a:
            #print 'a'
            loop.enqueue(MovementEvent(player, -1 , 0))
        if event.payload.key == K_s:
            #print 's'
            loop.enqueue(MovementEvent(player, 0 , 1))
        if event.payload.key == K_d:
            #print 'd'
            loop.enqueue(MovementEvent(player, 1 , 0))
