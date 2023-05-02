import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Birds(Obstacle):
    Y_POS_BIRD_HIGH = 300      #random.randint(300) 230(solo caminar), 270(duck), 300 (salto)
    Y_POS_BIRD_MEDIUM = 230
    Y_POS_BIRD_LOW = 270
    LIST_BIRD_POS_Y = []
    LIST_BIRD_POS_Y.append(Y_POS_BIRD_HIGH)
    LIST_BIRD_POS_Y.append(Y_POS_BIRD_MEDIUM)
    LIST_BIRD_POS_Y.append(Y_POS_BIRD_LOW)


    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.choice(self.LIST_BIRD_POS_Y)

    def update(self, game_speed, player):
        if self.image == BIRD[0] or self.image == BIRD[1]:

            self.image = BIRD[0] if self.steps_index < 5 else BIRD[1]

            self.steps_index += 1
            if self.steps_index >= 10:
                self.steps_index = 0
        super().update(game_speed, player)