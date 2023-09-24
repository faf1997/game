import pygame

from entities.utils import load_img, get_path

import os

from random import randint


class Dirt(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super(Dirt,self).__init__()
        self.weight = weight
        self.material_type = 1
        self.image = load_img(path,mode="no_alpha")
        self.rect = self.image.get_rect()
        self.old_rect = self.rect.copy()
        self.rect.topleft = pos
        self.vector = pygame.Vector2(self.rect.topleft)
        #pygame.sprite.Sprite.rect = self.rect
        self.id = randint(1000, 9999)

    def __str__(self):
        return f'Dirt: {*self.rect.topleft,*self.rect.size}, id: {self.id}'

    def move(self):
        events = pygame.key.get_pressed()
        if events[pygame.K_a]:
            self.vector.x -= 1
        if events[pygame.K_d]:
            self.vector.x += 1
        if events[pygame.K_s]:
            self.vector.y += 1
        if events[pygame.K_w]:
            self.vector.y -= 1

    def update(self,dt):
        self.move()
        self.rect.topleft = self.vector

    def draw(self, surface):
        surface.blit(self.image,self.rect)

