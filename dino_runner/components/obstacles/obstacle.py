import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, player):
        self.rect.x -= game_speed


        #self.image = BIRD[0] if self.steps_index < 5 else BIRD[1]

        #self.steps_index += 1


        if self.rect.colliderect(player.dino_rect):
            pygame.time.delay(300)
            player.dead()



    def draw(self, screen):
        screen.blit(self.image, self.rect)

