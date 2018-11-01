import pygame
import numpy as np
import pandas as pd


def new_dat_f(dta_sts_matx):
    df = pd.DataFrame(dta_sts_matx)
    df.to_csv("DataSets.csv", header=None, index=None)


class Board:
    d_white = (250, 250, 250)
    blue_black = (50, 50, 50)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    teal = (0, 128, 128)
    gold = (255, 215, 0)

    def __init__(self, height, width):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.GAME_display = pygame.display.set_mode((height, width))
        self.clean()

    def clean(self):
        self.GAME_display.fill(Board.white)
        pygame.display.update()

    def close(self):
        print("preparing to exit...")
        pygame.quit()
        quit()

    def pop_exit_window(self, datsts):
        #       pygame.draw.rect(self.GAME_display, Board.white, (10,80,20,20), 100)
        pygame.font.init()  # you have to call this at the start,

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('To restart press C, Exit press X', False, (0, 0, 0))
        self.GAME_display.blit(textsurface, (0, 0))
        pygame.display.update()

        new_dat_f(datsts)

        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        pygame.quit()
                        # quit()
                    '''elif event.key == pygame.K_c:
                        self.clean() '''
