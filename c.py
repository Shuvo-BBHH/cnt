import requests,mahdix
from bs4 import BeautifulSoup
coki='sb=pIMZZL_1cXOTLny-omhanT89;datr=pIMZZNDFxyBtSDN51617U59K;oo=v1;dpr=1;locale=en_US;c_user=100001244871589;m_page_voice=100001244871589;xs=5%3A6rViu3hp2vACpQ%3A2%3A1688183050%3A-1%3A5124%3A%3AAcXbq7F010Gtw0-CAOjJxVQFEyl4oIza8WQxhXBkYA;fr=0vPkSRFx16ow9Sebv.AWWCmfg65UuCUKpUS_nEnFVCEzQ.BkoAim.2l.AAA.0.0.BkoA3k.AWWQRVNGgoo;wd=1366x649;usida=eyJ2ZXIiOjEsImlkIjoiQXJ4NDd1ZGdldG5vMyIsInRpbWUiOjE2ODgyMTExNTl9;presence=C%7B%22lm3%22%3A%22g.4774997019287185%22%2C%22t3%22%3A%5B%5D%2C%22utc3%22%3A1688211379599%2C%22v%22%3A1%7D;'
url = 'https://mbasic.facebook.com/bk4human/friends'
headers = {
        'Cookie': coki
    }
session = requests.Session()
r = BeautifulSoup(session.get(url, headers=headers).text, 'html.parser')
follow_link = r.find('a')
print(r)
