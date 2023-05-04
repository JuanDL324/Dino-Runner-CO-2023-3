import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Birds


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacles_overcome = 0
        self.cactus_or_bird = None
        self.list_cactus_or_bird = ["cactus", "bird"]


    def update(self, game_speed, player):
        self.cactus_or_bird = random.choice(self.list_cactus_or_bird)
        if len(self.obstacles) == 0 and self.cactus_or_bird == "cactus":
            self.obstacles.append(Cactus())
        if len(self.obstacles) == 0 and self.cactus_or_bird == "bird":
            self.obstacles.append(Birds())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width or obstacle.destroy:
                self.obstacles_overcome += 1
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)
        


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
