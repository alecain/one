import sys

import pygame
from pygame.locals import *
from pygame.sprite import (
    RenderUpdates,
    Sprite
    )

from locals import *

class HandlesEvents(object):
    def __init__(self, events):
        self.events = events

    def handles_event(self, event):
        return (self.events == ALL or type(event) in self.events)

    def handle_event(self, event):
        pass

class PrintHandler(HandlesEvents):
    def __init__(self):
        super(PrintHandler, self).__init__(ALL)

    def handle_event(self, event):
        print event

class PygameHandler(HandlesEvents):
    def __init__(self, pygame_type):
        super(PygameHandler, self).__init__([ PygameEvent ])
        self.pygame_type = pygame_type

    def handles_event(self, event):
        return (super(PygameHandler, self).handles_event(event) and event.pygame_type == self.pygame_type)

    def handle_event(self, event):
        pass

class QuitHandler(PygameHandler):
    def __init__(self):
        super(QuitHandler, self).__init__(QUIT)

    def handle_event(self, event):
        sys.exit(0)   

class Event(object):
    def __init__(self, payload):
        self.payload = payload

    def __str__(self):
        return self.payload

    def get_payload(self):
        return self.payload

class TargettedEvent(Event):
    def __init__(self, payload, target):
        super(TargettedEvent, self).__init__(payload)
        self.target = target

    def get_target(self):
        return target

class PygameEvent(Event):
    def __init__(self, event):
        super(PygameEvent, self).__init__(event)
        self.pygame_type = event.type

    def __str__(self):
        return "{0} {1}".format(super(PygameEvent, self).__str__(), self.payload)

class EventLoop(object):
    def __init__(self):
        self.objs = []
        self.events = []
        self.render = RenderUpdates()

    def add_object(self, obj):
        if isinstance(obj, HandlesEvents):
            self.objs.append(obj)
        if isinstance(obj, Sprite):
            self.render.add(obj)

    def enqueue(self, event):
        if isinstance(event, Event):
            self.events.append(event)
        if isinstance(event, list):
            for ev in event:
                self.enqueue(event)

    def tick(self):
        try:
            event = self.events.pop()
        except IndexError:
            event = None

        for obj in self.objs:
            if event is not None and not isinstance(event, TargettedEvent) and obj.handles_event(event):
                obj.handle_event(event)
            elif event is not None and isinstance(event, TargettedEvent):
                event.get_target().handle_event(event)
        map(lambda event: self.enqueue(PygameEvent(event)), pygame.event.get())
        self.render.draw(pygame.display.get_surface())
        pygame.display.flip()
