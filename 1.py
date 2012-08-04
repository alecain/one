import pygame
from event import (
    Event,
    EventLoop,
    PrintHandler,
    QuitHandler
    )
from keyboard import KeyboardHandler

import player

from locals import *

def main():
    loop = get_loop()

    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("1")

    loop.add_object(PrintHandler())
    loop.add_object(QuitHandler())
    loop.add_object(WASDHandler(player))
    loop.add_object(player.HumanPlayer("0", (255, 0, 0), (0, 0)))

>>>>>>> player
    while True:
        loop.tick()

if __name__ == '__main__':
    main()
