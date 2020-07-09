import numpy as np
def eightQueen(chess,chessBoard,n,result):
    if n==0:
        print(result)
        return True

    for i in range(0,8):
        chessBoard[chess[n][0]][i]=0
        chessBoard[i][chess[n][1]]=0

    for i in range(0,8):
        if chess[n][0]+1<8 and chess[n][1]+1<8:
            chessBoard[chess[n][0]+1][chess[n][1]+1]=0
        if chess[n][0]+1<8 and chess[n][1]-1>=0:
            chessBoard[chess[n][0]+1][chess[n][1]-1]=0
        if chess[n][0]-1>=0 and chess[n][1]-1>=0:
            chessBoard[chess[n][0]-1][chess[n][1]-1]=0
        if chess[n][0]-1>=0 and chess[n][1]+1<8:
            chessBoard[chess[n][0]-1][chess[n][1]+1]=0

    chess.pop(n)
    result.append(chess[n])

    a=True
    for i in chess:
        if chessBoard[i[0]][i[1]]==0:
            a=False
    if a==True:
        eightQueen(chess[:], chessBoard[:], n-1, result[:])


if __name__=="__main__":
    result=[]
    n=8
    chessBoard=[8][8]
    for i in range(0,8):
        for j in range(0,8):
            chessBoard[i][j]=1
    eightQueen(chessBoard,n,result)
