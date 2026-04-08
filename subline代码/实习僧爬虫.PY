#加入工资的爬取，这里网站在工资数上加了反爬虫措施(字体反爬虫)，故显示不到
#获取相关代码后在print处一个一个输出代码转换.
##https://www.shixiseng.com/interns?page=1&keyword=python&type=intern第一页
#https://www.shixiseng.com/interns?page=2&keyword=python&type=intern第二页
#https://www.shixiseng.com/interns?page=3&keyword=python&type=intern第三页
import requests#首先导入包
from bs4 import BeautifulSoup
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
#加入工资的爬取，这里网站在工资数上加了反爬虫措施(字体反爬虫)，故显示不到
#获取相关代码后在print处一个一个输出代码转换.
##https://www.shixiseng.com/interns?page=1&keyword=python&type=intern第一页
#https://www.shixiseng.com/interns?page=2&keyword=python&type=intern第二页
#https://www.shixiseng.com/interns?page=3&keyword=python&type=intern第三页
import requests#首先导入包
from bs4 import BeautifulSoup
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
	 #先用注释记录标签.f-l.intern-detail__job p a
def detail_data(url):
	html=requests.get(url,headers=headers)
	soup=BeautifulSoup(html.text,'lxml')
	title=soup.select('.new_job_name span')[0].get_text()
	salary=soup.select('.job_money.cutom_font')[0].get_text().encode('utf8')
	
	academic=soup.select('.job_academic')[0].get_text()
	jtime=soup.select('div.job_msg span.job_time.cutom_font')[0].get_text().encode('utf8')
	jtime=jtime.replace(b'\xef\x8e\x8b',b'1')
	jtime=jtime.replace(b'\xee\xbc\x9f',b'2')
	jtime=jtime.replace(b'\xee\xbe\xb8',b'3')
	jtime=jtime.replace(b'\xee\xb6\xab',b'4')
	jtime=jtime.replace(b'\xee\xb7\x83',b'5')
	jtime=jtime.replace(b'\xef\x9e\xa2',b'6')
	jtime=jtime.replace(b'\xee\xa0\x97',b'7')
	jtime=jtime.replace(b'\xee\xb6\xae',b'8')
	jtime=jtime.replace(b'\xee\xae\xa8',b'0')

	salary=salary.replace(b'\xef\x8e\x8b',b'1')
	salary=salary.replace(b'\xee\xbc\x9f',b'2')
	salary=salary.replace(b'\xee\xbe\xb8',b'3')
	salary=salary.replace(b'\xee\xb6\xab',b'4')
	salary=salary.replace(b'\xee\xb7\x83',b'5')
	salary=salary.replace(b'\xef\x9e\xa2',b'6')
	salary=salary.replace(b'\xee\xa0\x97',b'7')
	salary=salary.replace(b'\xee\xb6\xae',b'8')
	salary=salary.replace(b'\xee\xae\xa8',b'0')
	
	salary=salary.decode('utf8')
	jtime=jtime.decode('utf8')
	print(title,salary,academic,jtime)
for i in range(1,20):
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)
			   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
		   
		detail_data(d['href'])