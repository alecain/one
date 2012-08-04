import event
from pygame.locals import USEREVENT

ALL = "ALL"

PLAYER_SIZE = 30
MOVEMENT_INC = 5
REDRAWEVENT = USEREVENT
UPDATEEVENT = USEREVENT+1
SPAWNEVENT = USEREVENT+2
BULLET_SPEED = 1
UPDATE_TIME = 30
RESX=640
RESY=480

loop = None
def get_loop():
    global loop
    if loop is None:
        loop = event.EventLoop()
    return loop
