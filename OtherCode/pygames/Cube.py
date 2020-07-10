import pygame
class cube:
    C={'C_1_1':[0,9],'C_1_2':[0,6],'C_2_1':[0,8],'C_3_1':[0,8],'C_3_2':[0,7],'C_3_3':[0,8],'C_3_4':[0,7],'C_4_1':[0,8],'C_4_2':[0,7],'C_4_3':[0,8],'C_4_4':[0,7],'C_5_1':[0,7],'C_5_2':[0,8],'C_5_3':[0,7],'C_5_4':[0,8],'C_6_1':[0,7],'C_6_2':[0,8],'C_7_1':[0,7],'C_7_2':[0,8]}

    def __init__(self,screen,x,y,img,typeNo):
        self.screen=screen
        #'images/cube.png'
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.type=typeNo

    def changeType(self):
        if self.type=='C_1_1':
            self.type='C_1_2'
        elif self.type=='C_1_2':
            self.type = 'C_1_1'
        elif self.type=='C_2_1':
            self.type='C_2_1'
        elif self.type=='C_3_1':
            self.type='C_3_2'
        elif self.type=='C_3_2':
            self.type='C_3_3'
        elif self.type=='C_3_3':
            self.type='C_3_4'
        elif self.type == 'C_3_4':
            self.type = 'C_3_1'
        elif self.type == 'C_4_1':
            self.type = 'C_4_2'
        elif self.type == 'C_4_2':
            self.type = 'C_4_3'
        elif self.type == 'C_4_3':
            self.type = 'C_4_4'
        elif self.type == 'C_4_4':
            self.type = 'C_4_1'
        elif self.type == 'C_5_1':
            self.type = 'C_5_2'
        elif self.type == 'C_5_2':
            self.type = 'C_5_3'
        elif self.type == 'C_5_3':
            self.type = 'C_5_4'
        elif self.type == 'C_5_4':
            self.type = 'C_5_1'


    def blitme(self):
        self.screen.blit(self.image, self.rect)

