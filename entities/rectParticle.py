import pygame
from entities.timer import Timer
from random import randint




def reduce_particle(sprite, dt):
    sprite.size.x = sprite.size.x - sprite.subtract * dt
    sprite.size.y = sprite.size.y - sprite.subtract * dt
    sprite.temp_rect.topleft = sprite.rect.topleft
    sprite.temp_rect.size = sprite.size
    sprite.temp_rect.center = sprite.rect.width//2,sprite.rect.height//2
    if sprite.temp_rect.width <= 0 or sprite.temp_rect.height <= 0:
        sprite.kill()
    sprite.update_img()


def enlarge_particle(sprite, dt):
    sprite.size.x = sprite.size.x + sprite.subtract * dt
    sprite.size.y = sprite.size.y + sprite.subtract * dt
    sprite.temp_rect.topleft = sprite.rect.topleft
    sprite.temp_rect.size = sprite.size
    sprite.temp_rect.center = sprite.rect.width//2,sprite.rect.height//2
    if sprite.temp_rect.width > sprite.rect.width or sprite.temp_rect.height > sprite.rect.height:
        sprite.kill()
    sprite.update_img()




class RectParticle(pygame.sprite.Sprite):
    def __init__(self, pos, size:tuple,mode="enlarge"):
        super().__init__()
        self.image = pygame.Surface(size)
        self.__vars(pos, size)

        self.__config()
        self.__config_mode_sprite(pos, size, mode)


    def __vars(self,  pos, size):
        self.vector = pygame.math.Vector2(pos)
        self.gap = False
        self.subtract = 100
        self.size_borders_gap = 2
        self.color_rect = pygame.color.Color("#FFFFFF")
        self.image.fill(pygame.color.Color("#FF00FF"))
        self.image.set_colorkey(pygame.color.Color("#FF00FF"))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.old_rect = self.rect.copy()



    def __config(self):
        pass


    def __config_mode_sprite(self, pos, size, mode):
        if mode == "enlarge":
            self.size = pygame.math.Vector2((2,2))
            self.temp_rect = pygame.Rect(0,0, 2,2)
            self.update_particle = enlarge_particle
        if mode == "reduce":
            self.size = pygame.math.Vector2(size)
            self.temp_rect = pygame.Rect(0,0, *size)
            self.update_particle = reduce_particle
        self.temp_rect.center = self.temp_rect.center = self.rect.width//2,self.rect.height//2


    def set_color(self, color):
        self.color_rect = pygame.color.Color(color)


    def set_alpha(self,num:int):
        if num < 0 or num > 255:
            raise ValueError("alpha range is (0, 255)")
        self.image.set_alpha(num)

    def set_update_mode(self, mode:str):
        if mode == "reduce":
            print("reduce")
            self.update_particle = lambda x: reduce_particle
        if mode == "enlarge":
            self.update_particle = lambda x: enlarge_particle


    def is_gap(self, is_gap:bool, size_borders=2):
        self.gap = is_gap
        self.size_borders_gap = size_borders


    def subtractSize(self, size:int):
        self.subtract = size


    def center(self, x, y):
        self.rect.center = x, y

        
    def update_img(self):
        self.image.fill("#FF00FF")
        if self.gap:
            pygame.draw.rect(self.image,self.color_rect,self.temp_rect, self.size_borders_gap)
        else:
            pygame.draw.rect(self.image,self.color_rect,self.temp_rect)


    def update(self, dt):
        #pygame.draw.rect(self.image,self.color_rect,self.temp_rect)
        self.update_particle(self, dt)





















class Range:
    def __init__(self, a1, a2):
        self.__a1 = a1
        self.__a2 = a2

    @property
    def a1(self):
        return self.__a1
    
    @property
    def a2(self):
        return self.__a2



class Spark(pygame.sprite.Sprite):
    def __init__(self, pos, group, time_life:float=None,time_repeat=0.01, *args, **kwargs):
        super(Spark, self).__init__(*args, **kwargs)
        self.image = pygame.surface.Surface((0,0)).convert()
        self.rect = self.image.get_rect().center = pos
        self.vector = pygame.math.Vector2(pos)
        self.size = pygame.math.Vector2((20,20))
        self.range_x = Range(0,0)
        self.range_y = Range(0,0)
        self.group = group
        self.time_life = None
        self.time_repeat = Timer(time_repeat)
        self.__config(time_life)
        self.colors_proof()
        # self.image.set_alpha(0)


    def colors_proof(self):
        self.grays = [
        "#000000",  # Negro
        "#333333",  # Gris oscuro
        "#666666",  # Gris medio
        "#999999",  # Gris claro
        "#CCCCCC"   # Gris muy claro
        ]


    def set_range_x(self,range_x:tuple):
        self.range_x = Range(*range_x)


    def set_range_y(self,range_y:tuple):
        self.range_y = Range(*range_y)


    def set_pos(self, pos:tuple):
        self.vector = pygame.math.Vector2(pos)


    def set_size_particle(self, size:tuple):
        self.size = pygame.math.Vector2(size)


    def __config(self, time_life):
        if time_life != None:
            self.time_life = Timer(time)


    def update(self, dt):
        if self.time_life != None:
             self.time_life.update(dt)
        self.time_repeat.update(dt)

        if self.time_repeat.is_finish():
            rp = RectParticle((self.vector.x, self.vector.y),(self.size.x,self.size.y))

            #rp.set_color(self.grays[randint(0,len(self.grays)-1)])
            #rp.is_gap(True)

            rp.set_alpha(100)
            
            self.group.add(rp)
            self.time_repeat.reset()

    def draw(self, surface):
        surface.blit(self.image,self.rect)
















