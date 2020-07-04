#-*-coding:utf-8-*-
import re

import html
import time
import datetime

import chardet
import urllib.request

def crawl_joke_list(page=1):

    url1 = "http://38.103.161.140/forum/forum-230-"+str(page)+".html"

    headers1 = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
                "host": '174.127.195.213',
                'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
                'Accept-Encoding':'gzip, deflate'
    }

    res=urllib.request.Request(url1)
    res.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')

    with urllib.request.urlopen(res,timeout=10) as mpage:

        mpage=mpage.read()
    pattern = re.compile(r'<span id=\"thread_\d+\"><a href=\"thread-\d+-\d+-\d+\.html\".*?>.*?</a></span>', re.S)
    #<span id="thread_10076800"><a href="thread-10076800-1-1.html">[MP4/1.76G] HMPD-10052 やりすぎ家庭教師 霧島さくら</a></span>


    print(chardet.detect(mpage))
    print(mpage)
    m = pattern.findall(mpage.decode('GB2312','ignore'))


    f=open ('resgame_20170126_230_'+str(datetime.date.today().day)+'.txt','a')
    for page1 in m:
        href=re.findall('<a href=\"(.*?)\.html*?',page1,re.S)
        h_contet=re.findall('<span .*?><a .*?>(.*?)</a></span>',page1,re.S)
        f.write(href[0]+'||||'+h_contet[0]+'\n')
        print(href[0]+'||||'+h_contet[0])
    f.close()


    time.sleep(5)
if __name__ == '__main__':
    for i in range(1,1000):
        try:
            crawl_joke_list(i)
        except:
            print(i)
        else:
            print(i)
