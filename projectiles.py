import math

import pygame

from drawable import Drawable
from event import (
    Event,
    HandlesEvents,
    UpdateEvent,
    )
from locals import *

class ProjectileCreationEvent(Event):
    def __init__(self, source, destination, spawner):
        self.angle = math.atan2(destination[1] - source[1], destination[0] - source[0])

        super(ProjectileCreationEvent, self).__init__((source, destination, self.angle, spawner))
        self.spawner = spawner

class ProjectileCreationHandler(HandlesEvents):
    def __init__(self):
        super(ProjectileCreationHandler, self).__init__([ ProjectileCreationEvent ])

    def handle_event(self, event):
        if isinstance(event, ProjectileCreationEvent):
            p = SimpleProjectile(event.spawner.location, event.angle, event.spawner.string)
            loop = get_loop()
            loop.add_object(p, "projectile")

class Projectile(Drawable, HandlesEvents):
    def __init__(self, location, angle, string):
        Drawable.__init__(self, string, (255, 255, 255), location, 12)
        HandlesEvents.__init__(self, [ UpdateEvent ])

        self.location = location
        self.angle = angle

    def handle_event(self, event):
        if isinstance(event, UpdateEvent):
            self.location = (self.location[0] + BULLET_SPEED * UPDATE_TIME * math.cos(self.angle), self.location[1] + BULLET_SPEED * UPDATE_TIME * math.sin(self.angle))
            self.regen_sprite()

class SimpleProjectile(Projectile):
    def __init__(self, location, angle, string):
        super(SimpleProjectile, self).__init__(location, angle, string)

    def handle_event(self, event):
        super(SimpleProjectile, self).handle_event(event)
