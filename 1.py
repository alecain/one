import pygame
from event import (
    Event,
    EventLoop,
    PrintHandler,
    QuitHandler
    )

def main():
    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("1")

    loop = EventLoop()
    loop.add_object(PrintHandler())
    loop.add_object(QuitHandler())
    while True:
        loop.tick()

if __name__ == '__main__':
    main()
