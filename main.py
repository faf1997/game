import pygame
import sys

from entities.rectParticle import RectParticle, Spark
from entities.joistick import Joistick, Sprite2
from entities.utils import new_resolution, show_text, create_text, load_img, cut_imgs

from entities.layered_update import LayeredUpdates
from entities.camera import Camera
from entities.temporal_map import temporal_map
from entities.sprite import Sprite
from entities.water import Water





def draw_circle(surface, color, center, radius):
    pygame.draw.rect(surface,(0,255,0),pygame.draw.circle(surface, color, center, radius),1)



class App:
    def __init__(self):
        pygame.init()
        self.fps = 60
        self.bg_color = (pygame.color.Color('#6614ba'))
        self.clock = pygame.time.Clock()
        self.layered_updates = LayeredUpdates()
        self.screen = pygame.display.set_mode((0,0))
        pygame.display.set_caption("Platform Game")
        self.config()


    def config(self):
        self.screen = pygame.display.set_mode(new_resolution((self.screen.get_width(),self.screen.get_height()),0.25),pygame.SCALED)#|pygame.FULLSCREEN)
        self.camera = Sprite()#Camera(self.screen)
        # self.enlarge_rp = Spark((200,100),self.layered_updates)#RectParticle((80,100),(100,100))#
        # self.layered_updates.add(self.enlarge_rp)
        #self.layered_updates.add(self.camera)
        temporal_map(self.layered_updates, self.screen)
        self.layered_updates.set_pos_joistick((self.screen.get_width()-50,self.screen.get_height()-50))
        self.layered_updates.add(Water(self.screen,7))


    def run(self):
        running = True
        dt = 0
        while running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.FINGERDOWN:
                    draw_circle(self.screen,(255,0,0,),(event.x, event.y),40)

            try:
                dt = 1/self.clock.get_fps()
            except:pass

            self.update(dt)

            self.draw(self.screen, self.camera)

            # if pygame.mouse.get_pressed()[0]:
            #     draw_circle(self.screen,(255,0,0,0),(pygame.mouse.get_pos()),20)

            pygame.display.update()

        pygame.quit()
        sys.exit()



    def draw(self, screen, camera):
        self.screen.fill(self.bg_color)
        self.layered_updates.draw2(screen, camera)
        show_text(self.screen,f"FPS: {int(self.clock.get_fps())}",(10,10))
        show_text(self.screen,f"screen: {self.screen.get_width(),self.screen.get_height()}",(130,10))


    def update(self, dt):
        self.layered_updates.update(dt)
        # self.enlarge_rp.set_pos(pygame.mouse.get_pos())


if __name__ == "__main__":
    app = App()
    app.run()
