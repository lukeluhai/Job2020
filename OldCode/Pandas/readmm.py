from dateutil import parser
import jieba
import datetime,time
import re
dicword={}
dicusr={}
dicrelation={}
dicwhoiscat={}
dicwhoiscattmp={}
dicemoji={}



dicword['1栋']=0
dicword['2栋']=0
dicword['3栋']=0
dicword['4栋']=0
dicword['5栋']=0
dicword['6栋']=0
dicword['7栋']=0
dicword['8栋']=0
dicword['9栋']=0
dicword['10栋']=0
dicword['11栋']=0
dicword['12栋']=0
dicword['一栋']=0
dicword['二栋']=0
dicword['三栋']=0
dicword['四栋']=0
dicword['五栋']=0
dicword['六栋']=0
dicword['七栋']=0
dicword['八栋']=0
dicword['九栋']=0
dicword['十栋']=0
dicword['十一栋']=0
dicword['十二栋']=0
dicword['1座']=0
dicword['2座']=0
dicword['3座']=0
dicword['4座']=0
dicword['5座']=0
dicword['6座']=0
dicword['7座']=0
dicword['8座']=0
dicword['9座']=0
dicword['10座']=0
dicword['11座']=0
dicword['12座']=0
dicword['一座']=0
dicword['二座']=0
dicword['三座']=0
dicword['四座']=0
dicword['五座']=0
dicword['六座']=0
dicword['七座']=0
dicword['八座']=0
dicword['九座']=0
dicword['十座']=0
dicword['十一座']=0
dicword['十二座']=0


fileobject= open('fjy.txt','r',encoding='utf-8')

for line in fileobject:
    s=line.split('	')

    fdate=s[0].strip()
    fusr = s[1].strip()
    if fdate.count("/") == 2:
        t = time.strptime(fdate, "%Y/%m/%d %H:%M")
        if t.tm_hour>=23 or t.tm_hour <6:
            if fusr+'|'+(str(t.tm_year)+' '+str(t.tm_mon)+' '+str(t.tm_mday)) not in dicwhoiscattmp:
                dicwhoiscattmp[fusr+'|'+(str(t.tm_year)+' '+str(t.tm_mon)+' '+str(t.tm_mday))]=1
    else:
        continue

#将@用户挑出来
    fstrtemp = s[4].strip()

    nlusr=re.findall('@.*?\?',fstrtemp)
    if len(nlusr)>0:
        for i in nlusr:
            fstrtemp=fstrtemp.replace(i,'')

            if fusr in dicrelation:
                dicrelation[fusr]=dicrelation[fusr]+nlusr
            else:
                dicrelation[fusr]=nlusr

    fstr=fstrtemp
#把表情符挑出来
    nemoji=re.findall('\[.*?\]',fstrtemp)
    if len(nemoji)>0:
        for nemoji_n in nemoji:
            fstr=fstr.replace(nemoji_n,'')
            if fusr+'-'+nemoji_n in dicemoji:
                dicemoji[fusr+'-'+nemoji_n]=dicemoji[fusr+'-'+nemoji_n]+1
            else:
                dicemoji[fusr + '-' + nemoji_n]=1

#分析聊天内容
    #删除无用符号
    seg_list=jieba.lcut(fstr,cut_all=False)
    for word in seg_list:
        if word in dicword:
            dicword[word]=dicword[word]+1
        else:
            dicword[word]=1



    if fusr in dicusr:
        dicusr[fusr]=dicusr[fusr]+1
    else:
        dicusr[fusr]=1



'''
    # 内容字段分析
    for n in range(2,6):
        if len(fstr)>n:
            for i in range(0,len(fstr)-n+1):
                ftempstr=fstr[i:i+n].strip()
                if ftempstr in dicword:
                    dicword[ftempstr]=dicword[ftempstr]+1
                else:
                    dicword[ftempstr] = 1
'''
#用户字段分析


listword=sorted (dicword.items(),key=lambda d:d[1],reverse=True)
#打印热门词汇
for hotword in listword:
    print('||'+hotword[0]+'||')


#打印关系
print('打印邻里关系')
list_relation=[]
for a,b in dicrelation.items():
    if len(b)>0:
        for nerghbour in b:
            list_relation.append(a+'-'+nerghbour)
dic_relation_count={}
for relation in list_relation:
    abcd=list_relation.count(relation)
    dic_relation_count[relation]=abcd

list_relation_count=sorted (dic_relation_count.items(),key=lambda d:d[1],reverse=True)

for relations in list_relation_count:
    print(relations)


#打印表情
print("打印各位使用表情次数：")
list_emoji_count=sorted(dicemoji.items(),key=lambda d:d[1],reverse=True)
for emojicount in list_emoji_count:
    print(emojicount)



#print(dicword)
#谁是夜猫子
print('谁是夜猫子：')
for k,v in dicwhoiscattmp.items():
    usrname=k.split('|')
    if usrname[0] in dicwhoiscat:
        dicwhoiscat[usrname[0]]=dicwhoiscat[usrname[0]]+1
    else:
        dicwhoiscat[usrname[0]] =1
listwhoiscat =sorted(dicwhoiscat.items(),key=lambda d:d[1],reverse=True)
for i in listwhoiscat:
    print(i)
#各种输出
'''
print('定制热点话题：')
print('停水'+'|'+str(dicword['停水']+dicword['停止供水']))
print('车位'+'|'+str(dicword['车位']))
print('幼儿园'+'|'+str(dicword['幼儿园']))
print('物业'+'|'+str(dicword['物业']))
print('广园'+'|'+str(dicword['广园']))

print('热门的人：')
print('管家'+'|'+str(dicword['管家']))
print('保安'+'|'+str(dicword['保安']))
print('阿姨'+'|'+str(dicword['阿姨']))
print('业主'+'|'+str(dicword['业主']))
print('司机'+'|'+str(dicword['司机']))
print('邻居'+'|'+str(dicword['邻居']))
print('那一栋事情最多：')
print('1栋'+'|'+str(dicword['1栋']-dicword['11栋']+dicword['一栋']-dicword['十一栋']+dicword['1座']-dicword['11座']+dicword['一座']-dicword['十一座']))
print('2栋'+'|'+str(dicword['2栋']-dicword['12栋']+dicword['二栋']-dicword['十二栋']+dicword['2座']-dicword['12座']+dicword['二座']-dicword['十二座']))
print('3栋'+'|'+str(dicword['3栋']+dicword['三栋']+dicword['3座']+dicword['三座']))
print('4栋'+'|'+str(dicword['4栋']+dicword['四栋']+dicword['4座']+dicword['四座']))
print('5栋'+'|'+str(dicword['5栋']+dicword['五栋']+dicword['5座']+dicword['五座']))
print('6栋'+'|'+str(dicword['6栋']+dicword['六栋']+dicword['6座']+dicword['六座']))
print('7栋'+'|'+str(dicword['7栋']+dicword['七栋']+dicword['7座']+dicword['七座']))
print('8栋'+'|'+str(dicword['8栋']+dicword['八栋']+dicword['8座']+dicword['八座']))
print('9栋'+'|'+str(dicword['9栋']+dicword['九栋']+dicword['9座']+dicword['九座']))
print('10栋'+'|'+str(dicword['10栋']+dicword['十栋']+dicword['10座']+dicword['十座']))
print('11栋'+'|'+str(dicword['11栋']+dicword['十一栋']+dicword['11座']+dicword['十一座']))
print('12栋'+'|'+str(dicword['12栋']+dicword['十二栋']+dicword['12座']+dicword['十二座']))




print('打印出现次数大于1000的单词：')
for lstr in listword:
    if lstr[1]>3000:
        print(lstr)

print('打印表情符出现次数:')
for lstr in listword:
    if len(lstr[0])>=1:
        if lstr[0][0]=='[' and lstr[0][-1]==']':
            print(lstr)
'''
print('谁最多话:')
listusr=sorted(dicusr.items(),key=lambda d:d[1],reverse=True)
for i in listusr:
    print(i)



fileobject.close()
