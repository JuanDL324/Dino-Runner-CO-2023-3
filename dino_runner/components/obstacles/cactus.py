import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS


class Cactus(Obstacle):
    Y_POS_SMALL_CACTUS = 325
    Y_POS_LARGE_CACTUS = 300
    LIST_CACTUS_Y_POS = SMALL_CACTUS + LARGE_CACTUS


    def __init__(self):
        self.image = random.choice(self.LIST_CACTUS_Y_POS)
        super().__init__(self.image)
        if self.image in SMALL_CACTUS:
            self.rect.y = self.Y_POS_SMALL_CACTUS
        if self.image in LARGE_CACTUS:
            self.rect.y = self.Y_POS_LARGE_CACTUS

