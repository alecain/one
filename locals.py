import event

ALL = "ALL"

PLAYER_SIZE = 30
MOVEMENT_INC = 5

loop = None
def get_loop():
    global loop
    if loop is None:
        loop = event.EventLoop()
    return loop
