import pygame, random
from dino_runner.utils.constants import (JUMPING, JUMPING_SHIELD, JUMPING_HAMMER, 
                                         RUNNING, RUNNING_SHIELD, RUNNING_HAMMER,
                                         DUCKING, DUCKING_SHIELD, DUCKING_HAMMER, 
                                         DINO_DEAD, DEFAULT_TYPE, SHIELD_TYPE, 
                                         HAMMER_TYPE, CLOCK_TYPE)


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
        self.dino_super_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_dead = False
        self.flag_clock = False
        self.flag_hammer = False
        self.flag_shield = False
        self.shield = False
        self.hammer = False
        self.clock = False
        self.time_up_power_up = 0
        self.time_to_show_shield = 0
        self.time_to_show_hammer = 0
        self.time_to_show_clock = 0


    def update(self, user_input):
        if self.dino_super_jump:
            self.super_jump(user_input)
        if self.dino_jump:
            self.jump(user_input)
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()


        if user_input[pygame.K_q] and not self.dino_jump and not self.dino_duck:
            self.dino_super_jump = True
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump and not self.dino_super_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
            self.dino_super_jump = False
        elif user_input[pygame.K_UP]and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_super_jump = False
        elif not self.dino_jump and not self.dino_super_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
            self.dino_super_jump = False

        if self.steps_index >= 10:
            self.steps_index = 0

        if self.hammer:
            self.time_to_show_hammer = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if self.time_to_show_hammer <= 0:
                self.reset()

        if self.shield:
            self.time_to_show_shield = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if self.time_to_show_shield <= 0:
                self.reset()

        if self.clock:
            self.time_to_show_clock = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if self.time_to_show_clock <= 0:
                self.reset()


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

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 #Entre más alto el número más alto saltará #Independiente de la distancia, sin importar que tan alto vaya regresara a la misma distancia que si su número fuera menor #Altura
            self.jump_vel -= 0.8
        if user_input[pygame.K_w] and not user_input[pygame.K_UP]: # Mientras salta puede agacharse rapido y hacerlo repetidas veces
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        #if user_input[pygame.K_w] and not user_input[pygame.K_UP]: # puede bajar rapido mientras esta saltando
            #self.dino_rect.y -= self.jump_vel * 4 #Arriba lo que hace es no tener que presionar el salto para bajar, solo la W
            #self.jump_vel -= 1.6 #incluso con la rapidez de esta intercala los saltos
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def super_jump(self, user_input):
        self.image = self.jump_img[self.type]

        if self.dino_super_jump:
            self.dino_rect.y -= self.jump_vel * 5
            self.jump_vel -= 0.6
        if user_input[pygame.K_w] and not user_input[pygame.K_q]:
            self.dino_rect.y -= self.jump_vel * 5
            self.jump_vel -= 0.6
        #if user_input[pygame.K_w] and not user_input[pygame.K_q]:
            #self.dino_rect.y -= self.jump_vel * 5
            #self.jump_vel -= 1.2
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_super_jump = False
            self.jump_vel = self.JUMP_VEL



        #if self.dino_jump:
            #elf.dino_rect.y -= self.jump_vel * 4 #Entre más alto el número más alto saltará #Independiente de la distancia, sin importar que tan alto vaya regresara a la misma distancia que si su número fuera menor #Altura
            #self.jump_vel -= 0.8
        #if user_input[pygame.K_w] and user_input[pygame.K_UP]:
            #self.dino_rect.y -= self.jump_vel * 2
            #self.jump_vel += 0.36
        #if self.dino_jump:
            #self.dino_rect.y -= self.jump_vel * 4 #Entre más alto el número más alto saltará #Independiente de la distancia, sin importar que tan alto vaya regresara a la misma distancia que si su número fuera menor #Altura
            #self.jump_vel -= 0.8 #Distancia, entre menor sea el número, más alto va a saltar, si aumenta la distancia se acorta y salta menos

        #al no saltar mucho(en la resta de el eje y y la velocidad por 4) y restarle más(en veljump), pues menos distancia y menos salto subre
        # si la resta es muy pequeña, demorará mucho para hasta llegar al suelo


    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.shield = True
            self.time_up_power_up = power_up.time_up
            self.flag_shield = True 
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
            self.hammer = True
            self.time_up_power_up = power_up.time_up
            self.flag_hammer = True 
        if power_up.type == CLOCK_TYPE:
            self.clock = True
            self.time_up_power_up = power_up.time_up
            list_speed_fast_or_slow = [10, 40]
            self.game_speed = random.choice(list_speed_fast_or_slow)
            self.flag_clock = True 

    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.game_speed = 20
        self.clock = False
        self.flag_hammer = False
        self.flag_shield = False
        self.hammer = False
        self.time_up_power_up = 0
        

        
            
        
