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

    with urllib.request.urlopen(res, timeout=30) as mpage:

        mpage = mpage.read()
    pattern = re.compile(r'<a class=\"movie-box\" href=\"(.*?)\">.*?<div class=\"photo-frame\">.*?<img src=.*? title=\"(.*?)\">.*?</div>.*?<div class=\"photo-info\">.*?<span>.*?<br>.*?<date>.*?</date> / <date>.*?</date>.*?</span>.*?</div>.*?</a>', re.S)


    print(chardet.detect(mpage))
 #   print(mpage)
    m = pattern.findall(mpage.decode('utf-8', 'ignore'))
    print(m)
    f = open('resgame_20181216_230_' +
             str(datetime.date.today().day) +
             '.txt', 'a', encoding='utf-8')
    for i in m:
        print(i)

        res2 = urllib.request.Request(i[0])
        res2.add_header(
            "User-Agent",
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')
        with urllib.request.urlopen(res2, timeout=30) as mpage2:
            mpage2 = mpage2.read()
        pattern2 = re.compile(
            r'<span class=\"genre\"><a href=\"https://avmoo.xyz/cn/genre/.*?\">(.*?)</a></span>',
            re.S)
        m2 = pattern2.findall(mpage2.decode('utf-8', 'ignore'))
        print(m2)
        gene = ''
        for s in m2:
            gene = gene + s + ','
        subzm = ''
       # if '字幕' in i[2]:
        #    subzm = '字幕'
        f.write(i[0] + '||' + i[1] + '||' + gene + '\n')

    f.close()

    time.sleep(5)


if __name__ == '__main__':
    avname = 'https://avmoo.xyz/cn/genre/4y/page/'

    for i in range(2, 21):
        try:
            print(avname + str(i))
            crawl_joke_list(avname + str(i))
        except Exception:
            print(Exception)
        else:
            print(i)
