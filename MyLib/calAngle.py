'''
    计算两点之间在mapinfo中的夹角
    输入两点经纬度
    返回：夹角值，两点距离
'''
import math


def calAngle(lon_x1, lat_y1, lon_x2, lat_y2):
    valCos = (lat_y2-lat_y1)*110 / \
        ((((lon_x1-lon_x2)*110)**2+((lat_y1-lat_y2)*110)**2)**0.5)
    valSin = (lon_x2-lon_x1)*110 / \
        ((((lon_x1-lon_x2)*110)**2+((lat_y1-lat_y2)*110)**2)**0.5)
    distance = (((lon_x1-lon_x2)*110)**2+((lat_y1-lat_y2)*110)**2)**0.5
    if valSin >= 0 and valCos >= 0:
        return math.asin(valSin)*180/math.pi, distance
    elif valSin >= 0 and valCos < 0:
        return math.acos(valCos)*180/math.pi, distance
    elif valSin <= 0 and valCos <= 0:
        return 360-math.acos(valCos)*180/math.pi, distance
    elif valSin < 0 and valCos > 0:
        return 360-math.asin(valCos)*180/math.pi, distance

    # return(valSin,valCos,math.asin(valSin)*180/math.pi,math.acos(valCos)*180/math.pi)


a1 = calAngle(113.322500, 23.081710, 113.323250, 23.083009)
a2 = calAngle(113.322500, 23.081710, 113.323013, 23.080300)
a3 = calAngle(113.322500, 23.081710, 113.321201, 23.080960)
a4 = calAngle(113.322500, 23.081710, 113.321536, 23.082859)


a5 = calAngle(113.322500, 23.081710, 113.322500, 23.083009)  # 0
a6 = calAngle(113.322500, 23.081710, 113.322500, 23.080300)  # 180
a7 = calAngle(113.322500, 23.081710, 113.321201, 23.081710)  # 270
a8 = calAngle(113.322500, 23.081710, 113.323536, 23.081710)  # 90


print(a1)
print(a2)
print(a3)
print(a4)


print(a5)
print(a6)
print(a7)
print(a8)
