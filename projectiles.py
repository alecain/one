import pygame

from drawable import Drawable
from event import (
    HandlesEvents,
    Event
    )
from locals import *

class ProjectileCreationEvent(Event):
    def __init__(self, source, destination, spawner):
        self.slope = ((destination[0] - source[0]) / (destination[1] - source[1]))
        super(ProjectileCreationEvent, self).__init__((source, destination, self.slope, spawner))
        self.spawner = spawner

class ProjectileCreationHandler(HandlesEvents):
    def __init__(self):
        super(ProjectileCreationHandler, self).__init__([ ProjectileCreationEvent ])

    def handle_event(self, event):
        if isinstance(ProjectileCreationEvent):
            p = SimpleProjectile(event.spawner.location, event.slope, spawner.character)
            loop = get_loop()
            loop.add_object(p)

class Projectile(Drawable, HandlesEvents):
    def __init__(self, location, slope, string):
        Drawable.__init__(self, string, (255, 255, 255), location, 12)
        HandlesEvent.__init__(self, [])

        self.location = location
        self.slope = slope

class SimpleProjectile(Projectile):
    def __init__(self, location, slope, string):
        super(SimpleProjectile, self).__init__(location, slope, string)
