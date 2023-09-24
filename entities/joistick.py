import pygame

from entities.utils import load_img, get_path
from math import cos, sin, atan2


class Sprite2(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.weight = weight
        self.material_type = 1
        self.image = pygame.Surface((50, 50))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width() // 2, screen.get_height()// 2)
        self.speed = 5
        self.vector = pygame.Vector2(self.rect.topleft)

    def update(self, dt):
        # Mover el sprite hacia la posición del mouse
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            self.rect.move_ip((pos[0] - self.rect.centerx) // self.speed,(pos[1] - self.rect.centery) // self.speed)



class Joistick(pygame.sprite.Sprite):
    def __init__(self, pos, size=(80,80),mode="alpha"):
        super().__init__()
        self.image = load_img(f"{get_path()}./imgs/joystick.png", size, mode)
        self.body = self.image.copy()
        self.circle  = load_img(f"{get_path()}./imgs/joystick_2.png", (44.4,44.4), mode)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.old_rect = self.rect.copy()
        self.rect.topleft = pos
        self.rect_base = self.rect.copy()
        self.rect_base.topleft = (0,0)
        self.rect_circle = self.circle.get_rect()

        self.vector = pygame.Vector2(self.rect.topleft)
        self.image.set_alpha(100)
        



        
    def get_direction(self):
        self.rect_base.height//2

        x = self.rect_circle.centerx-self.rect_base.width//2
        y = self.rect_circle.centery-self.rect_base.height//2
        
        rad = atan2(y,x)
        return rad
        
    
    def set_pos(self, pos:tuple):
        self.rect.center = pos

    def __update_imgs(self):
        self.image.fill(self.image.get_colorkey())
        m_x, m_y = pygame.mouse.get_pos()
        if self.rect.collidepoint((m_x, m_y)):

            x = m_x - self.rect.x #- self.rect_circle.width//2
            y = m_y - self.rect.y #- self.rect_circle.height//2
            if pygame.mouse.get_pressed()[0]:
                self.rect_circle.move_ip((x - self.rect_circle.centerx) // 5,(y - self.rect_circle.centery) // 5)
            else:
                self.rect_circle.center = self.rect_base.center
        else:
            self.rect_circle.center = self.rect_base.center

            
        self.image.blit(self.body,(0,0))
        self.image.blit(self.circle,self.rect_circle.topleft)
        

    def update(self,dt):
        self.__update_limit_circle()
        self.__update_imgs()
        self.get_direction()

        


    def draw(self, surface):
        surface.blit(self.image,self.rect)
        # pygame.draw.rect(surface,(0,255,0),self.rect_base,1)
        # pygame.draw.rect(surface,(0,255,0),self.rect_circle,1)


    def __update_limit_circle(self):
        if self.rect_circle.right > self.rect_base.right:
            self.rect_circle.right = self.rect_base.right
            
        if self.rect_circle.left < self.rect_base.left:
            self.rect_circle.left = self.rect_base.left

        if self.rect_circle.bottom > self.rect_base.bottom:
            self.rect_circle.bottom = self.rect_base.bottom

        if self.rect_circle.top < self.rect_base.top:
            self.rect_circle.top = self.rect_base.top


