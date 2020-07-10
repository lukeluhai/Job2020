import numpy as np


def printBomb(grc,row,col):

    for i in range(row):
        for j in range(col):
            if j==0:
                print("")
            print(str(grc[i*col+j])+"|",end="")
def judgeThekey(bomb,bombNum,bombView,clickrow,clickcol,clicktype,row,col):
    if bomb[clickrow][clickcol]==1 and clicktype==0:
        print("踩炸弹了，游戏结束")
        for i in range(row):
            for j in range(col):
                if bombNum[i][j]>0:
                    bombView[i*col+j]=str(int(bombNum[i][j]))+" "
                if bomb[i][j]==1:
                    bombView[i * col + j]="※"
        printBomb(bombView,row,col)
    if bomb[clickrow][clickcol]==0 and clicktype==0:
        bombView[clickrow* col + clickcol] = str(int(bombNum[clickrow][clickcol])) + " "
        printBomb(bombView, row, col)
    if bomb[clickrow][clickcol]==1 and clicktype==1:
        bombView[clickrow * col + clickcol] = "■"
        printBomb(bombView, row, col)
    if bomb[clickrow][clickcol]==0 and clicktype==1:
        bombView[clickrow * col + clickcol] = "■"
        printBomb(bombView, row, col)
    return bombView




if __name__ == '__main__':
    row=15
    col=15
    bomb=((np.random.rand(row,col))-0.2).round(0)
    print(bomb)
    print(bomb.sum())
    bombNum=np.zeros((row,col))
    print(bombNum)
    for i in range(row):
        for j in range(col):
            if i-1>=0 and j-1>=0:
                n0=bomb[i-1][j-1]
            else:
                n0=0

            if i-1>=0 and j>=0:
                n1=bomb[i-1][j]
            else:
                n1=0
            if i-1>=0 and j+1<col:
                n2=bomb[i-1][j+1]
            else:
                n2=0
            if i>=0 and j-1>=0:
                n3=bomb[i][j-1]
            else:
                n3=0
            if i>=0 and j+1<col:
                n5=bomb[i][j+1]
            else:
                n5=0
            if i+1<row and j-1>=0:
                n6=bomb[i+1][j-1]
            else:
                n6=0
            if i+1<row and j>=0:
                n7=bomb[i+1][j]
            else:
                n7=0
            if i+1<row and j+1<col:
                n8=bomb[i+1][j+1]
            else:
                n8=0

            bombNum[i][j]=n0+n1+n2+n3+n5+n6+n7+n8
            n0 = 0
            n1 = 0
            n2 = 0
            n3 = 0
            n5 = 0
            n6 = 0
            n7 = 0
            n8 = 0
    print(bombNum)
    bombView=[]
    for i in range(row):
        for j in range(col):
            bombView.append("□")
    printBomb(bombView,row,col)

    inputStr = input("请输入：")
    while inputStr!='exit':
        clickrow,clickcol,clicktype=inputStr.split(" ")[0],inputStr.split(" ")[1],inputStr.split(" ")[2]
        print(clickrow,clickcol,clicktype)
        bombView=judgeThekey(bomb, bombNum, bombView,int(clickrow), int(clickcol), int(clicktype), row, col)
        if "※" in bombView:
            break
        else:
            inputStr = input("请输入：")



