import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD, LARGE_CACTUS, SMALL_CACTUS


class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.steps_index = 0

    def update(self, game_speed, player):
        self.rect.x -= game_speed

        if self.rect.colliderect(player.dino_rect):
            if not player.shield:
                pygame.time.delay(300)
                player.dead()



    def draw(self, screen):
        screen.blit(self.image, self.rect)

