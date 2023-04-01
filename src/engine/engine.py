from random import random, randint
import pygame, simple_draw as D
import entities.snowflake as S


class EventMouseMove:
    __moves_count = 0

    @staticmethod
    def check_moves_reached_number(number) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                EventMouseMove.__moves_count += 1
                break
        
        if EventMouseMove.__moves_count >= number:
            return True
        
        return False


class Engine:
    def __init__(self, resolution=(640, 480), snowflakes_number=10) -> None:
        D.resolution = resolution
        D.background_color = D.COLOR_BLACK

        pygame.init()
        pygame.mouse.set_visible(False)

        self.__snowflakes_number = snowflakes_number
        self.__snowflakes = [
            self.make_snowflake() for _ in range(self.__snowflakes_number)
        ]

        self.__trail_color = D.COLOR_BLACK
    
    def run(self) -> None:
        while True:
            for i in range(self.__snowflakes_number):
                self.__snowflakes[i].draw()
                self.__snowflakes[i].move()
                self.__snowflakes[i].draw_trail()
                if self.__snowflakes[i].y < -170:
                    self.__snowflakes[i] = self.make_snowflake()

            if EventMouseMove.check_moves_reached_number(4):
                pygame.quit()
                break
            
            D.sleep(0.005)
    
    def make_snowflake(self) -> S.Snowflake:
        x = randint(-120, D.resolution[0] + 20)
        y = D.resolution[1] + 70 + randint(-50, 720)
        speed_x = 1.0
        speed_y = randint(4, 12)
        accel_x = float(str(randint(1, 3)))
        size = randint(30, 95)
        sub_color = randint(230, 250)
        color = (sub_color, sub_color, sub_color)
        trail_color = D.COLOR_BLACK
        factor_a = random()
        factor_b = random()
        factor_c = 180 * random()

        return S.Snowflake(x=x, y=y, speed_x=speed_x,
                         speed_y=speed_y, accel_x=accel_x, size=size,
                         color=color, trail_color=trail_color, factor_a=factor_a,
                         factor_b=factor_b, factor_c=factor_c)