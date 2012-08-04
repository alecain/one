import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.sprite import (
    DirtySprite,
    Sprite
    )

class Drawable(DirtySprite):
    def __init__(self, string, color, location, size):
        DirtySprite.__init__(self)

        self.string = string
        self.color = color
        self.location = location

        self.font = Font(pygame.font.get_default_font(), size)

        self.regen_sprite()

    def _gen_surface(self):
        return self.font.render(self.string, True, self.color)

    def regen_sprite(self):
        self.image = self._gen_surface()
        self.rect = Rect(self.location, self.image.get_size())
        self.dirty = 1

class BGSprite(Sprite):
    def __init__(self, surface):
        super(BGSprite, self).__init__()
        self.rect = surface.get_rect()
        self.image = surface
