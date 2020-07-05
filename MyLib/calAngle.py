'''
    getAngle
    计算两点之间在mapinfo中的夹角
    输入：两点经纬度
    返回：夹角值，两点距离

    getRelative
    按照mapinfo的标准，计算两点方向的相关性
    输入：两点经纬度
    返回：相关性(0~1)，两点距离

'''
import math
distancePerlon = 102.2695072
distancePerlat = 111.1914257


def getAngle(X1_lon, Y1_lat, X2_lon, Y2_lat):
    valCos = (Y2_lat-Y1_lat)*distancePerlat / \
        ((((X1_lon-X2_lon)*distancePerlon)**2+((Y1_lat-Y2_lat)*distancePerlat)**2)**0.5)
    valSin = (X2_lon-X1_lon)*distancePerlon / \
        ((((X1_lon-X2_lon)*distancePerlon)**2+((Y1_lat-Y2_lat)*distancePerlat)**2)**0.5)
    distance = (((X1_lon-X2_lon)*distancePerlon)**2 +
                ((Y1_lat-Y2_lat)*distancePerlat)**2)**0.5
    if valSin >= 0 and valCos >= 0:
        return math.asin(valSin)*180/math.pi, distance
    elif valSin >= 0 and valCos < 0:
        return math.acos(valCos)*180/math.pi, distance
    elif valSin <= 0 and valCos <= 0:
        return 360-math.acos(valCos)*180/math.pi, distance
    elif valSin < 0 and valCos > 0:
        return 360-math.asin(valCos)*180/math.pi, distance


def getRelative(X1_lon, Y1_lat, ang1, X2_lon, Y2_lat, ang2):
    distance = (((X1_lon-X2_lon)*distancePerlon)**2 +
                ((Y1_lat-Y2_lat)*distancePerlat)**2)**0.5
    X11_lon = X1_lon+distance/distancePerlon/2*math.cos((90-ang1)/180*math.pi)
    Y11_lat = Y1_lat+distance/distancePerlat/2*math.sin((90-ang1)/180*math.pi)

    X21_lon = X2_lon+distance/distancePerlon/2*math.cos((90-ang2)/180*math.pi)
    Y21_lat = Y2_lat+distance/distancePerlat/2*math.sin((90-ang2)/180*math.pi)

    distance2 = (((X11_lon-X21_lon)*distancePerlon)**2 +
                 ((Y11_lat-Y21_lat)*distancePerlat)**2)**0.5

    return(1-distance2/distance/2, distance)

    # return(valSin,valCos,math.asin(valSin)*180/math.pi,math.acos(valCos)*180/math.pi)


# a1 = calAngle(113.322500, 23.081710, 113.323250, 23.083009)
# a2 = calAngle(113.322500, 23.081710, 113.323013, 23.080300)
# a3 = calAngle(113.322500, 23.081710, 113.321201, 23.080960)
# a4 = calAngle(113.322500, 23.081710, 113.321536, 23.082859)


# a5 = calAngle(113.322500, 23.081710, 113.322500, 23.083009)  # 0
# a6 = calAngle(113.322500, 23.081710, 113.322500, 23.080300)  # 180
# a7 = calAngle(113.322500, 23.081710, 113.321201, 23.081710)  # 270
# a8 = calAngle(113.322500, 23.081710, 113.323536, 23.081710)  # 90


# print(a1)
# print(a2)
# print(a3)
# print(a4)


# print(a5)
# print(a6)
# print(a7)
# print(a8)


# for i in range(360):

#     print(i,getRelative(113.317300,23.143800,i,113.318264,23.144949,45))
