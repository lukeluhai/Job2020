# -*- coding:UTF-8 -*-
import html
import time
import requests
import chardet
import re
from bs4 import BeautifulSoup


class telecomhr:
    def __init__(self):
        self.company = ""
        self.position = ""
        self.positiontype = ""
        self.workingplace = ''
        self.hiring = ''
        self.salarylevel = ''
        self.recruitmenttype = ''
        self.newcomer = ''
        self.gender = ''
        self.age = ''
        self.language = ''
        self.languagelevel = ''
        self.network = ''
        self.manufacturer = ''
        self.degree = ''
        self.experience = ''
        self.posttime = ''
        self.lasttime = ''


company=""
position=""
positiontype=""
workingplace=''
hiring=''
salarylevel=''
recruitmenttype=''
newcomer=''
gender=''
age=''
language=''
languagelevel=''
network=''
manufacturer=''
degree=''
experience=''
posttime=''
lasttime=''



def geturltxt(url,nn,mm):
    teljob = []
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
                "host": 'www.telecomhr.com',
                'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
                'Accept-Encoding':'gzip, deflate'
    }
    print(url)

    req=requests.get(url=url,headers=headers)
    htmlmain=req.content.decode('GB2312','ignore')

    soup=BeautifulSoup(htmlmain,'html5lib')
    job_list=soup.find_all("a",style="font-weight:bold; color:#060; font-size:16px;")


    for i in job_list:
        if len(job_list)==0:
            break
        myjob=telecomhr()
        time.sleep(1)
        req_job=requests.get(i['href'],headers=headers)
        htmljob=req_job.content.decode('GB2312','ignore')
        soupjob=BeautifulSoup(htmljob,'html5lib')
        jobcontent=soupjob.find('div',class_='qyzpxq_con_yqdy_left')
        company = soupjob.find('strong', style="color:#933").em.contents[0]


        position=jobcontent.find('span').contents[0]
        jobcontents_list=jobcontent.find_all('p')

        positiontype = jobcontents_list[0].find('em').contents[0]


        workingplace = jobcontents_list[1].find('em').contents[0]
        hiring = jobcontents_list[2].find('em').contents[0]
        salarylevel = jobcontents_list[2].find('i').contents[0]
        recruitmenttype = jobcontents_list[3].find('em').contents[0]
        newcomer = jobcontents_list[3].find('i').contents[0]
        gender = jobcontents_list[4].find_all('em')[0].contents[0].strip()
        age = jobcontents_list[4].find_all('em')[1].contents[0]
        language = jobcontents_list[5].find_all('em')[0].contents[0]
        languagelevel = jobcontents_list[5].find_all('em')[1].contents[0]
        network = jobcontents_list[6].find('em').contents[0]
        manufacturer = jobcontents_list[7].find('em').contents[0]
        degree = jobcontents_list[8].find_all('em')[0].contents[0]
        experience = jobcontents_list[8].find_all('em')[1].contents[0].strip()
        posttime = jobcontents_list[9].find_all('em')[0].contents[0]
        lasttime = jobcontents_list[9].find_all('em')[1].contents[0]
        myjob.company = company
        myjob.position = position
        myjob.positiontype = positiontype
        myjob.workingplace = workingplace
        myjob.hiring = hiring
        myjob.salarylevel = salarylevel
        myjob.recruitmenttype = recruitmenttype
        myjob.newcomer = newcomer
        myjob.gender = gender
        myjob.age = age
        myjob.language = language
        myjob.languagelevel = languagelevel
        myjob.network = network
        myjob.manufacturer = manufacturer
        myjob.degree = degree
        myjob.experience = experience
        myjob.posttime = posttime
        myjob.lasttime = lasttime
        teljob.append(myjob)
        print(company+posttime)
    if len(teljob) >0 :
        for job_record in teljob:
            f = open('telhr_1223.txt', 'a')
            f.write(str(nn)+str(mm)+'||'+job_record.company + '||' + job_record.position + '||' + job_record.positiontype + '||' + job_record.workingplace + '||' + job_record.hiring + '||' + job_record.salarylevel + '||' + job_record.recruitmenttype + '||' + job_record.newcomer + '||' + job_record.gender + '||' + job_record.age + '||' + job_record.language + '||' + job_record.languagelevel + '||' + job_record.network + '||' + job_record.manufacturer + '||' + job_record.degree + '||' + job_record.experience + '||' + job_record.posttime + '||' + job_record.lasttime + "\n")
            print(str(nn)+str(mm)+'||'+job_record.company + '||' + job_record.position + '||' + job_record.positiontype + '||' + job_record.workingplace + '||' + job_record.hiring + '||' + job_record.salarylevel + '||' + job_record.recruitmenttype + '||' + job_record.newcomer + '||' + job_record.gender + '||' + job_record.age + '||' + job_record.language + '||' + job_record.languagelevel + '||' + job_record.network + '||' + job_record.manufacturer + '||' + job_record.degree + '||' + job_record.experience + '||' + job_record.posttime + '||' + job_record.lasttime)
    print(len(job_list))
    return len(job_list)






if __name__ == '__main__':
    l=[x for x in  range(1000,1034)]
    l.append(4256)


    for n in l:
        for m in range(1,6):
            try:
                geturltxt('https://www.telecomhr.com/jobs/index.php?bc=&sc=&jobarea='+str(n)+'&keyword=&page='+str(m),n,m)
            except:
                print(str(n)+" "+str(m)+" fail")
            else:
                print(str(n)+" "+str(m)+" ok")