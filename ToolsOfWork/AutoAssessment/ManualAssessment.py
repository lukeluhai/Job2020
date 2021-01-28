import os
import MyLib.calAngle
import math

CsvPath = "D:\\temp\\人工评估\\csv\\"
CellName = {}
f = open(CsvPath + "CELL.csv", "r")
for line in f.readlines():
    tmpStr = line.replace("\n", "").split(",")
    CellName[tmpStr[5]] = tmpStr[0]
f.close
malAssCellFile = open(CsvPath + "msf.csv", "a+")
for DataFile in os.listdir(CsvPath):
    malAssCell = []
    if DataFile == "CELL.csv" or ("-" not in DataFile):
        continue
    df = open(CsvPath + DataFile, "r")
    malAssCell.append(df.__next__())
    for line in df.readlines():
        if line.split(",")[8] in CellName:
            malAssCell.append(line)
    df.close
    # malAssCell=list(set(malAssCell))
    malAssCellFile.writelines(malAssCell)
malAssCellFile.close

