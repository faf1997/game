import pygame 
from entities.utils import load_img, get_path
from math import cos, sin






class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Player,self).__init__()
        self.weight = weight
        self.material_type = 1
        self.image = load_img(f'{get_path()}./imgs/dirt_2_4.png',mode="no_alpha")
        self.rect = self.image.get_rect(); self.rect.topleft = pos
        self.old_rect = self.rect.copy()
        self.vector = pygame.Vector2(self.rect.topleft)


    def move(self):
        events = pygame.key.get_pressed()
        if events[pygame.K_LEFT]:
            self.vector.x -= 1
        if events[pygame.K_RIGHT]:
            self.vector.x += 1
        if events[pygame.K_DOWN]:
            self.vector.y += 1
        if events[pygame.K_UP]:
            self.vector.y -= 1


    def set_rad_joistic(self,rad):
        cos_value = cos(rad)
        if cos_value != 1:
            self.vector.x += cos_value
        self.vector.y += sin(rad)
        if self.vector.magnitude() != 0:
            self.vector.normalize()



    def update(self, dt):
        self.move()
        self.rect.topleft = self.vector
        self.rect.topleft = self.vector

    def draw(self, surface):
        surface.blit(self.image,self.rect)


    def __str__(self):
        return f'Player: {*self.rect.topleft,*self.rect.size}'