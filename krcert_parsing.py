from httplib2 import Http
from json import dumps
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import urllib.parse
import re

def now_time():
    nowDatetime = datetime.now().strftime('%Y.%m.%d')
    return nowDatetime

def krcert():
    pattern = re.compile(r'\s+')
    html_=''

    for l in range(2):
        web_url ="https://www.krcert.or.kr/data/secNoticeList.do?page="+str(l+1)
        print(web_url)
        with urllib.request.urlopen(web_url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            first_div = soup.find("tbody")
            html_ = html_ + str(first_div)

    first_temp = str(html_).replace('/data/secNoticeView.do', "https://www.krcert.or.kr/data/secNoticeView.do")

    first_temp = re.sub(pattern, '', first_temp)

    first_temp_=first_temp.replace('class="first">','').replace('<imgalt="새글"src="/img/common/ico/icon_new.gif"/></td>','</td>').split('<tr')

    del first_temp_[0]
    t_list=[]
    j = 0
    print(first_temp_)
    for i in first_temp_:
        t1_ = i.replace('><tdclass="gray">','').replace('<tdclass="gray">','').replace('</tbody>','')
        t1__ = t1_.replace('</td><tdclass="colTit"><ahref="','---')
        t1___ = t1__.replace('">','---')
        t1____ = t1___.replace('</a></td','---')
        t1_____ = t1____.replace('</td><td></td','---')
        t1______ = t1_____.replace('</td></tr>','')
        t1_______ = t1______.split('---')

        t_list.append(t1_______[4]+" "+t1_______[2]+"("+t1_______[1]+")")

        j = j+1

    temp_1 =''

    for z in t_list:
        temp_1 = temp_1 + z+ "\n"

    return temp_1

def main():
    temp = krcert()
	print(temp)

if __name__ == '__main__':
    main()
