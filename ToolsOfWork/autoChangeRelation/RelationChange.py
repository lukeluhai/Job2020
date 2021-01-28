import os
import pandas as pd
import numpy

path = "E:\\relation\\"
print("open relationfile...")
dfRelation = pd.read_csv(
    path + "RelationAll.csv", "r", encoding="GBK", delimiter=",", header=0
)
print("maping....")
dfRelation["newcol1"] = (
    dfRelation["子网ID"].map(str)
    + "-"
    + dfRelation["网元ID"].map(str)
    + "-"
    + dfRelation["E-UTRAN FDD小区ID"].map(str)
    + "-"
    + dfRelation["E-UTRAN邻接小区"]
)
print("maping....")
dfRelation["newcol2"] = (
    dfRelation["E-UTRAN 邻接关系ID"].map(str)
    + "|"
    + dfRelation["重选时相邻小区对服务小区偏差"].map(str)
    + "|"
    + dfRelation["小区个体偏移"].map(str)
)
print("dict relation....")
dictRelation = dict(zip(dfRelation["newcol1"], dfRelation["newcol2"]))
dfCell = pd.read_csv(path + "CellAll.csv", encoding="GBK", delimiter=",", header=0)

# dfCell['newcol1']=dfCell['子网ID'].map(str)+'-'+dfCell['网元ID'].map(str)+'-'+dfCell['E-UTRAN FDD小区ID'].map(str)
dfCell["newcol2"] = (
    dfCell["子网ID"].map(str)
    + "-"
    + dfCell["网元ID"].map(str)
    + "-"
    + dfCell["E-UTRAN FDD小区ID"].map(str)
    + "-"
    + dfCell["eNodeB标识"].map(str)
)
# dictMoCell=dict(zip(dfCell['newcol1'],dfCell['用户标识']))
dictCellMo = dict(zip(dfCell["用户标识"], dfCell["newcol2"]))

# tmpf=open('E:\\relation\\aaaa.csv','w+')

# for x,y in dictCellMo.items():
#     tmpf.writelines(str(x)+" "+str(y)+'\n')
# tmpf.close()

dfCell["CGI"] = "460:00:" + dfCell["eNodeB标识"].map(str) + ":" + dfCell["小区标识"].map(str)
dictCGICell = dict(zip(dfCell["CGI"], dfCell["用户标识"]))
dictCGIMo = dict(zip(dfCell["CGI"], dfCell["newcol2"]))
dictMoCgi = dict(zip(dfCell["newcol2"], dfCell["CGI"]))
print("open 切换统计...")
relationcount = []
cells = {}
f = open(path + "CELL.TXT", "r", encoding="utf-8")
for i in f.readlines():
    cells[i.replace("\n", "")] = 1
f.close()
relationcountfiles = os.listdir("e:\\relation\\切换指标\\")
for relationfile in relationcountfiles:
    print("open ", "e:\\relation\\切换指标\\" + relationfile)
    rlf = open("e:\\relation\\切换指标\\" + relationfile, "r")
    for line in rlf.readlines():
        if line.split(",")[9] in cells:
            relationcount.append(line)
            print(line)
    rlf.close()


resultlist = []
resultlist.append(
    "序号,开始时间,结束时间,查询粒度,子网,子网名称,网元,网元名称,小区,小区名称,eNodeB,eNodeB名称,邻区关系,产品,系统内切换出请求次数,系统内切换出成功次数,系统内切换入请求次数,系统内切换入成功次数"
    + ","
    + "邻小区名"
    + ","
    + "正向参数"
    + ","
    + "反向参数"
    + ","
    + "正向子网ID"
    + ","
    + "正向网元ID"
    + ","
    + "正向E-UTRAN FDD小区ID"
    + ","
    + "正向eNodeB标识"
    + ","
    + "反向子网ID"
    + ","
    + "反向网元ID"
    + ","
    + "反向E-UTRAN FDD小区ID"
    + ","
    + "反向eNodeB标识"
    + "\n"
)
row = 0
for line in relationcount:
    row += 1
    # print(row)
    ltemp = line.split(",")
    cellname = ltemp[9]
    try:
        cellmo = dictCellMo[cellname]

        print(cellmo)
    except:
        cellmo = ""
    if cellmo == "":
        continue
    cellmoinfo = cellmo.split("-")
    relationstr = cellmo[0 : cellmo.rfind("-")] + "-" + ltemp[12][2:]
    print(relationstr)
    try:
        forwordRelation = dictRelation[relationstr]
    except:
        forwordRelation = ""

    try:
        reversecellmo = dictCGIMo[ltemp[12][2:]]
    #        print(reversecellmo)
    except:
        reversecellmo = ""
    try:
        reversecellname = dictCGICell[ltemp[12][2:]]
    except:
        reversecellname = ""
    try:
        reverseCgi = dictMoCgi[cellmo]
    #        print(reverseCgi)
    except:
        reverseCgi = ""

    try:
        reverRelation = dictRelation[
            reversecellmo[0 : reversecellmo.rfind("-")] + "-" + reverseCgi
        ]
    except:
        reverRelation = ""

    try:
        cellrmoinfo = dictCellMo[reversecellname].split("-")
    except:
        cellrmoinfo = [
            "",
            "",
            "",
            "",
        ]

    print(cellmoinfo)
    a = (
        line.replace("\n", "")
        + ","
        + reversecellname
        + ","
        + forwordRelation
        + ","
        + reverRelation
        + ","
        + cellmoinfo[0]
        + ","
        + cellmoinfo[1]
        + ","
        + cellmoinfo[3]
        + ","
        + cellmoinfo[2]
        + ","
        + cellrmoinfo[0]
        + ","
        + cellrmoinfo[1]
        + ","
        + cellrmoinfo[3]
        + ","
        + cellrmoinfo[2]
        + "\n"
    )
    resultlist.append(a)
print("输出结果")
resultfile = open(path + "result.csv", "w")
resultfile.writelines(resultlist)

resultfile.close()

