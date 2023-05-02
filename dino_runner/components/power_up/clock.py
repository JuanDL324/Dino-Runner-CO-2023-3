from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import CLOCK

class Clock(PowerUp):
    Y_POS_CLOCK = 350


    def __init__(self):
        self.image = CLOCK
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CLOCK