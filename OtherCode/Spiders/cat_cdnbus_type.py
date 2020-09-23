# -*-coding:utf-8-*-
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
    pattern = re.compile(
        r'<a class=\"movie-box\" href=\"(.*?)\">.*?<div class=\"photo-frame\">.*?<img src=.*? title=\"(.*?)\">.*?</div>.*?<div class=\"photo-info\">.*?<span>.*?<br />.*?<div class=\"item-tag\">(.*?)</div>.*?<date>.*?</date> / <date>.*?</date>.*?</span>.*?</div>.*?</a>',
        re.S)
    # <span id="thread_10076800"><a href="thread-10076800-1-1.html">[MP4/1.76G] HMPD-10052 やりすぎ家庭教師 霧島さくら</a></span>

    print(chardet.detect(mpage))
    #   print(mpage)
    m = pattern.findall(mpage.decode('utf-8', 'ignore'))
    #print(m)
    f = open('resgame_20191210_gj_' +
             str(datetime.date.today().day) +
             '.txt', 'a', encoding='utf-8')
    for k in m:
        f.write(str(k)+'\n')
    f.close()

    time.sleep(5)


if __name__ == '__main__':
    avname = 'https://www.fanbus.co/search/%E7%9B%B8%E9%83%A8%E5%B1%8B/'

    for i in range(1, 200):
        # try:
        print(avname + str(i))
        crawl_joke_list(avname + str(i))
        # except Exception:
        #    print(Exception)
        #  else:
        print(i)
