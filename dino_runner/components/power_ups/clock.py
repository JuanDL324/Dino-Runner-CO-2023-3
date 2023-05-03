from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import CLOCK, CLOCK_TYPE

class Clock(PowerUp):
    #Y_POS_CLOCK = 350
    

    def __init__(self):
        self.image = CLOCK
        self.type = CLOCK_TYPE
        super().__init__(self.image, self.type)
        #self.rect.y = self.Y_POS_CLOCK