import pygame
import pygame.sprite
from event import (
    Event,
    EventLoop,
    PrintHandler,
    QuitHandler
    )

import player

from locals import *

def main():
    loop = get_loop()

    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("1")

    loop.add_object(PrintHandler())
    loop.add_object(QuitHandler())

    p = player.Player("0", (255, 0, 0), (0, 0))
    plane = pygame.sprite.RenderUpdates(p)
    while True:
        loop.tick()
        plane.draw(pygame.display.get_surface())
        pygame.display.flip()

if __name__ == '__main__':
    main()
