#-*-coding:utf-8-*-
import re

import html
import time
import datetime

import chardet
import urllib.request


def crawl_joke_list(page=1):

    url1 = page

    headers1 = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        "host": '174.127.195.213',
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept-Encoding': 'gzip, deflate'}

    res = urllib.request.Request(url1)
    res.add_header(
        "User-Agent",
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')

    with urllib.request.urlopen(res, timeout=10) as mpage:

        mpage = mpage.read()
    pattern = re.compile(r'<div class=\"item\">.*?<a class=\"avatar-box text-center\" href=\"(.*?)\">.*?<div class=\"photo-frame\">', re.S)
    #<span id="thread_10076800"><a href="thread-10076800-1-1.html">[MP4/1.76G] HMPD-10052 やりすぎ家庭教師 霧島さくら</a></span>

    print(chardet.detect(mpage))
 #   print(mpage)
    m = pattern.findall(mpage.decode('utf-8', 'ignore'))
    print(m)
    f = open('resgame_20191210_height_' +
             str(datetime.date.today().day) +
             '.txt', 'a', encoding='utf-8')

    for i in m:
        print(i)

        res2 = urllib.request.Request(i)
        res2.add_header(
            "User-Agent",
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')
        with urllib.request.urlopen(res2, timeout=10) as mpage2:
            mpage2 = mpage2.read()
        pattern2 = re.compile(
            r' <span class=\"pb10\">(.*?)</span>.*?<p>身高:(.*?)</p>',re.S)
        m2 = pattern2.findall(mpage2.decode('utf-8', 'ignore'))
        print(m2)
        gene = ''
        


        f.write(i + '||' + str(m2)+'\n')


    f.close()

    time.sleep(5)


if __name__ == '__main__':
    avname = 'https://www.cdnbus.in/actresses/'

    for i in range(113, 200):
       # try:
            print(avname + str(i))
            crawl_joke_list(avname + str(i))
       # except Exception:
        #    print(Exception)
      #  else:
            print(i)
