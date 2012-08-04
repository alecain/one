import pygame
from pygame import *


from event import (
    Event,
    EventLoop,
    PrintHandler,
    QuitHandler,
    RedrawHandler,
    UpdateHandler
    )
from keyboard import WASDHandler

import player

from locals import *

def main():

    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("1")
    pygame.key.set_repeat(50, 50)

    pygame.time.set_timer(REDRAWEVENT,16)
    pygame.time.set_timer(UPDATEEVENT,30)

    p = player.HumanPlayer("0", (255, 0, 0), (0, 0))
    e = player.AIPlayer("1", (0,0,255), (100,100))

    loop = get_loop()
    loop.add_object(RedrawHandler())
    loop.add_object(UpdateHandler())
    loop.add_object(PrintHandler())
    loop.add_object(QuitHandler())
    loop.add_object(WASDHandler(p))
    loop.add_object(p)
    loop.add_object(e)

    while True:
        loop.tick()

if __name__ == '__main__':
    main()
