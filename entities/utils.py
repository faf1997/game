import pygame
import os

def get_path():
    return f'{os.path.abspath(".")}/'

def new_resolution(size:tuple,porcent=0.25):
    w, h = size
    return int(w*porcent), int(h*porcent)



def show_text(screen, text, pos, font="Times New Roman", font_size=24, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_img = font.render(text, False, color)
    screen.blit(text_img, pos)


def create_text(screen, text, pos, font="Times New Roman", font_size=24, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    return font.render(text, False, color)


def resize_img(surface, size:tuple):
    return pygame.transform.scale(surface,size)


def load_img(path, resize=None,mode="alpha"):#no_alpha
    img = pygame.image.load(path)
    img.set_alpha(255)
    if mode == "no_alpha":
        new_surf = pygame.surface.Surface((img.get_width(),img.get_height())).convert()
        color_key = pygame.color.Color("#FF00FF")
        new_surf.set_colorkey(color_key)
        new_surf.fill(color_key)
        new_surf.blit(img, (0, 0))
        if not resize is None:
            resize_img(new_surf,resize)
        return new_surf
    if not resize is None:
        return resize_img(img,resize)
    return img



def create_surf(width,height,color_key=(255,0,255)):
    img = pygame.surface.Surface((width,height))
    img.set_colorkey(color_key)
    img.fill(color_key)
    img.convert()
    return img




def load_sprite(input_path,output_path,width=16,height=16,name_reference="blocks")->list:
    anim_list = []
    img = pygame.image.load(input_path)
    range_x = img.get_width()//width
    range_y = img.get_height()//height
    rect = pygame.Rect(0,0,width,height)
    for y in range(range_y):
        for x in range(range_x):
            pos = (x* width,y*height)
            new_img = create_surf(width,height)
            cut_rect = pygame.Rect(*pos,width,height)
            new_img.blit(img,rect,cut_rect)
            anim_list.append()



def cut_imgs(input_path,output_path,width=16,height=16,name_reference="blocks"):
    img = pygame.image.load(input_path)
    range_x = img.get_width()//width
    range_y = img.get_height()//height
    rect = pygame.Rect(0,0,width,height)
    for y in range(range_y):
        for x in range(range_x):
            pos = (x* width,y*height)
            new_img = create_surf(width,height)
            cut_rect = pygame.Rect(*pos,width,height)
            new_img.blit(img,rect,cut_rect)
            pygame.image.save(new_img,f'{output_path}{name_reference}_({y},{x}).png')


