from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Hammer(PowerUp):
    Y_POS_HAMMER = 325
    Y_POS_HAMMER = 300


    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type) #accediendo al constructor del padre, PowerUp