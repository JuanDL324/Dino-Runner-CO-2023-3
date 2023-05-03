import pygame, random
from dino_runner.utils.constants import (JUMPING, JUMPING_SHIELD, JUMPING_HAMMER, 
                                         RUNNING, RUNNING_SHIELD, RUNNING_HAMMER,
                                         DUCKING, DUCKING_SHIELD, DUCKING_HAMMER, DINO_DEAD,
                                         DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, CLOCK_TYPE)


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5


    def __init__(self):
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_dead = False
        self.flag_clock = False


    def update(self, user_input):
        if self.dino_jump:
            self.jump(user_input)
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()


        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP]:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.steps_index >= 10:
            self.steps_index = 0


    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def dead(self):
        if self.dino_duck:
            self.image = DINO_DEAD
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.dino_dead = True
        self.image = DINO_DEAD
        self.dino_dead = True


    def run(self):
        self.image = self.run_img[self.type][0] if self.steps_index < 5 else self.run_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps_index += 1


    def duck(self):
        self.image = self.duck_img[self.type][0] if self.steps_index < 5 else self.duck_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.steps_index += 1


    def jump(self, user_input):
        self.image = self.jump_img[self.type]
        if user_input[pygame.K_w] and self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 2
            self.jump_vel += 0.36
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 #Entre más alto el número más alto saltará #Independiente de la distancia, sin importar que tan alto vaya regresara a la misma distancia que si su número fuera menor #Altura
            self.jump_vel -= 0.8 #Distancia, entre menor sea el número, más alto va a saltar, si aumenta la distancia se acorta y salta menos
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
        #al no saltar mucho(en la resta de el eje y y la velocidad por 4) y restarle más(en veljump), pues menos distancia y menos salto subre
        # si la resta es muy pequeña, demorará mucho para hasta llegar al suelo


    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
        #if power_up.type == CLOCK_TYPE:
            #self.flag_clock = True ######### un número quiza?
        
            
        
