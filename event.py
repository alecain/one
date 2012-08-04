import sys

import pygame
from pygame.locals import *

class HandlesEvents(object):
    def __init__(self, events):
        self.events = events

    def handles_event(self, event):
        return (self.events == "ALL" or event.get_type() in self.events)

    def handle_event(self, event):
        pass

class PrintHandler(HandlesEvents):
    def __init__(self):
        super(PrintHandler, self).__init__("ALL")

    def handle_event(self, event):
        print event

class PygameHandler(HandlesEvents):
    def __init__(self, pygame_type):
        super(PygameHandler, self).__init__("pygame")
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
    def __init__(self, event_type):
        self.event_type = event_type

    def __str__(self):
        return self.event_type

    def get_type(self):
        return self.event_type

class PygameEvent(Event):
    def __init__(self, event):
        super(PygameEvent, self).__init__("pygame")
        self.pygame_type = event.type
        self.pygame_event = event

    def __str__(self):
        return "{0} {1}".format(super(PygameEvent, self).__str__(), self.pygame_event)

class EventLoop(object):
    def __init__(self):
        self.objs = []
        self.events = []

    def add_object(self, obj):
        if isinstance(obj, HandlesEvents):
            self.objs.append(obj)

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
            if event is not None and obj.handles_event(event):
                obj.handle_event(event)
        map(lambda event: self.enqueue(PygameEvent(event)), pygame.event.get())
