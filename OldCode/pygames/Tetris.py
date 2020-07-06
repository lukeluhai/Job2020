import sys
import pygame
from pygames import settings
from pygames import Cube
import numpy as np


def run_game():
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Trtris")
    cube=[]
    TMatrix=np.random.randint(0,2,(10,20))
    # 绘制底格

   # cube2=Cube.cube(screen,40,80,'images/C_1_1.png','C_1_1')

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        refreshScreen(TMatrix,screen,cube)

    #    cube2.blitme()

        pygame.display.flip()

def Cubecharge(cube,TMatrix):

    pass


def refreshScreen(TMatrix,screen,cube):


    print(TMatrix)
    for i in range(0,10):
        for j in range(0,20):
            if TMatrix[i][j]>0.5:
                cubetemp=Cube.cube(screen,i*20+10,j*20+20,'images/cube2.png','')
                cube.append(cubetemp)
            else:
                cubetemp=Cube.cube(screen,i*20+10,j*20+20,'images/cube.png','')
                cube.append(cubetemp)
    for i in range(0, 10):
        for j in range(0, 20):
            cube[i + j * 10].blitme()
run_game()