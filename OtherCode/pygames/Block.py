import numpy as np

C = {'C_1_1': [0, 9, 16, 'C_1_2',4], 'C_1_2': [0, 6, 19, 'C_1_1',4], \
      'C_2_1': [0, 8, 18, 'C_2_1',2], \
      'C_3_1': [0, 8, 17, 'C_3_2'], 'C_3_2': [0, 7, 18, 'C_3_3'], 'C_3_3': [0, 8, 17, 'C_3_4'],
      'C_3_4': [0, 7, 18, 'C_3_1'], \
      'C_4_1': [0, 8, 17, 'C_4_2'], 'C_4_2': [0, 7, 18, 'C_4_3'], 'C_4_3': [0, 8, 17, 'C_4_4'],
      'C_4_4': [0, 7, 18, 'C_4_1'], \
      'C_5_1': [0, 7, 18, 'C_5_2'], 'C_5_2': [0, 8, 17, 'C_5_3'], 'C_5_3': [0, 7, 18, 'C_5_4'],
      'C_5_4': [0, 8, 17, 'C_5_1'], \
      'C_6_1': [0, 7, 18, 'C_6_2'], 'C_6_2': [0, 8, 17, 'C_6_1'], \
      'C_7_1': [0, 7, 18, 'C_7_2'], 'C_7_2': [0, 8, 17, 'C_7_1']}
class Block:



    def __init__(self,x,y,z,type):
        self.x=x
        self.y=y
        self.z=z
        self.type=type
        pass

    def changeType(self,TMatrix,x,y):
        tempC=C[C[self.type][3]]

        if self.x>=tempC[0] and self.x<=tempC[1] and self.y<=tempC[2]:
            if C[self.type][3]=='C_1_2' and TMatrix[x+3][y]==0 and TMatrix[x+1][y]==0 and TMatrix[x+2][y]==0:
                self.type=C[self.type][3]
            elif C[self.type][3]=='C_1_1' and TMatrix[x][y+1]==0 and TMatrix[x][y+2]==0 and TMatrix[x][y+3]==0:
                self.type = C[self.type][3]
            elif C[self.type][3] == 'C_2_1':
                self.type = C[self.type][3]
            elif C[self.type][3] == 'C_3_1' and TMatrix[x][y+1]==0 and TMatrix[x][y+2]==0 and TMatrix[x+1][y+2]==0:
                self.type = C[self.type][3]


        if TMatrix[1][1]==0:

            pass


