import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = weight
        self.material_type = 1
        self.image = pygame.surface.Surface((10,10))
        self.rect = self.image.get_rect()
        self.old_rect = self.rect.copy()
        self.vector = pygame.math.Vector2(self.rect.topleft)

    def draw(self, surface):
        surface.blit(self.image,self.rect)

def update_gravity(sprite:Sprite):
    if sprite.pos.is_normalize():
        sprite.pos.normalize()
    



def update_rect(rect, sprite):

    topleft = sprite.rect.topleft
    rect.topleft = topleft
    return rect


