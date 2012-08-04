from event import PygameHandler
from pygame.locals import *
from locals import *

class MovementEvent(TargetedEvent):
    def __init__(self, target, dx, dy):
       super(MovementEvent,self).__init__(None,target)
       self.dx=dx
       self.dy=dy

class WASDHandler(PygameHandler):
    def __init__(self, player):
        super(KeyboardHandler, self).__init__(KEYDOWN)
        self.player = player
    def handle_event(self, event):
        loop = get_loop()
        if event.pygame_event.key == K_w:
            #print 'w'
            loop.enqueue(MovementEvent(player, 0 , -1))
        if event.pygame_event.key == K_a:
            #print 'a'
            loop.enqueue(MovementEvent(player, -1 , 0))
        if event.pygame_event.key == K_s:
            #print 's'
            loop.enqueue(MovementEvent(player, 0 , 1))
        if event.pygame_event.key == K_d:
            #print 'd'
            loop.enqueue(MovementEvent(player, 1 , 0))
