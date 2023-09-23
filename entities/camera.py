import pygame






class Camera(pygame.sprite.Sprite):
    def __init__(self, screen, *args, **kwarg):
        super(Camera,self).__init__(*args, **kwarg)
        self.image = pygame.surface.Surface((screen.get_width(),screen.get_height()))
        self.rect = self.image.get_rect()
        self.old_rect = self.rect.copy()
        self.vector = pygame.Vector2(self.rect.topleft)
        self.__image_config()

    def __image_config(self):
        #self.image = pygame.surface.Surface((60,60))
        self.image.set_colorkey(pygame.color.Color("#FF00FF"))
        self.image.fill(self.image.get_colorkey())
    
    def set_center(self, pos):
        self.rect.center = pos



    def update(self, dt):
        pass
        #self.set_center(pygame.mouse.get_pos())



    def draw(self, surface):
        surface.blit(self.image,self.rect)