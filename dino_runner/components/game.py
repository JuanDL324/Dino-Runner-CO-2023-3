import pygame, random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components import text_util


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
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count = 0
        self.difficulty = 1200



    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset_game()

    def update(self):
        if self.playing:
            self.points += 1
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            if self.player.flag_clock:
                self.game_speed = self.player.game_speed
                

            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1
            if self.points > self.difficulty:
                self.game_speed += 10
                self.difficulty += 1200



    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_score()
            self.draw_power_up()
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        else:
            self.draw_menu()
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


        image_width_bg = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width_bg + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width_bg:
            self.screen.blit(BG, (image_width_bg + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def draw_score(self):
        score, score_text = text_util.get_message("Points: " + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_text)

    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        if self.death_count == 0:
            text, text_rect = text_util.get_message("Press any key yto start", 30)
            self.screen.blit(text, text_rect)
        else:
            game_over, game_over_rect = text_util.get_message("GAME OVER", 60, height= SCREEN_HEIGHT//4)
            text, text_rect = text_util.get_message("Press any key to Restart", 30)
            score, score_rect = text_util.get_message("Your score: "+ str(self.points), 30, height= SCREEN_HEIGHT//2 + 50)
            collect_power_up, collect_power_up_rect = text_util.get_message("Your collected power ups: "+ str(self.power_up_manager.power_ups_collected), 30, height= SCREEN_HEIGHT//2 + 90)
            overcome_obstacle, overcome_obstacle_rect = text_util.get_message("Your obstacles overcome: "+ str(self.obstacle_manager.obstacles_overcome), 30, height= SCREEN_HEIGHT//2 + 130)
            self.screen.blit(game_over, game_over_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect) 
            self.screen.blit(collect_power_up, collect_power_up_rect)
            self.screen.blit(overcome_obstacle, overcome_obstacle_rect)

    def draw_power_up(self):
        if self.player.flag_clock:
            text, text_rect = text_util.get_message("Time left of clock: "+ str(self.player.time_to_show_clock), 20, 980, 60)
            self.screen.blit(text, text_rect)

        if self.player.flag_shield:
            text, text_rect = text_util.get_message("Time left of shield: "+ str(self.player.time_to_show_shield), 20, 980, 80)
            self.screen.blit(text, text_rect)

        if self.player.flag_hammer:
            text, text_rect = text_util.get_message("Time left of hammer: "+ str(self.player.time_to_show_hammer), 20, 970, 100)
            self.screen.blit(text, text_rect)




    def reset_game(self):
        self.difficulty = 1200
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0


        

