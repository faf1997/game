import pygame
from entities.utils import get_path

"""
material types

none type = 0
wood = 1
dirt = 2
sand = 3
grass = 4
water = 5



"""







class BoxWood(pygame.sprite.Sprite):
    def __init__(self, pos, weight=40):
        super().__init__()
        self.weight = weight
        self.material_type = 1
        self.vector = pygame.math.Vector2(pos)
        self.image = pygame.image.load(f'{get_path()}/imgs/box_wood.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.vector
        self.old_rect = self.rect.copy()


    def update(self, dt):
        self.vector.y += dt * self.weight
        self.rect.topleft = self.vector


    def draw(self,surface):
        surface.blit(self.image, self.rect)




