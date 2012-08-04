import pygame
import math
from pygame.sprite import DirtySprite

from locals import *

import random

from event import (
    HandlesEvents,
    UpdateEvent,
    PygameHandler
    )

from keyboard import (
    MovementEvent
    )

from mouse import (
    MouseEvent,
    )

from projectiles import (
    ProjectileCreationEvent
    )

from drawable import Drawable

# represents a player...not necessarily ours though!
class Player(HandlesEvents, Drawable):
    def __init__(self, character, color, location):
        Drawable.__init__(self, character, color, location, PLAYER_SIZE)
        HandlesEvents.__init__(self, [])
        self.events.append(MovementEvent)

    def toggle(self):
        if self.string == "0":
            self.string = "1"
        else:
            self.string = "0"

    def shoot(self):
        self.toggle()

    def handle_event(self, event):
        if isinstance(event, MovementEvent):
            self.location = (self.location[0] + event.dx, self.location[1] + event.dy)
            self.regen_sprite()

class HumanPlayer(Player):
    def __init__(self, character, color, location):
        super(HumanPlayer, self).__init__(character, color, location)
        self.events.append(MouseEvent)

    def handle_event(self, event):
        if isinstance(event, MouseEvent):
            loop = get_loop()
            loop.enqueue(ProjectileCreationEvent(self.location, event.payload, self))
            self.shoot()
            self.regen_sprite()
        super(HumanPlayer, self).handle_event(event)

class AIPlayer(Player):
    def __init__(self, character, color, location, player, mass = 10, maxvel = 4):
        super(AIPlayer, self).__init__(character, color, location)
        self.events.append(UpdateEvent)
        self.player = player
        self.vx=0
        self.vy=0
        self.mass= float(mass * (random.random()+1))
        self.maxvel= float(maxvel)
        self.force =0
        self.angle=0

    def calculate_force(self, angle, distance):
        self.force = max(.1, min(1/distance, 10))
        self.angle = angle

    def handle_event(self, event):
        if isinstance(event,UpdateEvent):

            #calculate distance and angle to player
            angle = math.atan2(self.player.location[1]-self.location[1],self.player.location[0]-self.location[0])
            distance = math.sqrt(math.pow(self.location[1]-self.player.location[1],2)+math.pow(self.location[0]-self.player.location[0],2))

            #make moves
            self.calculate_force(angle,distance)
            self.vx = self.vx + self.force/self.mass * UPDATE_TIME * math.cos(self.angle)
            if self.vx > self.maxvel:
               self.vx = self.maxvel
            if self.vx < -self.maxvel:
               self.vx = -self.maxvel
            self.vy = self.vy + self.force/self.mass * UPDATE_TIME * math.sin(self.angle)
            if self.vy > self.maxvel:
               self.vy = self.maxvel
            if self.vy < -self.maxvel:
               self.vy = -self.maxvel

            self.location = (self.vx+self.location[0], self.vy+self.location[1])

            self.regen_sprite()

        super(AIPlayer, self).handle_event(event)

class SpawnHandler(PygameHandler):
    def __init__(self, player):
        super(SpawnHandler, self).__init__(SPAWNEVENT)
        self.player = player
    def handle_event(self, event):
        loop = get_loop()
        for i in range(1, random.randint(1,5)):
            e = AIPlayer("1", (0,0,255), (random.randint(1,RESX),random.randint(1,RESY)), self.player)
            loop.add_object(e, "enemy")
