import pygame, random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    frames_clouds = 0
    clouds = []
    for index in range(6):
        x_pos_cluod = 1200
        y_pos_cluod = random.randint(0, 360)
        speed_cloud = random.randint(1, 8)
        list_clouds = [x_pos_cluod, y_pos_cluod, speed_cloud]
        clouds.append(list_clouds)


    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()



    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player)
        if self.player.dino_dead:
            self.playing = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):

        for index in self.clouds:
            index[0] -= index[2]
            if index[0] < -200:
                index[0] = 1200
                index[1] = random.randint(0, 360)
                index[2] = random.randint(1, 8)


        
        self.frames_clouds += 1
        if self.frames_clouds >= 71:
            self.frames_clouds = 1
        
        if self.frames_clouds < 11:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))
        elif self.frames_clouds < 31:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))
        elif self.frames_clouds < 51:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))
        elif self.frames_clouds < 71:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))

        #image_width_cloud = CLOUD.get_width()
        #image_height_cloud = CLOUD.get_height()
        #self.screen.blit(CLOUD, (self.x_pos_cluod, self.y_pos_cloud))
        #self.screen.blit(CLOUD, ((self.x_pos_cluod / 2), (self.y_pos_cloud / 2)))
        #self.screen.blit(CLOUD, ((self.x_pos_cluod / 1.5), (self.y_pos_cloud / 1.5)))
        #self.screen.blit(CLOUD, ((self.x_pos_cluod * 1.6) - image_width_cloud, (image_height_cloud * 1.6) + self.y_pos_cloud))
        #self.screen.blit(CLOUD, (self.x_pos_cluod + image_width_cloud, image_height_cloud + self.y_pos_cloud))
        #if self.x_pos_cluod <= -image_width_cloud:
        #    self.x_pos_cluod = 2100
        #self.x_pos_cluod -= self.game_speed - 5


        image_width_bg = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width_bg + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width_bg:
            self.screen.blit(BG, (image_width_bg + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
