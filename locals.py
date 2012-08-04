import event

ALL = "ALL"

loop = None
def get_loop():
    global loop
    if loop is None:
        loop = event.EventLoop()
    return loop
