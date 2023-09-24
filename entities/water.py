import pygame
import math







class Water(pygame.sprite.Sprite):
    def __init__(self, screen, step,color=(0,0,255)):
        super().__init__()
        self.wave = 0
        self.color = color
        self.image = pygame.surface.Surface((screen.get_width(),32))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,screen.get_height()+8)
        self.old_rect = self.rect.copy()
        self.vector = pygame.math.Vector2(self.rect.topleft)
        self.points_water = [[i,self.rect.top] for i in range(0,screen.get_width()+step,step)]
        self.image.set_colorkey((0,0,0))
        self.image.set_alpha(100)

    def draw(self, surface):
        self.image.fill(self.image.get_colorkey())
        rect = pygame.Rect(0,8,self.rect.width,self.rect.height)
        pygame.draw.rect(self.image, (0,0,233) , rect)
        
        rect2 = pygame.draw.lines(self.image, self.color, False, self.points_water, 10)
        self.old_rect = self.rect.copy()
        surface.blit(self.image, self.rect)

    def update(self, dt):
        for i in range(len(self.points_water)):
            self.points_water[i][1] = int(math.sin(i + self.wave)*4 +8)
        self.wave += 0.05
        self.rect.y = self.vector.y + math.sin(self.wave)*4
