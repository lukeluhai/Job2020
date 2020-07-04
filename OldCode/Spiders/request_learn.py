import requests
from bs4 import BeautifulSoup

def read_sex():

    #aa=requests.request('GET','http://www.huihui.cn/deals/12431992?keyfrom=popup')
    aa=requests.get("https://avos.pw/cn/star/2jv")
    html=aa.text

    print(len(html))
    bf=BeautifulSoup(html,'html5lib')


    tezt=bf.find_all('a',class_='movie-box')

    for img_list in tezt:


        abc=img_list.find('img')
        print(abc['src'])
      #  print(abc.img['src'])


if __name__ == '__main__':
    read_sex()
