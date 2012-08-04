import itertools
import sys

import pygame
from pygame.locals import *
from pygame.sprite import (
    Group,
    RenderUpdates,
    Sprite
    )

from drawable import (
    BGSprite,
    Drawable
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
        if event.payload.type == QUIT:
            sys.exit(0)   

class Event(object):
    def __init__(self, payload):
        self.payload = payload

    def __str__(self):
        return "Event type: {0} Payload: {1}".format(type(self), self.payload)

    def get_payload(self):
        return self.payload

class TargettedEvent(Event):
    def __init__(self, payload, target):
        super(TargettedEvent, self).__init__(payload)
        self.target = target

    def get_target(self):
        return self.target

    def __str__(self):
        return "{0} Target: {1}".format(super(TargettedEvent, self).__str__(), self.target)

class PygameEvent(Event):
    def __init__(self, event):
        super(PygameEvent, self).__init__(event)
        self.pygame_type = event.type

    def __str__(self):
        return "{0} {1}".format(super(PygameEvent, self).__str__(), self.payload)


class RedrawHandler(PygameHandler):
    def __init__(self):
        super(RedrawHandler, self).__init__(REDRAWEVENT)
    def handle_event(self, event):
        loop = get_loop()
        loop.render.clear(pygame.display.get_surface(), lambda surf, rect: surf.fill((0, 0, 0), rect))
        rect_list = loop.render.draw(pygame.display.get_surface())
        pygame.display.update(rect_list)

class UpdateEvent(Event):
    def __init__(self, payload):
       super(UpdateEvent,self).__init__(payload)

class UpdateHandler(PygameHandler):
    def __init__(self):
        super(UpdateHandler, self).__init__(UPDATEEVENT)
    def handle_event(self, event):
        loop = get_loop()
        loop.enqueue(UpdateEvent(None))

class CleanupHandler(HandlesEvents):
    def __init__(self):
        super(CleanupHandler, self).__init__([ UpdateEvent ])

    def handle_event(self, event):
        if isinstance(event, UpdateEvent):
            loop = get_loop()
            group = Group(loop.render.sprites())
            for member in pygame.sprite.spritecollide(loop.bg_sprite, loop.render, False):
                if member in group:
                    group.remove(member)
            for sprite in group:
                print sprite
                loop.rm_object(sprite)
        

class EventLoop(object):
    def __init__(self):
        self.objs = {}
        self.events = []
        self.render = RenderUpdates()
        self.projectiles = Group()
        self.enemies = Group()
        self.bg_sprite = BGSprite(pygame.display.get_surface())

        # Since we don't care about MOST EVENTS
        pygame.event.set_allowed(None)
        pygame.event.set_allowed([ MOUSEBUTTONDOWN, KEYDOWN, QUIT, UPDATEEVENT ])

    def add_object(self, obj, type=""):
        if isinstance(obj, HandlesEvents):
            if obj.events == ALL:
                try:
                    self.objs[ALL].append(obj)
                except KeyError:
                    self.objs[ALL] = [ obj ]
            else:
                for event in obj.events:
                    try:
                        self.objs[event].append(obj)
                    except KeyError:
                        self.objs[event] = [ obj ]
        if isinstance(obj, Sprite):
            self.render.add(obj)
            if type == "enemy":
                self.enemies.add(obj)
            if type == "projectile":
                self.projectiles.add(obj)

    def rm_object(self, obj):
        for key in self.objs.keys():
            self.render.remove(obj)
            if obj in self.objs[key]:
                self.objs[key].remove(obj)
            if self.projectiles.has(obj):
                self.projectiles.remove(obj)
            if self.enemies.has(obj):
                self.enemies.remove(obj)
            print "Removed {0}".format(obj)

    def enqueue(self, event):
        if isinstance(event, Event):
            return self.events.append(event)
        elif isinstance(event, list):
            return [ self.enqueue(ev) for ev in event ]

    def tick(self):
        try:
            event = self.events.pop()
        except IndexError:
            event = None

        if event is not None:
            if isinstance(event, TargettedEvent):
                event.get_target().handle_event(event)
                for obj in self.objs[ALL]:
                    obj.handle_event(event)
            else:
                for obj in self.objs[type(event)] + self.objs[ALL]:
                    if obj.handles_event(event):
                        obj.handle_event(event)


        py_events = map(lambda event: PygameEvent(event), pygame.event.get())
        for py_event in py_events:
            for obj in reduce(lambda obj_list, obj: obj_list + obj, map(lambda key: self.objs[key], filter(lambda handler_type: issubclass(handler_type, PygameEvent) if handler_type != ALL else False, self.objs.keys())), []):
                if obj.handles_event(py_event):
                    obj.handle_event(py_event)
