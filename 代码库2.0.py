#如何识别网站技术
from urllib import robotparser
import builtwith
from pprint import pprint
rp=robotparser.RobotFileParser()
rp.set_url('https://www.cnblogs.com/robots.txt')
url = 'https://www.cnblogs.com/'#输入要爬取的网页的url

html = builtwith.builtwith(url)
pprint(res)
print(rp.can_fetch('PythonCrawl',url))






#用户延迟访问插件
from urllib import parse
from datetime import datetime
import time,requests
class DelayRequests:
    def __init__(self,delay=3):
        self.delay=delay
        self.urls=dict()
    def wait(self,url):
        netloc=parse.urlparse(url).netloc
        #print(netloc)
        lastOne=self.urls.get(netloc)
        #print(lastOne)
        if self.delay>0 and lastOne:
            sleepTime=self.delay-\
                      (datetime.now()-lastOne).seconds
            if sleepTime>0:
                time.sleep(sleepTime)
        self.urls[netloc]=datetime.now()
urls=['https://blog.csdn.net/']*10
d=DelayRequests()
for url in urls:
    html=requests.get(url)
    d.wait(url)
    print(html.status_code)
