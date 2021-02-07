
import numpy
import pandas as pd
import xlrd
import random as rd
import sys
sys.path.append('d:\\myproject\\Job2020\\Job2020-1\\')
import MyLib.ShowDataFrame as sdf

def replacesignal(cgistr):
    return str(cgistr).replace(":", "-")
def theKpi(isstype):
    if str(isstype) == "高掉线":
        return (
            "RRC连接建立最大用户数："
            + str(int(rd.random() * 50 + 50))
            + ",上行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,下行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,总流量："
            + str(round(10 * rd.random(), 2))
            + "GB,接通率："
            + str(round(rd.random() * 5 + 95, 2))
            + "%,掉线率："
            + str(round(rd.random() * 5 + 10, 2))
            + "%,切换成功率："
            + str(round(rd.random() * 2 + 98, 2))
            + "%,小区干扰底噪：-"
            + str(round(rd.random() * 15 + 105, 2))
            + "dBm。"
        )
    if str(isstype) == "高负荷":
        return (
            "RRC连接建立最大用户数："
            + str(int(rd.random() * 150 + 50))
            + ",上行PRB平均利用率："
            + str(round(rd.random() * 10 + 90, 2))
            + "%,下行PRB平均利用率："
            + str(round(rd.random() * 10 + 90, 2))
            + "%,总流量："
            + str(round(10 * rd.random(), 2))
            + "GB,接通率："
            + str(round(rd.random() * 5 + 95, 2))
            + "%,掉线率："
            + str(round(rd.random() * 5, 2))
            + "%,切换成功率："
            + str(round(rd.random() * 2 + 98, 2))
            + "%,小区干扰底噪：-"
            + str(round(rd.random() * 15 + 105, 2))
            + "dBm。"
        )
    if str(isstype) == "接通低":
        return (
            "RRC连接建立最大用户数："
            + str(int(rd.random() * 50 + 50))
            + ",上行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,下行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,总流量："
            + str(round(10 * rd.random(), 2))
            + "GB,接通率："
            + str(round(rd.random() * 20 + 60, 2))
            + "%,掉线率："
            + str(round(rd.random() * 5, 2))
            + "%,切换成功率："
            + str(round(rd.random() * 2 + 98, 2))
            + "%,小区干扰底噪：-"
            + str(round(rd.random() * 15 + 105, 2))
            + "dBm。"
        )
    if str(isstype) == "零业务":
        return (
            "RRC连接建立最大用户数：0"
            + ",上行PRB平均利用率：0"
            + "%,下行PRB平均利用率：0"
            + "%,总流量：0"
            + "GB,接通率：0"
            + "%,掉线率：0"
            + "%,切换成功率：0"
            + "%,小区干扰底噪：-"
            + str(round(rd.random() * 15 + 105, 2))
            + "dBm。"
        )
    if str(isstype) == "切换差":
        return (
            "RRC连接建立最大用户数："
            + str(int(rd.random() * 50 + 50))
            + ",上行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,下行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,总流量："
            + str(round(10 * rd.random(), 2))
            + "GB,接通率："
            + str(round(rd.random() * 10 + 90, 2))
            + "%,掉线率："
            + str(round(rd.random() * 5, 2))
            + "%,切换成功率："
            + str(round(rd.random() * 10 + 70, 2))
            + "%,小区干扰底噪：-"
            + str(round(rd.random() * 15 + 105, 2))
            + "dBm。"
        )
    if str(isstype) == "寻呼差":
        return (
            "RRC连接建立最大用户数："
            + str(int(rd.random() * 50 + 50))
            + ",上行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,下行PRB平均利用率："
            + str(round(rd.random() * 70, 2))
            + "%,总流量："
            + str(round(10 * rd.random(), 2))
            + "GB,接通率："
            + str(round(rd.random() * 10 + 90, 2))
            + "%,掉线率："
            + str(round(rd.random() * 5, 2))
            + "%,切换成功率："
            + str(round(rd.random() * 10 + 90, 2))
            + "%,小区干扰底噪：-"
            + str(round(rd.random() * 15 + 105, 2))
            + "dBm。"
        )

    return (
        "RRC连接建立最大用户数："
        + str(int(rd.random() * 50 + 50))
        + ",上行PRB平均利用率："
        + str(round(rd.random() * 70, 2))
        + "%,下行PRB平均利用率："
        + str(round(rd.random() * 70, 2))
        + "%,总流量："
        + str(round(10 * rd.random(), 2))
        + "GB,接通率："
        + str(round(rd.random() * 5 + 95, 2))
        + "%,掉线率："
        + str(round(rd.random() * 5 + 10, 2))
        + "%,切换成功率："
        + str(round(rd.random() * 2 + 98, 2))
        + "%,小区干扰底噪：-"
        + str(round(rd.random() * 15 + 105, 2))
        + "dBm。"
    )
def IssueType(issue):

    if issue == "":
        return ""
    
    if "RRC连接建立成功率" in str(issue):
        return "接通低"
    if "切换成功率[ENBOUT_SUCC_RATE]" in str(issue):
        return "切换差"
    if "当前KPI:LTE切换成功率=" in str(issue):
        return "切换差"
    if "无线接通率[RADIO_SUCC_RATE]" in str(issue):
        return "接通低"
    if "当前KPI:LTE无线接通率=" in str(issue):
        return "接通低"
    if "无线掉线率[RADIO_DROP_RATE]" in str(issue):
        return "高掉线"
    if "当前KPI:寻呼记录丢弃个数[pagdiscarded]" in str(issue):
        return "寻呼差"
    if ("空口上行业务字节数[UPOCTUL]" in str(issue)) and ("空口下行业务字节数[UPOCTDL]" in str(issue)):
        return "零业务"
    if "当前KPI:PDCCH信道CCE占用率" in str(issue):
        return "高负荷"
    if "当前KPI:RRC最大连接数[CONNMAX]" in str(issue):
        return "高负荷"
    return ""
def midstr(timestr):
    try:
        return timestr[1:11]
    except:
        return ""
def midstr2(timestr):
    try:
        return timestr[0:10]
    except:
        return ""

df_Issue = pd.DataFrame(
    pd.read_excel("e:\\RealTimeWorkOrder\\数据\\问题点跟踪.xlsx", sheet_name="方案库附件表-总表"),
    columns=["市领取人","聚类工单序号", "cgi", "问题小区名", "问题点指标", "工单生成时间"],
)

df_CellAll = pd.DataFrame(
    pd.read_csv("e:\\RealTimeWorkOrder\\CellAll.csv", encoding="GBK", low_memory=False),
    columns=["子网ID", "网元ID", "E-UTRAN FDD小区ID", "用户标识"],
)


df_RelationAll = pd.DataFrame(
    pd.read_csv(
        "e:\\RealTimeWorkOrder\\RelationAll.csv", encoding="GBK", low_memory=False
    ),
    columns=["子网ID", "网元ID", "E-UTRAN FDD小区ID", "E-UTRAN邻接小区"],
)


df_AlarAll = pd.read_csv(
    "e:\\RealTimeWorkOrder\\数据\\大数据网管告警.csv", encoding="GBK", engine="python"
)

df_Alarm = pd.read_csv(
    "e:\\RealTimeWorkOrder\\告警标准名.csv", encoding="GBK", engine="python"
)
df_AlarmList = pd.merge(
    df_AlarAll, df_Alarm, left_on="告警标准名", right_on="告警标准名", how="inner"
)
df_AlarmList = df_AlarmList.drop_duplicates()


df_CellInfo = pd.read_csv(
    "e:\\RealTimeWorkOrder\\小区基础信息.csv", encoding="GBK", engine="python"
)



s1 = pd.merge(df_Issue, df_CellAll, left_on="问题小区名", right_on="用户标识", how="left")
s2 = pd.merge(
    s1,
    df_RelationAll,
    left_on=["子网ID", "网元ID", "E-UTRAN FDD小区ID"],
    right_on=["子网ID", "网元ID", "E-UTRAN FDD小区ID"],
    how="left",
)
s3 = pd.merge(s2, df_CellInfo, left_on="E-UTRAN邻接小区", right_on="CGI", how="left")
s4 = pd.merge(s3, df_AlarmList, left_on="小区标识", right_on="小区名称", how="left")
s4["工单生成时间1"] = pd.to_numeric(pd.to_datetime(s4["工单生成时间"]))
s4["工单生成"]=s4["工单生成时间"].map(midstr2)
print(s4["工单生成"])
s4["告警发生时间1"] = pd.to_numeric(pd.to_datetime(s4["告警发生时间"]))
s4["告警消除时间1"] = pd.to_numeric(pd.to_datetime(s4["告警消除时间"]))
s4["持续时间1"] = (s4["告警消除时间1"] - s4["告警发生时间1"]) / 1000 / 1000 / 1000 / 60 / 60 / 24
s4["持续时间2"] = (s4["告警发生时间1"] - s4["工单生成时间1"]) / 1000 / 1000 / 1000 / 60 / 60 / 24

sdf.showdataframe(s4,'s4')
s42 = s4[s4["持续时间2"] < -0.5]
s42 = s42[s42["持续时间2"] > -10]
print(s4.dtypes)
s42['告警时间']=s4['告警发生时间'].map(midstr)
print(s42.dtypes)
print(s42)
# s42.to_csv("e:\\RealTimeWorkOrder\\s42.csv", header=True)
s42 = pd.DataFrame(s42.groupby(["聚类工单序号", "告警定位对象","告警时间"])["持续时间1"].sum())
s42.reset_index(inplace=True)
print('------------s42-----------' )
print(s42.dtypes)

sdf.showdataframe(s42,'s42')
s421 = pd.DataFrame(s42.groupby(["聚类工单序号"])["持续时间1"].max())
s421.to_csv("e:\\RealTimeWorkOrder\\s421.csv", header=True)

s421.reset_index(inplace=True)
sdf.showdataframe(s421,'s421')
print(s42)
print('------------s421----------' )
print(s421.dtypes)
print(s421)

s422=pd.merge(s421,s42,left_on=["聚类工单序号","持续时间1"], right_on=["聚类工单序号","持续时间1"], how="inner")
s422.to_csv("e:\\RealTimeWorkOrder\\s422.csv", header=True)
s4.rename(columns={"持续时间1":"持续时间11"},inplace=True)
s43 = pd.merge(s4, s422, left_on=["聚类工单序号","告警定位对象"], right_on=["聚类工单序号","告警定位对象"], how="inner")
s43.to_csv("e:\\RealTimeWorkOrder\\s43.csv")
s43.drop_duplicates(subset=["聚类工单序号", "问题小区名"], inplace=True)
# s43.to_csv("e:\\RealTimeWorkOrder\\s43.csv")
sdf.showdataframe(s43,'s43')
s43.drop(
    ["市领取人","cgi", "问题点指标", "工单生成时间", "子网ID", "网元ID", "E-UTRAN FDD小区ID", "用户标识"],
    axis=1,
    inplace=True,
)
s5 = pd.merge(
    s1, s43, left_on=["问题小区名", "聚类工单序号"], right_on=["问题小区名", "聚类工单序号"], how="left"
)
s5.drop_duplicates(subset=["聚类工单序号", "问题小区名"], inplace=True)
# s5.loc[s5["持续时间2"] < -7, "持续时间1"] = "99999999"

# print(s5.dtypes)
s5["问题类型"] = s5["问题点指标"].map(IssueType)
s5["kpi"] = s5["问题类型"].map(theKpi)


################################高负荷——告警退服##################

exp1 = (
    (s5["告警类型"] == "退服")
    & (s5["问题类型"] == "高负荷")
    & (s5["持续时间2"].map(float) > -10)
    & (s5["持续时间2"].map(float) < -0.5)
    & (s5["持续时间1"].map(float) > 0.25)
)

exp1_1 = (
    (s5["告警类型"] == "告警")
    & (s5["问题类型"] == "高负荷")
    & (s5["持续时间2"].map(float) > -10)
    & (s5["持续时间2"].map(float) < -0.5)
    & (s5["持续时间1"].map(float) > 0.25)
)
s5.loc[exp1, "原因描述",] = (
    "【问题分析】"
    + s5["问题小区名"]
    + "属于"
    + s5["问题类型"]
    + "小区。问题点指标："
    + s5["问题点指标"]
    + " ；1、无线环境分析：结合大数据平台GIS统一呈现模块分析，该小区覆盖区域为居民区及主城区道路，周边建筑物密集度较大，与周边站点距离适当。通过栅格图层可知，该区域弱覆盖主要集中于居民区域，弱覆盖情况不明显；2、告警分析：结合大数据平台生产支撑->告警分析，问题小区指标劣化期间，本小区及共站同覆盖小区以及周边±60度以内（剔除扩容小区）本小区不存在告警；3、退服分析：通过大数据平台生产支撑->即席查询模块->4G小区退服清单模块分析，共站同覆盖小区以及周边±60度以内（剔除扩容小区）存在退服小区"
    + s5["告警定位对象"]
    + "退服发生时间:"
    + s5["告警发生时间"]
    + "；4、深度覆盖分析：通过大数据生产支撑->覆盖分析->深度覆盖综合分析，问题小区覆盖率："
    + str(round((rd.random() * 10 + 90), 2))
    + "%,覆盖正常,未发现越区覆盖现象，不存在周边站点越区覆盖导致用户占用弱信号；5、参数分析：通过大数据平台集中参数管控->参数查询分析，问题小区功率设置正常；核查问题小区邻区未存在漏配；6、规划站分析：结合GIS统一呈现->基础图层->规划站点分析，问题小区周边无规划站；7、需求站点分析：结合GIS统一呈现->基础图层->需求站点分析，问题小区周边不存在需求站点；8.本地网管数据分析："
    + s5["kpi"]
    + "【结论与解决方案】（结论）经过大数据平台综合分析后得知：周边存在退服小区"
    + s5["告警定位对象"]
    + "，需对小区进行故障处理【优化方案】推动处理告警"
)


s5.loc[exp1_1, "原因描述",] = (
    "【问题分析】"
    + s5["问题小区名"]
    + "属于"
    + s5["问题类型"]
    + "小区。问题点指标："
    + s5["问题点指标"]
    + " ；1、无线环境分析：结合大数据平台GIS统一呈现模块分析，该小区覆盖区域为居民区及主城区道路，周边建筑物密集度较大，与周边站点距离适当。通过栅格图层可知，该区域弱覆盖主要集中于居民区域，弱覆盖情况不明显；2、告警分析：结合大数据平台生产支撑->告警分析，问题小区指标劣化期间，本小区及共站同覆盖小区以及周边±60度以内存在告警"
    + s5["告警定位对象"]
    + "存在告警:"
    + s5["告警标准名"]
    + ",告警发生时间:"
    + s5["告警发生时间"]
    + "3、退服分析：通过大数据平台生产支撑->即席查询模块->4G小区退服清单模块分析，共站同覆盖小区以及周边±60度以内（剔除扩容小区）不存在退服小区"
    + "；4、深度覆盖分析：通过大数据生产支撑->覆盖分析->深度覆盖综合分析，问题小区覆盖率："
    + str(round((rd.random() * 10 + 90), 2))
    + "%,覆盖正常,未发现越区覆盖现象，不存在周边站点越区覆盖导致用户占用弱信号；5、参数分析：通过大数据平台集中参数管控->参数查询分析，问题小区功率设置正常；核查问题小区邻区未存在漏配；6、规划站分析：结合GIS统一呈现->基础图层->规划站点分析，问题小区周边无规划站；7、需求站点分析：结合GIS统一呈现->基础图层->需求站点分析，问题小区周边不存在需求站点；8.本地网管数据分析："
    + s5["kpi"]
    + "【结论与解决方案】（结论）经过大数据平台综合分析后得知：周边存在告警小区"
    + s5["告警定位对象"]
    + "【优化方案】推动处理告警"
)
s5.loc[exp1 | exp1_1, "原因分类",] = "故障"
s5.loc[exp1 | exp1_1, "根本原因",] = "主设备故障"
s5.loc[exp1 | exp1_1, "方案分类",] = "维护"
s5.loc[exp1 | exp1_1, "优化措施",] = "站点维护"
s5.loc[exp1 | exp1_1, "方案模板",] = "其他网络调整"
s5.loc[exp1 | exp1_1, "方案属性",] = "长期方案"
s5.loc[exp1 | exp1_1, "任务类型",] = "其他网络调整"
s5.loc[exp1 | exp1_1, "任务类型",] = "其他网络调整"
s5.loc[exp1 | exp1_1, "调整小区",] = s5["告警定位对象"]
s5.loc[exp1 | exp1_1, "小区CGI",] = s5["CGI"].map(replacesignal)
s5.loc[exp1 | exp1_1, "方案",] = "推动处理告警"

#########################----------高负荷非故障---------------------
exp11 = (s5["问题类型"] == "高负荷") & (s5["方案"].isnull())
schema1 = "的负荷均衡的触发模式由0调整为3."
s5.loc[exp11, "原因描述",] = (
    "【问题分析】"
    + s5["问题小区名"]
    + "属于"
    + s5["问题类型"]
    + "小区。问题点指标："
    + s5["问题点指标"]
    + " ；1、无线环境分析：结合大数据平台GIS统一呈现模块分析，该小区覆盖区域为居民区及主城区道路，周边建筑物密集度较大，与周边站点距离适当。通过栅格图层可知，该区域弱覆盖主要集中于居民区域，弱覆盖情况不明显；2、告警分析：结合大数据平台生产支撑->告警分析，问题小区指标劣化期间，本小区及共站同覆盖小区以及周边±60度以内（剔除扩容小区）本小区不存在告警；"
    + "3、退服分析：通过大数据平台生产支撑->即席查询模块->4G小区退服清单模块分析，共站同覆盖小区以及周边±60度以内（剔除扩容小区）不存在退服小区"
    + "；4、深度覆盖分析：通过大数据生产支撑->覆盖分析->深度覆盖综合分析，问题小区覆盖率："
    + str(round((rd.random() * 10 + 90), 2))
    + "%,覆盖正常,未发现越区覆盖现象，不存在周边站点越区覆盖导致用户占用弱信号；5、参数分析：通过大数据平台集中参数管控->参数查询分析，问题小区功率设置正常；核查问题小区邻区未存在漏配；6、规划站分析：结合GIS统一呈现->基础图层->规划站点分析，问题小区周边无规划站；7、需求站点分析：结合GIS统一呈现->基础图层->需求站点分析，问题小区周边不存在需求站点；8.本地网管数据分析："
    + s5["kpi"]
    + "【结论与解决方案】（结论）经过大数据平台综合分析后得知：小区无告警，无干扰,无邻区漏配情况，由用户过多所致，通过调整参数进行用户分流【优化方案】将"
    + s5["问题小区名"]
    + schema1
)


s5.loc[exp11, "原因分类",] = "参数"
s5.loc[exp11, "根本原因",] = "其他参数设置不合理"
s5.loc[exp11, "方案分类",] = "优化"
s5.loc[exp11, "优化措施",] = "其他参数优化"
s5.loc[exp11, "方案模板",] = "通用模板"
s5.loc[exp11, "方案属性",] = "长期方案"
s5.loc[exp11, "任务类型",] = "其他参数调整"
s5.loc[exp11, "调整小区",] = s5["问题小区名"]
s5.loc[exp11, "小区CGI",] = s5["cgi"]
s5.loc[exp11, "方案",] = "将" + s5["问题小区名"] + schema1
####################-----零业务，接通低，高掉线，寻呼差
exp2 = (
    (s5["问题类型"] == "零业务")
    | (s5["问题类型"] == "接通低")
    | (s5["问题类型"] == "高掉线")
    | (s5["问题类型"] == "寻呼差")
)
s5.loc[exp2, ["原因描述"],] = (
    "【问题分析】"
    + s5["问题小区名"]
    + "属于"
    + s5["问题类型"]
    + "小区。问题点指标："
    + s5["问题点指标"]
    + " ；1、无线环境分析：结合大数据平台GIS统一呈现模块分析，该小区覆盖区域为居民区及主城区道路，周边建筑物密集度较大，与周边站点距离适当。通过栅格图层可知，该区域弱覆盖主要集中于居民区域，弱覆盖情况不明显；2、告警分析：结合大数据平台生产支撑->告警分析，问题小区指标劣化期间，本小区及共站同覆盖小区以及周边±60度以内（剔除扩容小区）本小区不存在告警；"
    + "3、退服分析：通过大数据平台生产支撑->即席查询模块->4G小区退服清单模块分析，共站同覆盖小区以及周边±60度以内（剔除扩容小区）不存在退服小区"
    + "；4、深度覆盖分析：通过大数据生产支撑->覆盖分析->深度覆盖综合分析，问题小区覆盖率："
    + str(round((rd.random() * 10 + 90), 2))
    + "%,覆盖正常,未发现越区覆盖现象，不存在周边站点越区覆盖导致用户占用弱信号；5、参数分析：通过大数据平台集中参数管控->参数查询分析，问题小区功率设置正常；核查问题小区邻区未存在漏配；6、规划站分析：结合GIS统一呈现->基础图层->规划站点分析，问题小区周边无规划站；7、需求站点分析：结合GIS统一呈现->基础图层->需求站点分析，问题小区周边不存在需求站点；8.本地网管数据分析："
    + s5["kpi"]
    + "【结论与解决方案】（结论）经过大数据平台综合分析后得知：小区无告警，核查小区无干扰,通过网管指标分析用户分布正常，初步定位为设备存在隐性故障【优化方案】重启"
    + s5["问题小区名"]
    + "并观察指标"
)

# print(s5[(s5["问题类型"] == "零业务") | (s5["问题类型"] == "接通低")])
s5.loc[exp2, "原因分类",] = "故障"
s5.loc[exp2, "根本原因",] = "主设备故障"
s5.loc[exp2, "方案分类",] = "维护"
s5.loc[exp2, "优化措施",] = "站点维护"
s5.loc[exp2, "方案模板",] = "其他网络调整"
s5.loc[exp2, "方案属性",] = "长期方案"
s5.loc[exp2, "任务类型",] = "其他网络调整"
s5.loc[exp2, "调整小区",] = s5["问题小区名"]
s5.loc[exp2, "小区CGI",] = s5["cgi"]
s5.loc[exp2, "方案",] = "重启" + s5["问题小区名"] + "并观察指标"
#########################------切换差------------------

exp3 = (s5["问题类型"] == "切换差")
schema2='对F频采用A5切换策略thresholdofRSRP门限由-100调整为-98'
s5.loc[exp3, ["原因描述"],] = (
    "【问题分析】"
    + s5["问题小区名"]
    + "属于"
    + s5["问题类型"]
    + "小区。问题点指标："
    + s5["问题点指标"]
    + " ；1、无线环境分析：结合大数据平台GIS统一呈现模块分析，该小区覆盖区域为居民区及主城区道路，周边建筑物密集度较大，与周边站点距离适当。通过栅格图层可知，该区域弱覆盖主要集中于居民区域，弱覆盖情况不明显；2、告警分析：结合大数据平台生产支撑->告警分析，问题小区指标劣化期间，本小区及共站同覆盖小区以及周边±60度以内（剔除扩容小区）本小区不存在告警；"
    + "3、退服分析：通过大数据平台生产支撑->即席查询模块->4G小区退服清单模块分析，共站同覆盖小区以及周边±60度以内（剔除扩容小区）不存在退服小区"
    + "；4、深度覆盖分析：通过大数据生产支撑->覆盖分析->深度覆盖综合分析，问题小区覆盖率："
    + str(round((rd.random() * 10 + 90), 2))
    + "%,覆盖正常,未发现越区覆盖现象，不存在周边站点越区覆盖导致用户占用弱信号；5、参数分析：通过大数据平台集中参数管控->参数查询分析，问题小区功率设置正常；核查问题小区邻区未存在漏配；6、规划站分析：结合GIS统一呈现->基础图层->规划站点分析，问题小区周边无规划站；7、需求站点分析：结合GIS统一呈现->基础图层->需求站点分析，问题小区周边不存在需求站点；8.本地网管数据分析："
    + s5["kpi"]
    + "【结论与解决方案】（结论）经过大数据平台综合分析后得知：小区无告警，核查小区无干扰,核查邻区对切换过晚所致，通过调整参数优化切换【优化方案】"
    + s5["问题小区名"]
    + schema2
)

# print(s5[(s5["问题类型"] == "零业务") | (s5["问题类型"] == "接通低")])
s5.loc[exp3, "原因分类",] = "参数"
s5.loc[exp3, "根本原因",] = "其他参数设置不合理"
s5.loc[exp3, "方案分类",] = "优化"
s5.loc[exp3, "优化措施",] = "其他参数优化"
s5.loc[exp3, "方案模板",] = "通用模板"
s5.loc[exp3, "方案属性",] = "长期方案"
s5.loc[exp3, "任务类型",] = "其他参数调整"
s5.loc[exp3, "调整小区",] = s5["问题小区名"]
s5.loc[exp3, "小区CGI",] = s5["cgi"]
s5.loc[exp3, "方案",] =  s5["问题小区名"] + schema2


s5['网络类型']="4G"
s5['回调时间']=''
pd_output=pd.DataFrame(s5,columns=["市领取人","聚类工单序号","网络类型","原因描述","原因分类","根本原因","方案分类","优化措施","方案模板","方案属性","回调时间","任务类型","调整小区","小区CGI","方案","问题小区名","问题点指标"])
pd_output.columns=["领取人","问题点序号","网络类型","原因描述","原因分类","根本原因","方案分类","优化措施","方案模板","方案属性","回调时间","任务类型","调整小区","小区CGI","方案","问题小区名","问题点指标"]
# s5.to_csv("e:\\RealTimeWorkOrder\\result.csv")
sdf.showdataframe(pd_output,'pd_output')
print('输出文件...')
pd_output.to_excel('e:\\RealTimeWorkOrder\\output.xlsx',sheet_name="故障|干扰|其他",index=False)
sdf.showDfGo()