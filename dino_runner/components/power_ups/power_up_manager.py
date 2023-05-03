import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.clock import Clock


class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.shield_or_hammer_or_clock = None
        self.list_shield_or_hammer_or_clock = ["shield", "clock", "hammer"]

    def update(self, game_speed, points, player):
        self.shield_or_hammer_or_clock = random.choice(self.list_shield_or_hammer_or_clock)
        if len(self.power_ups) == 0 and points % 200 == 0 and self.shield_or_hammer_or_clock == "hammer":
            self.power_ups.append(Hammer())
        if len(self.power_ups) == 0 and points % 200 == 0 and self.shield_or_hammer_or_clock == "shield":
            self.power_ups.append(Shield())
        if len(self.power_ups) == 0 and points % 200 == 0 and self.shield_or_hammer_or_clock == "clock":
            self.power_ups.append(Clock())
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)