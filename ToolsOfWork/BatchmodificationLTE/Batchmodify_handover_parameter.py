import pandas as pd
import numpy
import xlrd


def repalceEUtranCellMeasurement(str):

    return str.replace(",EUtranCellMeasurement=1", "")


dataPath = "E:\\DataBase\\FDD\\"
DFCellMeasGroup = pd.read_excel(
    dataPath + "CellMeasGroup_BatchData0.xlsx", sheet_name="CellMeasGroup", header=1
)
DFCellMeasGroup.drop([0, 1])
DFEUtranCellFDD = pd.read_excel(
    dataPath + "EUtranCellFDD_BatchData0.xlsx", sheet_name="EUtranCellFDD", header=1
)
DFEUtranCellFDD.drop([0, 1])

DFEUtranCellMeasurement = pd.read_excel(
    dataPath + "EUtranCellMeasurement_BatchData0.xlsx",
    sheet_name="EUtranCellMeasurement",
    header=1,
)
DFEUtranCellMeasurement=DFEUtranCellMeasurement.drop(index=[0, 1])
DFEUtranCellMeasurement["cellindex"] = DFEUtranCellMeasurement["DN"].map(
    repalceEUtranCellMeasurement
)
print(DFEUtranCellMeasurement)
print(DFEUtranCellMeasurement["cellindex"])


DF=pd.merge(DFEUtranCellFDD,DFEUtranCellMeasurement,left_on='DN',right_on='cellindex')
DF=pd.merge(DF,DFCellMeasGroup,left_on='测量配置索引组ID',right_on='DN')
DF['']