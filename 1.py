import pygame
from pygame import *


from event import (
    CleanupHandler,
    Event,
    PrintHandler,
    QuitHandler,
    RedrawHandler,
    UpdateHandler
    )

from keyboard import WASDHandler
from mouse import MouseHandler

import player
from player import SpawnHandler
from projectiles import ProjectileCreationHandler

from locals import *

def main():

    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("1")
    pygame.key.set_repeat(50, 50)

    pygame.time.set_timer(REDRAWEVENT,16)
    pygame.time.set_timer(UPDATEEVENT, UPDATE_TIME)
    pygame.time.set_timer(SPAWNEVENT, 2500)

    p = player.HumanPlayer("0", (255, 0, 0), (0, 0))

    loop = get_loop()
    loop.add_object(RedrawHandler())
    loop.add_object(UpdateHandler())
    loop.add_object(SpawnHandler(p))
    loop.add_object(PrintHandler())
    loop.add_object(QuitHandler())
    loop.add_object(WASDHandler(p))
    loop.add_object(CleanupHandler())
    loop.add_object(p, "you")
    loop.add_object(ProjectileCreationHandler())
    loop.add_object(MouseHandler())

    while True:
        loop.tick()

if __name__ == '__main__':
    main()
