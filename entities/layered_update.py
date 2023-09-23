from pygame.sprite import LayeredUpdates
import pygame
from entities.joistick import Joistick
from entities.camera import Camera
from entities.floor import Dirt
from entities.player import Player
from entities.colision_sys import collide_update



class LayeredUpdates(LayeredUpdates):
    def __init__(self):
        super().__init__()
        self.joistick = Joistick((0,0))
        self.add(self.joistick)


    def set_pos_joistick(self, pos):
        self.joistick.set_pos(pos)


    def draw2(self, surface:pygame.surface.Surface, camera, bgsurf=None, special_flags=0, show_hitbox=False):
        for s in self.sprites():
            rect = s.image.get_rect()
            rect.topleft = s.rect[0],s.rect[1]
            s.draw(surface)
            # if camera.rect.colliderect(rect) or isinstance(s, (Joistick)):
            #surface.blit(s.image, s.rect, None, special_flags)
            if show_hitbox:
                pygame.draw.rect(surface,(255,0,0),s.rect,1)
                pygame.draw.rect(surface,(255,0,255),s.old_rect,1)
            
                
    
    def update(self, *args, **kwargs):
        sprites:list = self.sprites()
        for sprite_a in sprites:
            sprite_a.old_rect.topleft = sprite_a.rect.topleft
            if isinstance(sprite_a,(Player)):
                sprite_a.set_rad_joistic(self.joistick.get_direction())
            sprite_a.update(*args, **kwargs)
            for sprite_b in sprites:
                if sprite_a != sprite_b:
                    collide_update(sprite_a.rect,sprite_a.old_rect,sprite_a.vector, sprite_b.rect)









            