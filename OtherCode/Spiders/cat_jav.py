#-*-coding:utf-8-*-
import re

import html
import time
import datetime

import chardet
import urllib.request


def crawl_joke_list(page=1):

    url1 = page

    # headers1 = {
    #     "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    #     "host": '174.127.195.213',
    #     'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    #     'Accept-Encoding': 'gzip, deflate'}

    res = urllib.request.Request(url1)
    res.add_header(
        "User-Agent",
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')

    with urllib.request.urlopen(res, timeout=20) as mpage:

        mpage = mpage.read()
    pattern = re.compile(r'<a class=\"movie-box\" href=\"(.*?)\">.*?<div class=\"photo-frame\">.*?<img src=.*? title=\"(.*?)\">.*?</div>.*?<div class=\"photo-info\">.*?<span>.*?<br />.*?<div class=\"item-tag\">(.*?)</div>.*?<date>.*?</date> / <date>.*?</date>.*?</span>.*?</div>.*?</a>', re.S)
    #<span id="thread_10076800"><a href="thread-10076800-1-1.html">[MP4/1.76G] HMPD-10052 やりすぎ家庭教師 霧島さくら</a></span>

    print(chardet.detect(mpage))
 #   print(mpage)
    m = pattern.findall(mpage.decode('utf-8', 'ignore'))
    print(m)
    f = open('相部屋' +
             str(datetime.date.today().day) +
             '.csvcd ', 'a', encoding='utf-8')

    for i in m:
        print(i)

        res2 = urllib.request.Request(i[0])
        res2.add_header(
            "User-Agent",
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')
        with urllib.request.urlopen(res2, timeout=20) as mpage2:
            mpage2 = mpage2.read()
        pattern2 = re.compile(
            r'<span class=\"genre\"><a href=\"https://www.fanbus.co/genre/.*?\">(.*?)</a></span>',
            re.S)
        m2 = pattern2.findall(mpage2.decode('utf-8', 'ignore'))
        print(m2)
        gene = ''
        for s in m2:
            gene = gene + s + ','
        subzm = ''
        if '字幕' in i[2]:
            subzm = '字幕'
        f.write(i[0] + '||' + i[1] + '||' + subzm + '||' + gene + '\n')

    f.close()

    time.sleep(5)


if __name__ == '__main__':
    avname = 'https://www.fanbus.co/search/%E7%9B%B8%E9%83%A8%E5%B1%8B/'

    for i in range(6, 100):
       # try:
            print(avname + str(i))
            crawl_joke_list(avname + str(i))
       # except Exception:
        #    print(Exception)
      #  else:
            print(i)

# test change 202007041547


#change by notebook


#change by gitkraken


#change by vs code  local change this line

#change by vs code remote change this line

