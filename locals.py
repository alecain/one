import event
from pygame.locals import USEREVENT

ALL = "ALL"

PLAYER_SIZE = 30
MOVEMENT_INC = 5
REDRAWEVENT = USEREVENT
UPDATEEVENT = USEREVENT+1


loop = None
def get_loop():
    global loop
    if loop is None:
        loop = event.EventLoop()
    return loop
