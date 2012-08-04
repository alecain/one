import pygame
import pygame.key

from event import (
    Event,
    EventLoop,
    PrintHandler,
    QuitHandler
    )
from keyboard import WASDHandler

import player

from locals import *

def main():

    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("1")
    pygame.key.set_repeat(50, 50)

    p = player.HumanPlayer("0", (255, 0, 0), (0, 0))

    loop = get_loop()
    loop.add_object(PrintHandler())
    loop.add_object(QuitHandler())
    loop.add_object(WASDHandler(p))
    loop.add_object(p)

    while True:
        loop.tick()

if __name__ == '__main__':
    main()
