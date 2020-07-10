#-*-coding:utf-8-*-
import re

import html
import time
import datetime

import chardet
import urllib.request

def crawl_joke_list(page=1):

    url1 = "http://38.103.161.140/forum/forumdisplay.php?fid=27&filter=type&typeid=191&page="+str(page)

    headers1 = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
                "host": '174.127.195.213',
                'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
                'Accept-Encoding':'gzip, deflate'
    }

    res=urllib.request.Request(url1)
    res.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')

    with urllib.request.urlopen(res,timeout=10) as mpage:

        mpage=mpage.read()
    pattern = re.compile(r'成人游戏</a>]</em>.*?<span id=\"thread_.*?\"><a href=\"(.*?)\">(.*?)</a>', re.S)
    #<span id="thread_10076800"><a href="thread-10076800-1-1.html">[MP4/1.76G] HMPD-10052 やりすぎ家庭教師 霧島さくら</a></span>
#r'成人游戏</a>]</em>.*?<span id=\"thread_.*?\"><a href=\".*?\">.*?</a>

#    print(chardet.detect(mpage))
#    print(mpage)
    m = pattern.findall(mpage.decode('gbk','ignore'))

    print(m)
    f=open ('resgame_20170126_230_'+str(datetime.date.today().day)+'.txt','a')
    for page1 in m:
       # href=re.findall(r'成人游戏</a>]</em>.*?<span id=\"thread_.*?\"><a href=\"（.*?）\">.*?</a>',page1,re.S)
       # h_contet=re.findall(r'成人游戏</a>]</em>.*?<span id=\"thread_.*?\"><a href=\".*?\">（.*?）</a>',page1,re.S)
        f.write(page1[0]+'||||'+page1[1]+'\n')
        print(page1[0]+'||||'+page1[0])
    f.close()


    time.sleep(5)
if __name__ == '__main__':
    for i in range(27,1000):
        try:
            crawl_joke_list(i)
        except:
            print(i)
        else:
            print(i)
