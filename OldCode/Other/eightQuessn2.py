import numpy as np


def eightQueen(x, y, chessBoard1, result1, n):

   # print(x,y)
  #  print("chessbordid=",id(chessBoard))
  #  print("resultid=",id(result))
    if chessBoard1[x][y] == 0:
        return False
    else:
        chessBoard = []
        for i in chessBoard1:
            chessBoard.append(i.copy())
        result = []
        for i in result1:
            result.append(i)
        if n == 7:
            result.append([x, y])
            print('结果是:', n, result)
            return True
        for i in range(0, 8):
            chessBoard[x][i] = 0
            chessBoard[i][y] = 0
            if x + i < 8 and y + i < 8:
                chessBoard[x + i][y + i] = 0
            if x - i >= 0 and y + i < 8:
                chessBoard[x - i][y + i] = 0
            if x - i >= 0 and y - i >= 0:
                chessBoard[x - i][y - i] = 0
            if x + i < 8 and y - i >= 0:
                chessBoard[x + i][y - i] = 0
       # print('-------------------------------------------------------------',result)
        # for i in chessBoard:
        #    print(i)
        result.append([x, y])
        n += 1
        for i in range(x + 1, 8):
            for j in range(0, 8):

                eightQueen(i, j, chessBoard, result, n)

    return True


if __name__ == "__main__":
    result = []
    n = 8
    chessBoard = []
    for i in range(0, 8):
        chessBoard.append([1, 1, 1, 1, 1, 1, 1, 1])

    for j in range(0, 8):
            # print(chessBoard)
        eightQueen(0, j, chessBoard, result, 0)
