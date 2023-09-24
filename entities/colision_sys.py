import pygame





def collide_update(rect_a, old_rect_a, vector_a, rect_b):
    
    if rect_a.colliderect(rect_b):# and not old_rect_a.colliderect(sprite_b.old_rect_a):

        if old_rect_a.left >= rect_b.right and rect_a.left <= rect_b.right:
            rect_a.left = rect_b.right
            vector_a.x = rect_a.x

        if old_rect_a.right <= rect_b.left and rect_a.right >= rect_b.left:
            rect_a.right = rect_b.left
            vector_a.x = rect_a.x

        if old_rect_a.top >= rect_b.bottom and rect_a.top <= rect_b.bottom:
            rect_a.top = rect_b.bottom
            vector_a.y = rect_a.y

        if old_rect_a.bottom <= rect_b.top and rect_a.bottom >= rect_b.top:
            rect_a.bottom = rect_b.top
            vector_a.y = rect_a.y


def water_collide(sprite_a, sprite_b):
    pass




