#requests模块代码
<link href="index-style.css"rel="stylesheet">#添加代码文件位置
p,h1{color:blue;font-family:KaiTi}#同时用P处理两个 
var alertText = "Hello makerbean"#这句话用var定义了一个字符串变量
alert(alertText)#这句话可以在网页弹出一个提示框
#JavaScript使用实列
var alertText = "makerbean"
if (alertText=="makerbean"){alert("Hello makerbean!")}else{alertT("OK")}
#JavaScript定义函数的方式
function alerUser(){alert("Hello makerbean!");}
alertUser();
#JavaScript定义函数之后的调用
<h1 onclick="alertUser()">每颗豆创客<h1>#在HTML中调用JavaScript函数
import requests
req = requests.get('http://docs.python-requests.org/en/master/')
print(type(req))
print(req.status_code)
print(req.encoding)
print(req.cookies)#状态码status_code编码方式encoding   
#requests库，提供http的所有请求方式
req = requests.post('http://docs.python-requests.org/en/master/')
req = requests.put('http://docs.python-requests.org/en/master/')
req = requests.delete('http://docs.python-requests.org/en/master')
req = requests.head('http://docs.python-requests.org/en/master')
req = requests.options('http://docs.python-requests.org/en/master')
#可利params参数
import requests
payload = {'key1':'value1','key2':'value2'}
r = requests.get("http://docs.python-requests。org/en/master/",params=payload)
print(r.url)
#POST请求
#1利用data参数为POST添加参数
data_form = {'key1':'value1','key2':value2}
req = requests.post("http://httpbin.org/post",data=data_form)
print(req.text)
#2上传文件(两种写法均可，python推荐第二种)
files = {'file':open('test.txt','rb')}
req = requests.post("http://httpbin.org/post",file=files)
with open('test.txt') as f:
	requests.post("http://httpbin.org/post",data=f)
	#获取www.baidu.com的cookies
import requests
url = 'httpS://www.baidu.com'
req = requests.get(ur1)
coo = req.cookies
print(coo)
for key in coo.keys():
	print(key)
	print(coo[key])
#发送cookies
url = 'http://httpbin.org/cookies'
cookies = dict(my_cookie='test')
req = requests.get(url,cookies=cookies)
print(req.text)
#利用timeout变量来配置最大请求时间
requests.get('http://www.baidu.com',timeout=0.001)
#会话对象
import requests
s = requests.Session
s.get('http://www.baidu.com/s?wd=pycharm')
print(s.cookies)
s.get('http://www.baidu.com/s?wd=puthon')
print(s.cookies)


req = requests.get('http//www.baidu.com/?wd=pycharm')
print(req.cookies)
req = requests.get('http://www.baidu.com/s?wd=python')
print(req.cookies)

#proxies参数使用代理
import requests
proxies = {"https":"http://101.6.162.19:22"}
r = requests.post("http://httpbin.org/post",proxies=proxies)
print(r.text)


#Beautiful Soup模块代码
#注意如何导入时的模块名称
from bs4 import BeautifulSoup
#prettify()格式化输出
r = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc")
html = r.text
# print(html)
soup = BeautifulSoup(html,"lxml")
print(soup.prettify())
#四大种类Tag(返回的是第一个符合要求的标签，即使HTML中有多个符合要求的标签)
r = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
html = r.text
#print(html)
soup = BeautifulSouop(html,"lxml")
print(soup.prettify())
print('### title ###')
print(soup.title)
print('### head ###')
print(soup.head)
print('### a ###')
print(soup.a)
#attrs(获取标签属性)
#get()方法获取标签的某个属性值
#可以通过修改字典的方式对这些属性和内容等等进行修改，删除等操作
print(soup.a.attrs)
print(soup.a['title'])
print(soup.a.get('title'))
soup.a['title']="a new title"
#获取某个标签的内容
print('a.string:{}'.format(soup.a.string))
print('a.string type:{}'.format(type(soup.a.string)))
#四大种类中的Comment
<h1 onclick="alerUser()">每颗豆创客</h1>
<p id="welcome-line">欢迎来到每颗豆创客学院</p>
<a class="link"href="https://makerbean.com"><!--每颗豆官网--></a>
<a class="link"href="https://ke.youdao.com">有道精品课官网</a>
<img onclick="alerUser()"src="html.png"> 
#文档树-直接子节点
from bs4 import BeautifulSoup
import requests
r = requests.get("http://www.crummy.com/software/BeautifulSoup/bs4/doc/")
html = r.text
soup = BeautifulSoup(html,'lxml')
#直接子节点
print(soup.head.contents)
print(soup.head.children)
for child in soup.head.children:
	print(child)
#文档树-所有子孙节点(。descendants把某个标签内的所有子孙节点都列出来，可以通过for循环来进行处理)
for child in soup.descendants:
	print(child)
#soup.a.string与soup.p.string的输出是一样的
#注意如果tag包含多个(能够调用.string的)节点，.string方法会返回什么(None)对于BeautifulSoup来说，空格和换行都算作一个节点
#如果想获得一个tag下面的多个内容，如何操作？.strings或者.stripped_strings
for string in soup.ol.strings:
	print(string)
for string in soup.ol.stripped_strings:
	print(string)
#文档树-父节点 .parent获得当前tag的父节点.parents可以获得当前元素的所有父节点
print(soup.p.parent.name)
<a><p>MakerBean</p></a>
#兄弟节点:和当前节点在同一级的节点
.next_sibling#获取下一个兄弟节点
.prev_sibling#获取上一个兄弟节点

#如何找出当前节点的所有之前的兄弟节点和之后的兄弟节点
print(soup.p.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling.prev_sibling)
#前后节点:该节点的之前(之后)的所有节点，不分层次，注意与兄弟节点的区别，对应方法如下
.next_sibling
.previous_element
.next_elements
.previous_element
#搜索文档树-find all(可以获得当前tag的所有tag子节点)
print（soup.find_all('a'）#find_all()里可以直接填的参数:标签名称，比如a，p，h1等列表['a','p'],True，找出所有子节点，正则表达式
#keyward参数，find_all(标签内属姓名=属性值)
<a accesskey="I" href="genindex.html" title="General Index"index</a>
print(soup.find_all(accesskey="I"))#找class记得写成class，因为class是python自带关键词
#text参数:对搜索文档中的所有tag字符串内容进行搜索匹配
#limit参数:限制返回结果数量
#recursive参数:如果只想搜索tag的直接子节点，可以使用参数recursive=False




#搜索文档树——其他方法
find(name,attrs,recursive,text,**kwargs)

find_parents() find_parent()

find_next_siblings() find_next_sibling()
find_previous_siblings()  find_previous_sibling()

fins_all_next() find_next()
find_all_previous() find_previous()











#CSS选择器
#soup.select()筛选元素，返回的是list
#语法规则:标签名 不加任何修饰，class名前加点，id面前加#
soup.select('title')
soup.find_all('title')

soup.select('a')
soup.find_all('a')

soup.select('.footer')#(点为class的意思)
soup.find_all(Ture,class_='footer')

soup.select('p,#link')#ID名前加"#"一个页面上，ID只有一个，不会重复
soup.find_all('p',id='link')

soup.select('head>title')
soup.head.find_all('title')

soup.select('a[href="www.baidu.com"]')
soup.find_all('a',href='www.baidu.com')













#案例----爬取糗事百科（url即为链接）
#目标网站:https://www.qiushibaike.com/hot/S
#目前正在维护，改变目标，xiaohua.zol.com.cn
#http://xiaohua.zol.com.cn/lengxiaohua/2.html  
#第三页http://xiaohua.zol.com.cn/lengxiaohua/3.html（所见即所得，先获取页面才能获取所爬的内容，即必须有url）
import requests
for i in range(1,4):
	url='http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
	print(url)
#CMD上运行 cd C:\Users\肖晓晨>\Users\肖晓晨\Desktop\编程\python 实验代码处.py即可





import requests#request，模仿人类行为，替我们完成一些简单重复的工作，用于发起请求，叫做爬虫库。
from bs4 import BeautifulSoup#用于页面解析(HTML解析)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}#请求头，在Get(相当于TCP的包)前添加
for i in range(1,4):
	url='http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
	
		#print(url)
	html=requests.get(url,headers=headers)

	
	res=html.text#.text即为答应其源代码
	
	soup=BeautifulSoup(res,'lxml')




import requests#find all示例
from bs4 import BeautifulSoup#用于页面解析(HTML解析)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}#请求头，在Get(相当于TCP的包)前添加
for i in range(1,4):
	url='http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
	#print(url)
	html=requests.get(url,headers=headers)
    res=html.text
    soup=BeautifulSoup(res,'lxml')
    print(soup.find_all('a'))
#Css选择器
<p>这是第一个标签</p>
<p class="para">这是第二个标签 </p>
#p.para即可

#带有多个标签的CSS选择器的选择方法
<p class="para">这是第一个p标签</p>
<p class="para tag">这是第二个p标签 </p>
#若打p.para，都会选到，若要选第二个p.para.tag即可
#p.para.tag的所有内部标签(子孙辈都算)，p.para.tag p
#p.para.tag的所有内部标签(子辈)p.para.tag>p



#标签
<p class="para">这是第一个p标签</p>
<<p class="para tag">
<p id="only_tag">这是第二个p标签 </p>
</p>
#选择带id的CSS的选择器的方法#only_tag


<div class="test">这是第一个p标签</p>
<<p class="para tag">
<p id="only_tag">这是第二个p标签 </p>
</div>#css选择器中div可以省略，test.para p




#重置缩进，成功爬取范例1
import requests#find all示例
from bs4 import BeautifulSoup#用于页面解析(HTML解析)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}#请求头，在Get(相当于TCP的包)前添加
for i in range(1,4):
	url='http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
		#print(url)
	html=requests.get(url,headers=headers)
	res=html.text
	soup=BeautifulSoup(res,'lxml')
	titles=soup.select('.article-title a')
	for t in titles:
	    print(t.get_text())#获取标签页内的文字




#重置缩进，成功爬取范例2
import requests#find all示例
from bs4 import BeautifulSoup#用于页面解析(HTML解析)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}#请求头，在Get(相当于TCP的包)前添加
for i in range(1,4):
	url='http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
		#print(url)
	html=requests.get(url,headers=headers)
	res=html.text
	soup=BeautifulSoup(res,'lxml')
	titles=soup.select('.article-title a')
	good_btns=soup.select(".good-btn span.text")
	for t in titles:
	    print(t.get_text())#获取标签页内的文字
	for g in good_btns:  
	 print(g.get_text()) 



#调试页面，用ctrl+F即有调试框,调试框内搜索内容前面一定要加"."比如 .good-btn span.text即为搜索"good-btn span.text"


#重置缩进，成功爬取范例3，针对二的改进，更加精确.此处获取了源代码，加了em，改写print
import requests#find all示例
from bs4 import BeautifulSoup#用于页面解析(HTML解析)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}#请求头，在Get(相当于TCP的包)前添加
for i in range(1,4):
	url='http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
		#print(url)
	html=requests.get(url,headers=headers)
	res=html.text
	soup=BeautifulSoup(res,'lxml')
	titles=soup.select('.article-title a')
	good_btns=soup.select("em.good-btn span.text")
	for t in titles:
	    print(t.get_text())#获取标签页内的文字
	for g in good_btns:  
	 print(g)










#重置缩进，成功爬取范例4，针对三的改进，获取内容。
import requests#find all示例
from bs4 import BeautifulSoup#用于页面解析(HTML解析)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}#请求头，在Get(相当于TCP的包)前添加
for i in range(1,4):
	url='http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
		#print(url)
	html=requests.get(url,headers=headers)
	res=html.text
	soup=BeautifulSoup(res,'lxml')
	titles=soup.select('.article-title a')
	contents=soup.select(' .summary-text')
	for t in titles:
	    print(t.get_text())#获取标签页内的文字
	for c in contents:  
	 print(c.get_text().strip())#增加.strip，删除前后段的空白





#实习僧的爬取案例
#https://www.shixiseng.com/interns?page=1&keyword=python&type=intern第一页
#https://www.shixiseng.com/interns?page=2&keyword=python&type=intern第二页
#https://www.shixiseng.com/interns?page=3&keyword=python&type=intern第三页
import requests#首先导入包
from bs4 import BeautifulSoup
for i in range(1,4):#再导入解析库
    url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
    print(url)


#上一个调试后，完整版，
#https://www.shixiseng.com/interns?page=1&keyword=python&type=intern第一页
#https://www.shixiseng.com/interns?page=2&keyword=python&type=intern第二页
#https://www.shixiseng.com/interns?page=3&keyword=python&type=intern第三页
import requests#首先导入包
from bs4 import BeautifulSoup
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
 #先用注释记录标签.f-l.intern-detail__job p a
for i in range(1,4):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
	   
	soup=BeautifulSoup(html.text,'lxml')

	##https://www.shixiseng.com/interns?page=1&keyword=python&type=intern第一页
#https://www.shixiseng.com/interns?page=2&keyword=python&type=intern第二页
#https://www.shixiseng.com/interns?page=3&keyword=python&type=intern第三页
import requests#首先导入包
from bs4 import BeautifulSoup
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
 #先用注释记录标签.f-l.intern-detail__job p a
for i in range(1,4):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
		   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
	    print(d['href'])#这里已经获取了a标签下的整整一条，现在只要获取连接故加入href,将.改为href












#下一步写个函数处理每一页该爬什么数据.
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
	print(title)

for i in range(1,4):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
			   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
		   # print(d['href'])#这里已经获取了a标签下的整整一条，现在只要获取连接故加入href,将.改为href
	    detail_data(d['href'])#传一个参数.






#加入工资的爬取，这里网站在工资数上加了反爬虫措施(字体反爬虫)，故显示不到
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
	salary=soup.select('.job_money.cutom_font')[0].get_text()
	print(title,salary)

for i in range(1,4):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
			   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
		   # print(d['href'])#这里已经获取了a标签下的整整一条，现在只要获取连接故加入href,将.改为href
	    detail_data(d['href'])#传一个参数.


#破解反爬虫(多答应几组找规律，此为第一组)
print('-'.encode('utf8'))
#b'\xee\xbc\x9f\xee\xae\xa8\xee\xae\xa8-\xee\xbc\x9f\xee\xae\xa8\xee\xae\xa8' (这是一个十六进制对应日薪为150-300)


#破解反爬虫(多答应几组找规律，此为第二组)
print('-'.encode('utf8'))
#b'\xef\x8e\x8b\xee\xae\xa8\xee\xae\xa8-\xef\x8e\x8b\xee\xb7\x83\xee\xae\xa8' (这是一个十六进制对应日薪为100-150)



#破解反爬虫(多答应几组找规律，此为第三组)
print('-'.encode('utf8'))
#b'\xef\x8e\x8b\xee\xb7\x83\xee\xae\xa8-\xee\xbc\x9f\xee\xb7\x83\xee\xae\xa8' (这是一个十六进制对应日薪为150-250)

#总体看一遍
#b'\xef\x8e\x8b\xee\xae\xa8\xee\xae\xa8-\xef\x8e\x8b\xee\xb7\x83\xee\xae\xa8' (这是一个十六进制对应日薪为100-150)
#b'\xef\x8e\x8b\xee\xb7\x83\xee\xae\xa8-\xee\xbc\x9f\xee\xb7\x83\xee\xae\xa8' (这是一个十六进制对应日薪为150-250)
#b'\xee\xbc\x9f\xee\xae\xa8\xee\xae\xa8-\xee\xbc\x9f\xee\xae\xa8\xee\xae\xa8' (这是一个十六进制对应日薪为150-300)
#对应查看结果如下
#100=\xef\x8e\x8b\xee\xae\xa8\xee\xae\xa8 150=\xef\x8e\x8b\xee\xb7\x83\xee\xae\xa8
#150=\xef\x8e\x8b\xee\xb7\x83\xee\xae\xa8 250=\xee\xbc\x9f\xee\xb7\x83\xee\xae\xa8
#150=\xee\xbc\x9f\xee\xae\xa8\xee\xae\xa8 300=\xee\xbc\x9f\xee\xae\xa8\xee\xae\xa8
#继续拆分，
#1=\xef\x8e\x8b 0=\xee\xae\xa8 0=\xee\xae\xa8 
#1=\xef\x8e\x8b 5=\xee\xb7\x83 0=\xee\xae\xa8 
#2=\xee\xbc\x9f 5=\xee\xb7\x83 0=\xee\xae\xa8 
#3=\xee\xbc\x9f 0=\xee\xae\xa8 0=\xee\xae\xa8
#把0~9全部取到分析即可(结果如下)





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
	salary=salary.replace(b'\xef\x8e\x8b',b'1')
	salary=salary.replace(b'\xee\xb7\x83',b'5')
	salary=salary.replace(b'\xee\xb7\x83',b'0')
	salary=salary.replace(b'\xee\xbc\x9f',b'3')
	salary=salary.replace(b'\xee\xbc\x9f',b'2')
    #用什么编码就用什么解码
	salary=salary.decode('utf8')
	print(title,salary)
for i in range(1,4):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
			   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
		   # print(d['href'])#这里已经获取了a标签下的整整一条，现在只要获取连接故加入href,将.改为href
	    detail_data(d['href'])#传一个参数.

#升级改进，获取学历
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
	salary=salary.replace(b'\xef\x8e\x8b',b'1')
	salary=salary.replace(b'\xee\xb7\x83',b'5')
	salary=salary.replace(b'\xee\xb7\x83',b'0')
	salary=salary.replace(b'\xee\xbc\x9f',b'3')
	salary=salary.replace(b'\xee\xbc\x9f',b'2')
    #用什么编码就用什么解码
	salary=salary.decode('utf8')
	print(title,salary,academic)
for i in range(1,20):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
			   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
		   # print(d['href'])#这里已经获取了a标签下的整整一条，现在只要获取连接故加入href,将.改为href
	    detail_data(d['href'])#传一个参数.



#增加实习时间的爬取，注意差别
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
	jtime=soup.select('div.job_msg span.job_time.cutom_font')[0].get_text()
	salary=salary.replace(b'\xef\x8e\x8b',b'1')
	salary=salary.replace(b'\xee\xb7\x83',b'5')
	salary=salary.replace(b'\xee\xb7\x83',b'0')
	salary=salary.replace(b'\xee\xbc\x9f',b'3')
	salary=salary.replace(b'\xee\xbc\x9f',b'2')
    #用什么编码就用什么解码
	salary=salary.decode('utf8')
	print(title,salary,academic,jtime)
for i in range(1,20):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
			   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
		   # print(d['href'])#这里已经获取了a标签下的整整一条，现在只要获取连接故加入href,将.改为href
	    detail_data(d['href'])#传一个参数.





#完整反爬虫
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
	#用什么编码就用什么解码
	salary=salary.decode('utf8')
	jtime=jtime.decode('utf8')
	print(title,salary,academic,jtime)
for i in range(1,20):#再导入解析库
	url='https://www.shixiseng.com/interns?page={}&keyword=python&type=intern'.format(i)
	html=requests.get(url,headers=headers)#先请求页面
			   
	soup=BeautifulSoup(html.text,'lxml')
	detail_urls=soup.select('.f-l.intern-detail__job p a')
	for d in detail_urls:
		   # print(d['href'])#这里已经获取了a标签下的整整一条，现在只要获取连接故加入href,将.改为href
		detail_data(d['href'])#传一个参数.




#scrapy使用结构
#tutorial/scrapy.cfg#部署配置文件
#tutorial/_init_.py项目的python模块，从这里加入自己的代码
#items.py 项目的pipeline文件
#settings.py 项目的settings文件
#spiders/_init_.py 放置spider代码的目录
#view-indeNtation处可以转换缩进方式






#scrapy库范列一
# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']
	start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']

	def parse(self, response):
		page=response.url.split("/")[-2]
		file_name="quotes-{}.html".formata(page)
		with open(file_name,'wb')as f:
			 f.write(response.body)
		self.log("Saved file{}".format(file_nameB))

#scrapy库范列二
# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']
	#start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
	def start_requests(self):
		 uels=['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
		 for url in urls:
			 yield scrapy.Request(url=url,callback=self.parse)

	def parse(self, response):
		page=response.url.split("/")[-2]
		file_name="quotes-{}.html".formata(page)
		with open(file_name,'wb')as f:
			 f.write(response.body)
		self.log("Saved file{}".format(file_nameB))	  

#CMD中按下向上的方向键会自动打出上一条已经发出的命令.
# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']
	#start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
	def start_requests(self):
		 uels=['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
		 for url in urls:
			 yield scrapy.Request(url=url,callback=self.parse)

	def parse(self, response):
		page=response.url.split("/")[-2]
		file_name="quotes-{}.html".formata(page)
		with open(file_name,'wb')as f:
			 quotes=response.css('.quote')
			 for index,quote in enumerate(quotes):#套一个enume，在for循环中加入index可知道已经循环第几次
				 text=quote.css('span.text::text').extrac_first()
				 author=quote.css('small.author::text').extrac_first()
				 tags=quotes.css('.tags .tag::text').extract()
				 f.write("No.{}".format(index+1)encode())
				 f.write("\r\n".encode())
				 f.write(text.encode())
				 f.write("\r\n".encode())
				 f.write("By {}".format(author).encode())
				 f.write("\r\n".encode())
				 tags_str=''
				 for tag in tags:
					 tags_str += tag+ ","
				 f.write("Tags:{}".format(tags_str).encode())
				 f.write("\r\n".encode())
				 f.write(("-"*20).encode())
				 f.write("\r\n".encode())
		self.log("Saved file{}".format(file_name))	  
#scrapy新建项目方式，CMD处输入 scrapy startproject news(NEWS为项目名，可以替换)

#scrapy爬取组件示例地址，C:\Users\肖晓晨\news\news\spiders
#切换到相关目录下，CMD输入news>scrapy crawl news2019运行.
#自动导入包，切换到目录，CMD处输入scrapy genspider -t crawl news19 news.163.com










#爬取网易新闻示例，未调试成功.
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import NewsItem

class News19Spider(CrawlSpider):
	name = 'news19'
	allowed_domains = ['news.163.com']
	start_urls = ['http://news.163.com/']

	rules = (
		Rule(LinkExtractor(allow=r'http://news.163.com/20/0115/\d+/.*?\.'), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		item=NewsItem()
		#item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
		#item['name'] = response.xpath('//div[@id="name"]').get()
		#item['description'] = response.xpath('//div[@id="description"]').get()
		item['news_thread']=response.url.strip().split('/')[-1][:-5]#strip,用于去除前后端的空白,split用于分割
		self.get_title(response,item)
		self.get_time(response,item)
		self.get_source(response,item)
		self.get_body(response,item)
		self.get_source_url(response,item)
		self.get_url(response,item)
		return item
	def get_title(self,response,item):
		title=response.css('.post_content_main h1::text').extract()
		if title:
			print('title:{}'.format(title[0][:-5]))
			item['news_title']=title[0][:-5]
	def get_time(self,response,item):
		time=response.css('div.post_time_source::text').extract()		
		if time:
			print("time:{}".format(time[0].strip().replace()))
			item['news_time']=time[0].strip().replace()
	def get_source(self,response,item):
		source=response.css('post_time_source').extract()	
		if source:
			source['news_source']=source[0]
	def get_body(self,responce,item):
		title=post_body.css('div.post_body::text').extract()
		if body:
			item['news_body']=body
	def get_source_url(self,responce,item):
		get_source_url=response.css('post_time_source::attr(href').extract()
		if source_url:
			item['source_url']=source_url[0]
	def get_url(self,responce,item):
		url=response.url
		if url:
			item['news_url']=url


#Numpy模块
import numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(data.ndim)#判断维度



import numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(data.shape)#判断各维度及长度
#创建全是0的数组
data = np.zeros(10)#括号内的10指的是长度
print(data)

 


mport numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(data.shape)#判断各维度及长度
#创建一个全是1的二维数组
data = np.ones((3,10))#代表三行十列
print(data)


import numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(data.shape)#判断各维度及长度
data = np.ones(10)#获取列表中的某个数字，行话，索引
print(data[5])#这里的五指的是五号位（注意，计算机从0号位开始计数）




import numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(data[0][1])#获取二维数组中的某个数字，行话，索引,此处括号内指第0行第一列
print(data[0,1])#此处括号内指第0行第一列，与上一行有着相同的含义。



import numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
data=np.arange(10)
print(data[3:6])#获取数组中的某几个数字，俗称，切片。,从三号位开始，到六号位结束

#文件夹目录中直接输入cmd回车会直接在该文件夹中运行cmd
#注意任何切片得到的数据对应的还是原始数据，任何修改都会反映到原始数据上


import numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
data=np.arange(10)
print(data[3:6])#获取数组中的某几个数字，俗称，切片。,从三号位开始，到六号位结束
data[3:6].copy()#复制一份副本不影响原始数据



mport numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
data=np.arange(10)
#变换数组的维度
print(data)
print(data.reshape((2,5)))



mport numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
data=np.arange(10)
#变换数组的维度
print(data)
print(data.reshape((2,5)).T)#变为五行两列，矩阵的转置






import numpy as np
data=np.array([[1,2,3,4,5],[1,2,3,4,5]])
data=np.arange(10)
#对ndarray数组每个元素都求平方根
print(np.sqrt(data))






#将两个数组相加(垂直相加)
import numpy as np
data1=np.array([[1,2,3,4,5,],[6,7,8,9,10]])
data2=np.array([[11,12,13,14,15],[14,15,16,17,18]])
print(data2+data1) 


import numpy as np
data=np.arange(100)
print(data.sum())#数学及统计方法，求和(此处求的是0~100)


import numpy as np
data=np.arange(100)
print(data.mean())#数学及统计方法，求平均值(此处求的是0~100)



import numpy as np
data=np.arange(100)
print(data.std())#数学及统计方法，求标准差(此处求的是0~100)


import numpy as np
data=np.array([9,7,1,8,5,1,3,0,9])
data.sort()
print(data)#数组的排序



import numpy as np
data=np.genfromtxt('data.txt',delimiter=',')
print(data)#读取txt文件



mport numpy as np
data=np.genfromtxt('data.txt',delimiter=',')
print(data.astype(int))#数组.astype(要转换的类型)，int转换成整数型的数据




#第一步读取数据并转换为整数
import numpy as numpy
data = np.genfromtxt('输入文件所在地址')
data = data.astype(int)
#第二步创建两个数组，分别存各个书籍的总得分和总评分人数
rating_sum = np.zeros(10000)
rating_people_count = np.zeros(10000)
#第三步，for循环读取每行数据
for rating in data:
	book_id = rating[1]-1
	rating_sum[book_id] += rating1[2]
	rating_people_count[book_id] += 1
#第四步，输出平均得分
rint(rating_sum/rating_people_count)
 


 #作业数据分析项目
 #第一步读取数据并转换为整数
import numpy as np
data = np.genfromtxt('D:/素材/数据分析项目/rating.txt',delimiter=',')
data = data.astype(int)
#第二步创建两个数组，分别存各个书籍的总得分和总评分人数
rating_sum = np.zeros(10000)
rating_people_count = np.zeros(10000)
#第三步，for循环读取每行数据
for rating in data:
	book_id = rating[1]-1
	rating_sum[book_id] += rating[2]
	rating_people_count[book_id] += 1
#第四步，输出平均得分
print(rating_sum/rating_people_count)
 


 #pandas模块
 import pandas as pd
#创建一个series类型的数据
data = pd.Series([1,3,5,7])
#两种方法效果一致
list_data = [1,3,5,7] 
data = pd.Series(list_data)
print(data)
#获取series数据的值
print(data.values)
#获取series数据的索引
print(data.index)
data = pd.Series(list_data,index=['a','j','k','z'])#创建特殊索引值
print(len(data))#获取series长度
print(data)
print(data['a'])#获取第a个数据
print(data[['a','b']])#获取第a个数据及第b个数据，注意里边还有括号




#计重复元素出现次数
import pandas as pd
#创建一个series类型的数据
list_data= pd.Series([1,3,5,7,1,1,3,3,3,5])
data = pd.Series(list_data)
print(data.value_counts())#计重复元素出现次数


#计重复元素出现次数
import pandas as pd
#创建一个series类型的数据
list_data= pd.Series([1,3,5,7,1,1,3,3,3,5])
data = pd.Series(list_data)
data = pd.Series(list_data,index=['a','b','c','d','e','f','g','h','i','j'])#创建特殊索引值
print(data.value_counts())#计重复元素出现次数
print('a'in data)#判断a索引值是否存在




#从字典创建一个series类型的数据
import pandas as pd
dict_data = {"Beijing":1000,"Shanghai":800,"Shenzhen":500}#从字典创建一个series类型的数据
data = pd.Series(dict_data)
print(data)


import pandas as pd
dict_data = {"Beijing":1000,"Shanghai":800,"Shenzhen":500}#从字典创建一个series类型的数据
index_list = ["Guangzhou","Beijing","Shanghai","Shenzhen"]#广州的字符不存在，故系统会用NaN反应，NO a number
data = pd.Series(dict_data,index=index_list)#给数据传入索引值
print(data)
print(data.isnull())#检测哪些数据是空的，检测非空用notnull() ,广州字符是空的，故用Ture,其他字符存在，故为False



import pandas as pd
import numpy as np
dict_data = {"Beijing":1000,"Shanghai":800,"Shenzhen":500}#从字典创建一个series类型的数据
index_list = ["Guangzhou","Beijing","Shanghai","Shenzhen"]#广州的字符不存在，故系统会用NaN反应，NO a number
data = pd.Series(dict_data,index=index_list)#给数据传入索引值
print(data) 
print(data.isnull())#检测哪些数据是空的，检测非空用notnull()
print(data*2)#数组运算，此处为乘二
print(np.square(data))#数组运算亦支持numpy数组运算



#设定series对象的name和索引名称 
data.name = 'City Data'
data.index.name = 'City'
print(data)



#创建一个DataFrame类型的数据
import pandas as pd
dict_data = {'student':['lilei','hanmeimei','madongmei']
,'score':[98,99,100],'gender':['M','F','F']}#创建一个DataFrame类型的数据
data = pd.DataFrame(dict_data,columns=['gender','student','score'])#指定DataFrame数据的列顺序
print(data)
print(data.columns)#获取DataFrame数据的列名称.
print(data['student'])#获取DataFrame数据中.student一列的数据，下面的指令有着相同效果
print(data.student)
#1，根据行编号
print(data.iloc[0])
#2.根据行索引
print(data.loc['a'])
slice_data = data['score']
print(slice_data)#切片得到的数据对应的还是原始的数据，任何修改都会反应到原始数据上。
data['score'] = 95#将data中的数据修改为95
print(data)
del data['score']#删除dataframe中的score那列数据
print(data)
#根据新的索引重新排列数据
data = data.reindex(['c','a','b'],fill_value=0)#将缺失位置填上0
print(data)


#创建一个DataFrame类型的数据
import pandas as pd
dict_data = {'student':['lilei','hanmeimei','madongmei']
,'score':[98,99,100],'gender':['M','F','F']}#创建一个DataFrame类型的数据
data = pd.DataFrame(dict_data,index = ['a','b','c'])#传入series类型修改dataframe数据中的score
score_data = pd.Series([100,90,80],index =['c','a','b'] )#传入series类型修改dataframe数据中的score
print(data)
print(score_data)



data = data.reindex(['c','a','b'],method='ffill')#fill从前面数据计算插值 bfill从后面计算插值
print(data)




#扔掉包含缺失的数据（NaN)
print(data。dropna())#扔掉包含缺失数据（NaN)的行，有一个空的就删掉
print(data.dropna(how='all'))#扔掉全部都是缺失的数据（NaN)的行




print(data.fillna(0))#填充所有缺失数据为一个值
print(data.fillna({'gender':M,'student'='unknown'，'score'：60}))#填充所有缺失数据为一个值，gender处填充M，student填充unknown,score填充60




data = data.drop('d')#删除第d行数据
print(data)





print(data['score']>=90)#这里相当于使用series只会显示Ture or False
print(data[data['score']>=90])#筛选score中大于等于90的数据


select_list = [95,98,100]
print(data[data['score'].isin(select_list)])#从列表中筛选数据,此处为在score中选择95 98 100的数值


import pandas as pd
data= pd.DataFrame({
'tag_id':['a','b','c','a','a','c'],
'count':[10,30,20,10,15,22]

	})
grouped_data = data.groupby('tag_id')
print(grouped_data.sum())#把对应标签数字加起来求一个和，groupby是对某一列进行重组
print(data.sort_index())#数据排序，按索引名称升序排列
data = data.sort_values(by='score')#按score那列的数据进行排序
print(data.sum())#数据汇总
print(data)







#同一个轴可以用多种方式索引
import pandas as pd
import numpy as np
data= book_ratings = pd.Series(np.random.randint(1,6,size=7),
	index=[['b1','b1','b2','b2','b3','b4','b4'],[1,2,1,2,1,2,3]]
	)
print(book_ratings)





#两个DataFrame可以合并
import pandas as pd
book_name = pd.DataFrame({'book_name':['a','b','c','d','e','f'],'book_id':[11,22,33,44,55,66]})
id_rating = pd.DataFrame({'book_id':[11,22,22,44,55,66,33,11,55],'rating':[1,3,5,2,4,3,2,4,5]})
print(pd.merge(book_name,id_rating,how='outer'))#merge用于合并，会把两个数组都有的索引值合起来，把没有的去掉,加参数how=outer就会把一方没有的参数也加进去





#Empty DataFrame此处显示,因为大小写字母不能合并，无法显示
mport pandas as pd
book_name = pd.DataFrame({'book_name':['a','b','c','d','e','f'],'book_id':[11,22,33,44,55,66],'key':['A','B','C','a','b','c']})
id_rating = pd.DataFrame({'book_id':[11,22,22,44,55,66,33,11,55],'rating':[1,3,5,2,4,3,2,4,5],'key':['D','E','F','d','e','f','d1','f2','e3']})
print(pd.merge(book_name,id_rating,on='key'))#指定两个DataFrame连接的列的名称，此处为KEY列




#两个DataFrame可以合并
import pandas as pd
data1 = pd.DataFrame({'lkey':['a','b','c','d','e','f'],'book_id':[11,22,33,44,55,66]})
data2 = pd.DataFrame({'rkey':['a','b','c','d','e','f','g','h','i'],'rating':[1,3,5,2,4,3,2,4,5]})
print(pd.merge(data1,data2,left_on='lkey',right_on='rkey'))#两个DataFrame可以合并，并且指定连接列的名称，这里在左边指定为lkey,在右边指定为rkey


#pandas文件存取
#此处为CSV读取文件
import pandas as pd
data = pd.read_csv('rating.csv',header=None，,ndex_col='user_id',sep=',')#文件名此处为rating.csv，不要标题行，即不要把第一行当作标题，以user_id作为索引列,指定分隔符为','
print(data)
data.to_csv('student.csv')#将数据存储为CSV文件




#pandas文件存取
#读取Excel文件
import pandas as pd
file = pd.ExcelFile('student.xlsx')#文件名，此处为student.xlsx
data = file.parse('student')#，默认shift+1
print(data)







#作业pandas
#第一步，找出最热门的五十本书
import pandas as pd
file = pd.ExcelFile('to_read.csv')

to_read = pd.read_csv('to_read.csv')#读取csv文件
to_read_counts = to_read['book_id'].value_counts().sort_values(ascending=False)#找到book_id列进行value_counts（数值收集）
hottest_50_books_id= to_read_counts[:50].index#对数值进行排序
hottest_50_books_counts= to_read_counts[:50].values#记录数值重复出现的次数
hottest_50_books = pd.DataFrame({
	'book_id':hottest_50_books_id,'to_read_counts':hottest_50_books_counts})#做了两列dataframe一列为book_id，一列为to_read_counts
print(hottest_50_books)

books = pd.read_csv('books.csv')#第二步找到最热的50本书
book_id_and_title = books[['book_id','goodreads_book_id','title']]#选取需要的几列数据
hottest_50_books_with_title = pd.merge(hottest_50_books,book_id_and_title,on='book_id',how='left')#用merge合并，整合book_id合并在left（左边）
print(hottest_50_books_with_title)
hottest_50_books_with_title.to_csv('hottest_50_books_with_title.to_csv')

#第三步，找到5这50本书对应最热的10个标签
book_tags = pd.read_csv('book_tags.csv')
book_tags = book_tags[book_tags['_goodreads_book_id_'].isin(hottest_50_books_with_title['goodreads_book_id'])]
del book_tags['_goodreads_book_id_']
hottest_10_tags = book_tags.groupby('tag_id').sum()#用sum求和
hottest_10_tags = hottest_10_tags.sort_values(by='count',ascending=False)[:10]#倒序排列取前十个
print(hottest_10_tags)




#pyecharts模块的运用

from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

bar = Bar()
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
bar.render()#此时目录下会生成一个HTML文件打开就是了



#改动主要为添加了标题,切换主题颜色，这里切换为PURPLE(紫色)，调整标题角度
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-基本示例",subtitle="我是副标题"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION,width="1920px",height="1080px"))#切换主题颜色，这里切换为PURPLE(紫色),px即为像素，通过高与宽改变 
bar.render()#此时目录下会生成一个HTML文件打开就是了



#改动主要为添加了标题,，调整标题角度
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-基本示例",subtitle="我是副标题"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list

bar.render()#此时目录下会生成一个HTML文件打开就是了




#改动主要为添加了标题,，调整标题角度,堆叠数据
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-基本示例",subtitle="我是副标题"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
bar.add_yaxis("商家A",Faker.values(),stack='stack1')
bar.add_yaxis("商家B",Faker.values(),stack='stack1')#传入两组数据，stack=stack1表示两组数据堆叠在stack1这一组数据里
bar.render()#此时目录下会生成一个HTML文件打开就是了




#改动主要为添加了标题,，调整标题角度，去掉stack1则会得到并排数据
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-基本示例",subtitle="我是副标题"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
#bar.add_yaxis("商家A",Faker.values(),stack='stack1')
#bar.add_yaxis("商家B",Faker.values(),stack='stack1')#传入两组数据，stack=stack1表示两组数据堆叠在stack1这一组数据里
bar.add_yaxis("商家A",Faker.values())
bar.add_yaxis("商家B",Faker.values())#去掉stack1则会得到并排数据
bar.render()#此时目录下会生成一个HTML文件打开就是了




#改动主要为添加了标题,，调整标题角度，去掉stack1则会得到并排数据，数据两两堆叠
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-基本示例",subtitle="我是副标题"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
bar.add_yaxis("商家A",Faker.values(),stack='stack1')
bar.add_yaxis("商家B",Faker.values(),stack='stack1')#传入两组数据，stack=stack1表示两组数据堆叠在stack1这一组数据里
bar.add_yaxis("商家C",Faker.values(),stack='stack2')#数据两两堆叠
bar.add_yaxis("商家D",Faker.values(),stack='stack2')
#bar.add_yaxis("商家A",Faker.values())
#bar.add_yaxis("商家B",Faker.values())#去掉stack1则会得到并排数据
bar.render()#此时目录下会生成一个HTML文件打开就是了




#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-基本示例",subtitle="我是副标题"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
bar.add_yaxis("商家A",Faker.values(),stack='stack1')
bar.add_yaxis("商家B",Faker.values(),stack='stack1')#传入两组数据，stack=stack1表示两组数据堆叠在stack1这一组数据里
bar.add_yaxis("商家C",Faker.values(),stack='stack2')#数据两两堆叠
bar.add_yaxis("商家D",Faker.values(),stack='stack2')
#bar.add_yaxis("商家A",Faker.values())
#bar.add_yaxis("商家B",Faker.values())#去掉stack1则会得到并排数据
bar.set_series_opts(
	label_opts=opts.LabelOpts(is_show=False),#不显示数字,若要标记线，改markpoint为markline_opts
	markpoint_opts=opts.MarkPointOpts(#若要标记线，改markpoint为markline_opts
		data=[	
		opts.MarkPointItem(type_="max",name="最大值"),
		opts.MarkPointItem(type_="min",name="最小值"),
		opts.MarkPointItem(type_="average",name="平均值"),

]


	   ),
    markline_opts=opts.MarkLineOpts(data=[
                                         opts.MarkLineItem(type_="average",name="平均值"),
    	]
    	),




	)
bar.render()#此时目录下会生成一个HTML文件打开就是了





#改动主要为添加了标题,，调整标题角度，去掉stack1则会得到并排数据，数据两两堆叠,x轴y轴交换
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-基本示例",subtitle="我是副标题"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['衬衫','毛衣','裤子','风衣','高跟鞋','袜子'])
bar.add_yaxis("商家A",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
bar.add_yaxis("商家A",Faker.values(),stack='stack1')
bar.add_yaxis("商家B",Faker.values(),stack='stack1')#传入两组数据，stack=stack1表示两组数据堆叠在stack1这一组数据里
bar.add_yaxis("商家C",Faker.values(),stack='stack2')#数据两两堆叠
bar.add_yaxis("商家D",Faker.values(),stack='stack2')
#bar.add_yaxis("商家A",Faker.values())
#bar.add_yaxis("商家B",Faker.values())#去掉stack1则会得到并排数据
bar.set_series_opts(
	label_opts=opts.LabelOpts(is_show=False),#不显示数字,若要标记线，改markpoint为markline_opts
	markpoint_opts=opts.MarkPointOpts(#若要标记线，改markpoint为markline_opts
		data=[	
		opts.MarkPointItem(type_="max",name="最大值"),
		opts.MarkPointItem(type_="min",name="最小值"),
		opts.MarkPointItem(type_="average",name="平均值"),

]


	   ),
    markline_opts=opts.MarkLineOpts(data=[
                                         opts.MarkLineItem(type_="average",name="平均值"),
    	]
    	),




	)
bar.reversal_axis()#x轴y轴交换
bar.render()#此时目录下会生成一个HTML文件打开就是了















#改动主要为添加了标题,，调整标题角度，去掉stack1则会得到并排数据，数据两两堆叠,x轴y轴交换,窗口滑块效果
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-参考项目",subtitle="进行项目"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['项目A','项目B','项目C','项目D','项目E','项目F'])
bar.add_yaxis("对象X",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
bar.add_yaxis("对象A",Faker.values(),stack='stack1')
bar.add_yaxis("对象B",Faker.values(),stack='stack1')#传入两组数据，stack=stack1表示两组数据堆叠在stack1这一组数据里
bar.add_yaxis("对象C",Faker.values(),stack='stack2')#数据两两堆叠
bar.add_yaxis("对象D",Faker.values(),stack='stack2')
#bar.add_yaxis("商家A",Faker.values())
#bar.add_yaxis("商家B",Faker.values())#去掉stack1则会得到并排数据
bar.set_series_opts(
	label_opts=opts.LabelOpts(is_show=False),#不显示数字,若要标记线，改markpoint为markline_opts
	markpoint_opts=opts.MarkPointOpts(#若要标记线，改markpoint为markline_opts
		data=[	
		opts.MarkPointItem(type_="max",name="最大值"),
		opts.MarkPointItem(type_="min",name="最小值"),
		opts.MarkPointItem(type_="average",name="平均值"),

]


	   ),
    markline_opts=opts.MarkLineOpts(data=[
                                         opts.MarkLineItem(type_="average",name="平均值"),
    	]
    	),




	)
bar.set_global_opts(#从这一行开始，包括这一行，为窗口滑块效果
	title_opts=opts.TitleOpts(
        title="Bar-参考项目",
        subtitle="进行项目",
    datazoom_opts=[opts.DataZoom_Opts()]
		)
	)

bar.render()#此时目录下会生成一个HTML文件打开就是了


#改动主要为添加了标题,，调整标题角度，去掉stack1则会得到并排数据，数据两两堆叠,x轴y轴交换,窗口滑块效果
from pyecharts import options as opts
from pyecharts.charts import Bar#(柱状图)
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType#切换主题颜色用
bar = Bar()
#如果只是想看看，添加虚假数据切换为一下两句
#bar.add_xaxis(Faker.choose())
#bar.add_yaxis("商家A"，Faker.values())
#添加大标题副标题
bar.set_global_opts(title_opts=opts.TitleOpts(
title="Bar-参考项目",subtitle="进行项目"),
xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30))#rotate=旋转角度（-90~90）之间，旋转X轴标签
)#
#添加数据
bar.add_xaxis(['项目A','项目B','项目C','项目D','项目E','项目F'])#利用tolist转换为python列表数据
bar.add_yaxis("对象X",[92,134,141,96,54,59,117])#add_xais(x轴数据列表)add_yais(y轴数据列表)注意数据应该要是python的list列表类型，如果是numpy的数组要转换成list
bar.add_yaxis("对象A",Faker.values(),stack='stack1')
bar.add_yaxis("对象B",Faker.values(),stack='stack1')#传入两组数据，stack=stack1表示两组数据堆叠在stack1这一组数据里
bar.add_yaxis("对象C",Faker.values(),stack='stack2')#数据两两堆叠
bar.add_yaxis("对象D",Faker.values(),stack='stack2')
#bar.add_yaxis("商家A",Faker.values())
#bar.add_yaxis("商家B",Faker.values())#去掉stack1则会得到并排数据
bar.set_series_opts(
	label_opts=opts.LabelOpts(is_show=False),#不显示数字,若要标记线，改markpoint为markline_opts
	markpoint_opts=opts.MarkPointOpts(#若要标记线，改markpoint为markline_opts
		data=[	
		opts.MarkPointItem(type_="max",name="最大值"),
		opts.MarkPointItem(type_="min",name="最小值"),
		opts.MarkPointItem(type_="average",name="平均值"),

]


	   ),
    markline_opts=opts.MarkLineOpts(data=[
                                         opts.MarkLineItem(type_="average",name="平均值"),
    	]
    	),




	)
bar.set_global_opts(#从这一行开始，包括这一行，为窗口滑块效果
	title_opts=opts.TitleOpts(
        title="Bar-参考项目",
        subtitle="进行项目",
    datazoom_opts=[opts.DataZoomOpts()]
		)
	)

bar.render()#此时目录下会生成一个HTML文件打开就是了






#3D图pyecharts
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar3D#创建3D图
import random
#创建数据,下列一行为列表推导式，for i in range(6) 中前面加i*2会得到[0,2,4,6,8,10,12]，i**2代表整体平方
data = [(i,j,random.randint(0,12)) for i in range(24) for j in range(6)]#数据格式，一个列表，每一项都是一个三个元素组成的列表/元祖，X为坐标，Y为坐标，Z轴为高度,range(6)代表生成从0~6的列表[0,1,2,3,4,5,6]
#添加图表并渲染
bar3d = Bar3D()
bar3d.add(
	"",#此为图表总名称
	data,#这里放刚刚生成的data
	xaxis3d_opts=opts.Axis3DOpts(Faker.clock,type_="category"),
	yaxis3d_opts=opts.Axis3DOpts(Faker.week_en,type_="category"),
	zaxis3d_opts=opts.Axis3DOpts(type_="value"),


	)
bar3d.set_global_opts(
	visualmap_opts=opts.VisualMapOpts(max_=20),
	title_opts=opts.TitleOpts(title="Bar3D-基本示例"),#此为标题

	)
bar3d.render()












#折线图，曲线图
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Line#折线图，导入line
#替换下列中的color，用渐变的颜色color={'type':'linear','x':0,'y':0,'x2':0,'y2':1,'colorStops':[{'offset':0,'color':'red'},{'offset':1,'color':'blue'}]}
line = Line()
line.add_xaxis(Faker.choose())
line.add_yaxis("商家A",Faker.values(),is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.2,color='#000'))#比较圆滑的效果，加参数is_smooth=True，即曲线效果,opacity，此处为0.2即%20的透明度:填充区域透明度,color:填充区域颜色
line.add_yaxis("商家B",Faker.values())
line.set_global_opts(title_opts=opts.TitleOpts(title="line-基本示例"))
line.render()


#折线图，曲线图渐变色

from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Line#折线图，导入line
#替换下列中的color，用渐变的颜色color={'type':'linear','x':0,'y':0,'x2':0,'y2':1,'colorStops':[{'offset':0,'color':'red'},{'offset':1,'color':'blue'}]}
line = Line()
line.add_xaxis(Faker.choose())
line.add_yaxis("商家A",Faker.values(),is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.2,color={'type':'linear','x':0,'y':0,'x2':0,'y2':1,'colorStops':[{'offset':0,'color':'red'},{'offset':1,'color':'blue'}]}))#比较圆滑的效果，加参数is_smooth=True，即曲线效果,opacity，此处为0.2即%20的透明度:填充区域透明度,color:填充区域颜色
line.add_yaxis("商家B",Faker.values())
line.set_global_opts(title_opts=opts.TitleOpts(title="line-基本示例"))
line.render()



#饼状图
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Pie#饼状图
pie = Pie()
pie.add("",[list(z) for z in zip(Faker.choose(),Faker.values())])#系列数据项[(key1,value1),(key2,value2)],
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))#整个饼图的标题
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))#formatter标签中以什么格式来写
pie.render()



#把A1与A2组的对应数字打包为一个元祖
zip(A1,A2)




#圆环饼状图加入参数radius=["40%","75%"]
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Pie
pie = Pie()
pie.add("",[list(z) for z in zip(Faker.choose(),Faker.values())],
	radius=["40%","75%"]#加入参数radius=["40%","75%"]
	)
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))#整个饼图的标题
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))#formatter标签中以什么格式来写
pie.render()


#玫瑰饼状图加入参数rosetype="area"
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Pie
pie = Pie()
pie.add("",[list(z) for z in zip(Faker.choose(),Faker.values())],
	radius=["40%","75%"],rosetype="area"#加入参数rosetype="area"
	)
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))#整个饼图的标题
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))#formatter标签中以什么格式来写
pie.render()




#pyecharts动态涟漪特效效果散点图.
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType
effect_scatter = EffectScatter()
effect_scatter.add_xaxis(Faker.choose())#x轴坐标
effect_scatter.add_yaxis(#Y轴坐标
    "",
    Faker.values(),
    symbol=SymbolType.ARROW)#ARROW指箭头标识，除此之外，还有'cicle','rect','roundRect','triangle','diamond','pin','arrow','none'标识，改成大写就行
effect_scatter.set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
	
effect_scatter.render()






#漏斗图
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Funnel#漏斗图的导入
funnel = Funnel()
funnel.add("商品",[list(z) for z in zip(Faker.choose(),Faker.values())])#直接添加列表里的一个数据
funnel.set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))#图表的总标题
funnel.render()




#地理坐标系模块
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Geo#地理坐标系模块
geo = Geo()
geo.add_schema(maptype="china")#说明地图类型，此为中国地图
geo.add("geo",[list(z) for z in zip(Faker.provinces,Faker.values())])#选择省份，可以打中文
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))#是否展示数字，此处为不显示数字False
geo.set_series_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title="Geo-基本示例"),


	)
geo.render()






#地理坐标系模块
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Geo#地理坐标系模块
geo = Geo()
geo.add_schema(maptype="china")#说明地图类型，此为中国地图
geo.add("geo",[list(z) for z in zip(['广东','江苏','湖南'],Faker.values())])#选择省份，可以打中文
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))#是否展示数字，此处为不显示数字False
geo.set_series_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title="Geo-基本示例"),


	)
geo.render()






#地理坐标系模块,中国热力图
from pyecharts.globals import ChartType 
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Geo#地理坐标系模块
geo = Geo()
geo.add_schema(maptype="china")#说明地图类型，此为中国地图
geo.add("geo",[list(z) for z in zip(['广东','江苏','湖南'],Faker.values())],type_=ChartType.HEATMAP)#选择省份，可以打中文,选择地理类型，热力图HEATMAP

geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))#是否展示数字，此处为不显示数字False
geo.set_series_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title="Geo-基本示例"),


	)
geo.render()






#水球图
from pyecharts import options as opts
from pyecharts.charts import Liquid
liquid = Liquid()
liquid.add("Liquid",[0.7,0.6,0.5])#各比例
liquid.set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))#大标题的名字
liquid.render()


#调整水球图
from pyecharts import options as opts
from pyecharts.charts import Liquid
liquid = Liquid()
liquid.add("Liquid",[0.7,0.6,0.5],is_outline_show=False)#各比例is_outline_show是否显示外边框，is_animation_show是否显示动画效果，shape=("输入路径")边框形状和symbol可用的形状类似，还可以自定义.去Iconfont.cn找,选择SVG下载，用Sublime打开复制Path及其之后的数字，字符串开头为path://
liquid.set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))#大标题的名字
liquid.render()







#雷达图，这里创建了两张雷达图的数据，v1里有两个数据，v2里有一个数据

from pyecharts import options as opts
from pyecharts.charts import Page,Radar
v1 = [

        [4300,10000,28000,35000,50000,19000],
        [3300,13000,25000,30000,48000,24000]

]
v2 = [[5000,14000,28000,31000,42000,21000]]
radar = Radar()
radar.add_schema(
schema=[
opts.RadarIndicatorItem(name="销售",max_=6500),#各个角标的名称，并且设定最大值
opts.RadarIndicatorItem(name="管理",max_=16000),
opts.RadarIndicatorItem(name="信息技术",max_=30000),
opts.RadarIndicatorItem(name="客服",max_=38000),
opts.RadarIndicatorItem(name="研发",max_=52000),
opts.RadarIndicatorItem(name="市场",max_=25000),
]
	)
radar.add("预算分配",v1)
radar.add("实际开销",v2)
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
radar.set_global_opts(title_opts=opts.TitleOpts(title="Radar-基本示例"))
radar.render()




#创建一个词云图
from pyecharts import options as opts
from pyecharts.charts import WordCloud
words=[

("Sam S Club",10000),#第一项为名称，第二项为对应数值
("Macys",6181),
("Amy Sxhumer",4386),
("Jurassic world",4055),
("Character Communications",2467),

]
wordcloud = WordCloud()
wordcloud.add("",words,word_size_range=[20,100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-基本示例"))
wordcloud.render()




#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
#print(comment_data)#先把数据导出来看看，[404972 rows x 7 columns]有404972行，7列的数据
#统计各个电影的评论数
movie_list = comment_data['MOVIEID'].value_counts()#利用value_counts()进行重复计数
#print(movie_list)#导出来，看看。1292222     1780，1292222重复了1780次
#现在筛选评论数大于100的电影
movie_list = comment_data['MOVIEID'].value_counts()
movie_list = movie_list[movie_list.values>100]
#print(movie_list)
#print(movie_list.count())#直接统计评论数大于100的电影的数量，993部


#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次

#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
#print(comment_data)#先把数据导出来看看，[404972 rows x 7 columns]有404972行，7列的数据
#调用函数
#print(get_movie_id_list(1000))#Index(['1292222', '1292052'], dtype='object'),即评论数超过一千的其实只有两个电影，'1292222',和 '1292052'
#如和通过ID查看豆瓣电影页面？观察豆瓣网址规律，得出https://mobie.douban.com/subject/1292222,即，替换后面的数字即可.
#简单测试jieba模块
#import jieba
#print(list(jieba.cut('关于希望最强有力的注释。')))
#根据ID筛选评论
movie_id='1292052'
comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
#整合全部评论为一个字符串，以换行隔开
comment_str_all = ''
for comment in comment_list:
	 comment_str_all += comment + '\n'
print(comment_list)#输出评论先看看


	







#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
#print(comment_data)#先把数据导出来看看，[404972 rows x 7 columns]有404972行，7列的数据
#调用函数
#print(get_movie_id_list(1000))#Index(['1292222', '1292052'], dtype='object'),即评论数超过一千的其实只有两个电影，'1292222',和 '1292052'
#如和通过ID查看豆瓣电影页面？观察豆瓣网址规律，得出https://mobie.douban.com/subject/1292222,即，替换后面的数字即可.
#简单测试jieba模块
#import jieba
#print(list(jieba.cut('关于希望最强有力的注释。')))
#根据ID筛选评论
movie_id='1292052'
comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
#print(comment_list)#输出评论先看看
#整合全部评论为一个字符串，以换行隔开
comment_str_all = ''
for comment in comment_list:
	comment_str_all += comment + '\n'#加上换行符号
#获取分词后的列表
seg_list = list(jieba.cut(comment_str_all))
#转换成Pandas的Series类型数据
keywords_counts = pd.Series(seg_list)
#统计各个关键词的出现次数
keywords_counts = keywords_counts.value_counts()
print(keywords_counts)









#筛选关键词	，方案一
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次

#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
#print(comment_data)#先把数据导出来看看，[404972 rows x 7 columns]有404972行，7列的数据
#调用函数
#print(get_movie_id_list(1000))#Index(['1292222', '1292052'], dtype='object'),即评论数超过一千的其实只有两个电影，'1292222',和 '1292052'
#如和通过ID查看豆瓣电影页面？观察豆瓣网址规律，得出https://mobie.douban.com/subject/1292222,即，替换后面的数字即可.
#简单测试jieba模块
#import jieba
#print(list(jieba.cut('关于希望最强有力的注释。')))
#根据ID筛选评论
movie_id='1292052'
comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
#print(comment_list)#输出评论先看看
#整合全部评论为一个字符串，以换行隔开
comment_str_all = ''
for comment in comment_list:
	comment_str_all += comment + '\n'#加上换行符号
#获取分词后的列表
seg_list = list(jieba.cut(comment_str_all))
#转换成Pandas的Series类型数据
keywords_counts = pd.Series(seg_list)
#利用str.len()筛选字符串长度
keywords_counts = pd.Series(seg_list)
keywords_counts = keywords_counts[keywords_counts.str.len()>1]#筛选内容分析：1，分词长度大于一（只有一个字意义并不大），2，关键词应有实际意义
#统计各个关键词的出现次数
keywords_counts = keywords_counts.value_counts()
print(keywords_counts)












#方案二，建立关键词过滤列表
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
#方案二，建立关键词过滤列表
FILTER_WORDS=['知道','影评','电影','影片','这么','那么','怎么','如果','\n','一部','这部','没有','还有']#根据实际情况来调整过滤词列表，具体问题具体分析。
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
#print(comment_data)#先把数据导出来看看，[404972 rows x 7 columns]有404972行，7列的数据
#调用函数
#print(get_movie_id_list(1000))#Index(['1292222', '1292052'], dtype='object'),即评论数超过一千的其实只有两个电影，'1292222',和 '1292052'
#如和通过ID查看豆瓣电影页面？观察豆瓣网址规律，得出https://mobie.douban.com/subject/1292222,即，替换后面的数字即可.
#简单测试jieba模块
#import jieba
#print(list(jieba.cut('关于希望最强有力的注释。')))
#根据ID筛选评论
movie_id='1292052'
comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
#print(comment_list)#输出评论先看看
#整合全部评论为一个字符串，以换行隔开
comment_str_all = ''
for comment in comment_list:
	comment_str_all += comment + '\n'#加上换行符号
#获取分词后的列表
seg_list = list(jieba.cut(comment_str_all))
#转换成Pandas的Series类型数据
keywords_counts = pd.Series(seg_list)
#利用str.len()筛选字符串长度
keywords_counts = pd.Series(seg_list)
keywords_counts = keywords_counts[keywords_counts.str.len()>1]#筛选内容分析：1，分词长度大于一（只有一个字意义并不大），2，关键词应有实际意义
#统计各个关键词的出现次数
keywords_counts = keywords_counts.value_counts()
print(keywords_counts)
#利用str.contains()筛选数据
#keywords_counts.str.contains('|'.join(FILTER_WORDS))#str.contains()里填一个字符或者正则表达式，这里指用'|'把词组连接起来
print('|'.join(FILTER_WORDS))








#筛选数据，join()方法
word_list = ['a','b','c','d','e']
word = '|'.jion(word_list)
print(word)
#输出结果a|b|c|d





#列表前加~表示取反
#方案二，建立关键词过滤列表
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
#方案二，建立关键词过滤列表
FILTER_WORDS=['知道','影评','电影','影片','这么','那么','怎么','如果','\n','一部','这部','没有','还有']#根据实际情况来调整过滤词列表，具体问题具体分析。
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
#print(comment_data)#先把数据导出来看看，[404972 rows x 7 columns]有404972行，7列的数据
#调用函数
#print(get_movie_id_list(1000))#Index(['1292222', '1292052'], dtype='object'),即评论数超过一千的其实只有两个电影，'1292222',和 '1292052'
#如和通过ID查看豆瓣电影页面？观察豆瓣网址规律，得出https://mobie.douban.com/subject/1292222,即，替换后面的数字即可.
#简单测试jieba模块
#import jieba
#print(list(jieba.cut('关于希望最强有力的注释。')))
#根据ID筛选评论
movie_id='1292052'
comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
#print(comment_list)#输出评论先看看
#整合全部评论为一个字符串，以换行隔开
comment_str_all = ''
for comment in comment_list:
	comment_str_all += comment + '\n'#加上换行符号
#获取分词后的列表
seg_list = list(jieba.cut(comment_str_all))
#转换成Pandas的Series类型数据
keywords_counts = pd.Series(seg_list)
#利用str.len()筛选字符串长度
keywords_counts = pd.Series(seg_list)
keywords_counts = keywords_counts[keywords_counts.str.len()>1]#筛选内容分析：1，分词长度大于一（只有一个字意义并不大），2，关键词应有实际意义
keywords_counts = keywords_counts[~keywords_counts.str.contains('|'.join(FILTER_WORDS))]#反向选择不包含过滤词列表中词语的数据，前面加"~"表示取反，如列表中的Ture改为False
#统计各个关键词的出现次数
keywords_counts = keywords_counts.value_counts()[:30]#汇总
print(keywords_counts)
#利用str.contains()筛选数据
#keywords_counts.str.contains('|'.join(FILTER_WORDS))#str.contains()里填一个字符或者正则表达式，这里指用'|'把词组连接起来
print('|'.join(FILTER_WORDS))









#导入pyecharts并绘制词云图
#列表前加~表示取反
#方案二，建立关键词过滤列表
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
import pyecharts as pec
FILTER_WORDS=['知道','影评','电影','影片','这么','那么','怎么','如果','\n','一部','这部','没有','还有']#根据实际情况来调整过滤词列表，具体问题具体分析。
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
	#筛选出前十个评论里最多的关键词
def  get_comment_keywords_counts(movie_id,count):
	 comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
	 comment_str_all = ''
	 for comment in comment_list:
		 comment_str_all += comment + '\n'
	 seg_list = list(jieba.cut(comment_str_all))
	 #转换成Pandas的Series类型数据
	 keywords_counts = pd.Series(seg_list)
	 #利用str.len()筛选字符串长度
	 keywords_counts = pd.Series(seg_list)
	 keywords_counts = keywords_counts[keywords_counts.str.len()>1]
	 return keywords_counts
#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
movie_id = '1292052'
keywords_counts = get_comment_keywords_counts(movie_id,30)#取前30个关键词
wordcloud = pec.WordCloud(width=1280,height=720)
wordcloud.add("",keywords_counts.index,keywords_counts.values,
	word_size_range=[20,100],
	shape='diamond')
wordcloud.render()
#根据ID筛选评论
movie_id='1292052'
comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
#print(comment_list)#输出评论先看看
#整合全部评论为一个字符串，以换行隔开
comment_str_all = ''
for comment in comment_list:
	comment_str_all += comment + '\n'#加上换行符号
#获取分词后的列表
seg_list = list(jieba.cut(comment_str_all))
#转换成Pandas的Series类型数据
keywords_counts = pd.Series(seg_list)
#利用str.len()筛选字符串长度
keywords_counts = pd.Series(seg_list)
keywords_counts = keywords_counts[keywords_counts.str.len()>1]#筛选内容分析：1，分词长度大于一（只有一个字意义并不大），2，关键词应有实际意义
keywords_counts = keywords_counts[~keywords_counts.str.contains('|'.join(FILTER_WORDS))]#反向选择不包含过滤词列表中词语的数据，前面加"~"表示取反，如列表中的Ture改为False
#统计各个关键词的出现次数
keywords_counts = keywords_counts.value_counts()[:30]#汇总
print(keywords_counts)
#利用str.contains()筛选数据
#keywords_counts.str.contains('|'.join(FILTER_WORDS))#str.contains()里填一个字符或者正则表达式，这里指用'|'把词组连接起来
print('|'.join(FILTER_WORDS))




#未解决pyecharts wordcloud模块问题
#导入pyecharts并绘制词云图
#列表前加~表示取反
#方案二，建立关键词过滤列表
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
import pyecharts as pec
FILTER_WORDS=['知道','影评','电影','影片','这么','那么','怎么','如果','\n','一部','这部','没有','还有']#根据实际情况来调整过滤词列表，具体问题具体分析。
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
	#筛选出前十个评论里最多的关键词
def  get_comment_keywords_counts(movie_id,count):
	 comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
	 comment_str_all = ''
	 for comment in comment_list:
		 comment_str_all += comment + '\n'
	 seg_list = list(jieba.cut(comment_str_all))
	 #转换成Pandas的Series类型数据
	 keywords_counts = pd.Series(seg_list)
	 #利用str.len()筛选字符串长度
	 keywords_counts = pd.Series(seg_list)
	 keywords_counts = keywords_counts[keywords_counts.str.len()>1]

	 return keywords_counts
#写为函数方便调用	 
def get_movie_name_and_score(movie_id):
       #根据电影ID在douban_movie_data找出电影名和评分
    #douban_movie_data中体现ID的是链接
    movie_link = 'https://movie.douban.com/subject/{}/'.format(movie_id)
    
    search_result = movie_data[movie_data['链接']==movie_link].iloc[0]#只把第一行的内容给筛选出来，通过".iloc[0]"
    movie_name = search_result['电影名']
    movie_score = search_result['评分']
    return(movie_name,movie_score)

#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
movie_data = pd.read_excel('douban_movie_data.xlsx')


movie_id = '1292052'
keywords_counts = get_comment_keywords_counts(movie_id,30)#取前30个关键词
wordcloud = pec.WordCloud(width=1280,height=720)
wordcloud.add("",keywords_counts.index,keywords_counts.values,
	word_size_range=[20,100],
	shape='diamond')
wordcloud.render()
movie_name,movie_score = get_movie_name_and_score(movie_id)


#print(comment_data)#先把数据导出来看看，[404972 rows x 7 columns]有404972行，7列的数据
#调用函数
#print(get_movie_id_list(1000))#Index(['1292222', '1292052'], dtype='object'),即评论数超过一千的其实只有两个电影，'1292222',和 '1292052'
#如和通过ID查看豆瓣电影页面？观察豆瓣网址规律，得出https://mobie.douban.com/subject/1292222,即，替换后面的数字即可.
#简单测试jieba模块
#import jieba
#print(list(jieba.cut('关于希望最强有力的注释。')))
#根据ID筛选评论
movie_id='1292052'
comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
#print(comment_list)#输出评论先看看
#整合全部评论为一个字符串，以换行隔开
comment_str_all = ''
for comment in comment_list:
	comment_str_all += comment + '\n'#加上换行符号
#获取分词后的列表
seg_list = list(jieba.cut(comment_str_all))
#转换成Pandas的Series类型数据
keywords_counts = pd.Series(seg_list)
#利用str.len()筛选字符串长度
keywords_counts = pd.Series(seg_list)
keywords_counts = keywords_counts[keywords_counts.str.len()>1]#筛选内容分析：1，分词长度大于一（只有一个字意义并不大），2，关键词应有实际意义
keywords_counts = keywords_counts[~keywords_counts.str.contains('|'.join(FILTER_WORDS))]#反向选择不包含过滤词列表中词语的数据，前面加"~"表示取反，如列表中的Ture改为False
#统计各个关键词的出现次数
keywords_counts = keywords_counts.value_counts()[:30]#汇总
print(keywords_counts)
#利用str.contains()筛选数据
#keywords_counts.str.contains('|'.join(FILTER_WORDS))#str.contains()里填一个字符或者正则表达式，这里指用'|'把词组连接起来
print('|'.join(FILTER_WORDS))







#词云老版本函数构造，理解思路
def generate_word_cloud(world_list,path_name):
	wordcloud = pec.WordCloud(width=1300,height=620)
	wordcloud.add("",word_list.index,word_list.values
	    word_size_range=[20,100],
	    shape='diamond')
	wordcloud.render(path=path_name)
	print('Generate word cloud file done:{}'.format)


#调用函数的方法
path_name = 'wordcloud/{}_{}.html'.format(movie_name)
generate_word_cloud(word_list,path_name)


#导入pyecharts并绘制词云图，结合调用函数的思路参考，函数调用方法为旧版本的方法，仅作参考
#列表前加~表示取反
#方案二，建立关键词过滤列表
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
import pyecharts as pec
FILTER_WORDS=['知道','影评','电影','影片','这么','那么','怎么','如果','\n','一部','这部','没有','还有']#根据实际情况来调整过滤词列表，具体问题具体分析。
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
	#筛选出前十个评论里最多的关键词
def  get_comment_keywords_counts(movie_id,count):
	 comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
	 comment_str_all = ''
	 for comment in comment_list:
		 comment_str_all += comment + '\n'
	 seg_list = list(jieba.cut(comment_str_all))
	 #转换成Pandas的Series类型数据
	 keywords_counts = pd.Series(seg_list)
	 #利用str.len()筛选字符串长度
	 keywords_counts = pd.Series(seg_list)
	 keywords_counts = keywords_counts[keywords_counts.str.len()>1]

	 return keywords_counts
#写为函数方便调用	 
def get_movie_name_and_score(movie_id):
	   #根据电影ID在douban_movie_data找出电影名和评分
	#douban_movie_data中体现ID的是链接
	movie_link = 'https://movie.douban.com/subject/{}/'.format(movie_id)
	
	search_result = movie_data[movie_data['链接']==movie_link].iloc[0]#只把第一行的内容给筛选出来，通过".iloc[0]"
	movie_name = search_result['电影名']
	movie_score = search_result['评分']
	return(movie_name,movie_score)
#词云老版本函数构造，理解思路
def generate_word_cloud(world_list,path_name):
	wordcloud = pec.WordCloud(width=1300,height=620)
	wordcloud.add("",word_list.index,word_list.values
		word_size_range=[20,100],
		shape='diamond')
	wordcloud.render(path=path_name)
	print('Generate word cloud file done:{}'.format)
#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
movie_data = pd.read_excel('douban_movie_data.xlsx')
movie_id = '1292052'
keywords_counts = get_comment_keywords_counts(movie_id,30)#取前30个关键词
wordcloud = pec.WordCloud(width=1280,height=720)
wordcloud.add("",keywords_counts.index,keywords_counts.values,
	word_size_range=[20,100],
	shape='diamond')
wordcloud.render()
movie_name,movie_score = get_movie_name_and_score(movie_id)

#调用函数的方法
path_name = 'wordcloud/{}_{}.html'.format(movie_name,movie_score)
generate_word_cloud(word_list,path_name)
generate_word_cloud(keywords_counts,path_name)







#向下取整函数
 import math
 print(math.floor(3.5))#向下取整为3
 print(math.floor(5.8))#向下取整为5
 #列表的连接
 l1 = [1,2,3]
 l2 = [4,5,6]
 l1.extend(l2)
 print(l1)
 #输出结果为
 [1,2,3,4,5,6]






#关键词及评分的关系分析
#以电影评论关键词作为切入
#展示与评分的联系
#不同评分下的关键词还具有不同的热度
#所以，一共有几个维度的数据三个维度，可用3D柱状图和热力图展示1，不同的关键词，2不同的打分，3，不同的关键词在不同的打分下还有不同的热度。
#创建两个列表，存储关键词和出现次数把每部电影的30个关键词按评分区间放进去
#每个列表都含十个列表
kw_list_by_score = [[]for _ in range(10)]
kw_counts_list_by_score = [[] for _ in range(10)]
#每个列表都含有十个列表
movie_id_list=get_movie_id_list(300)
for movie_id in movie_id_list:
      word_list = get_comment_kw_counts(movie_id,30)
      movie_name,movie_score=get_movie_name_and_score(movie_id)
      try:
      	  
      	  kw_counts_list_by_score[math.floor(movie_score)].extend(word_list.index)#通过extend，把列表movie_score加进word_list
      	  kw_list_by_score[math.floor(movie_score)].extend(word_list.values)
      except:
      	  print(movie_id)

#每次创建一个DataFrame数据
#保存该得分区间的TOP3-关键词和出现总次数
for i in range(10)
    if kw_list_by_score[i]:
    	kw30_with_counts = pd.DataFrame({
             'kw': kw_list_by_score[i],
             'counts': kw_counts_list_by_score[i]
    		})
#统计关键词的出现总次数，并算出百分比，并储存为文件
kw30_with_counts = kw30_with_counts.groupby('kw').sum()
kw30_with_counts = kw30_with_counts.sort_values(by='counts',ascending=False)[:30]#第一步，通过sort_values按照计算次数（counts）来排序，再通过ascending=False进行降序排列
counts_sum = kw30_with_counts['counts'].sum()#将每部电影前30位关键词取出来后，把它们打分的次数进行求和（相当于按比例显示）
kw30_with_counts['percentage'] = kw30_with_counts['counts']/counts_sum
kw30_with_counts.to_csv('movie_keywords_by_score/{}_movie_keywords.csv'.format(i))#将其存入一个CSV文件











#整理数据
#导入pyecharts并绘制词云图
#列表前加~表示取反
#方案二，建立关键词过滤列表
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
import pyecharts as pec
import math
FILTER_WORDS=['知道','影评','电影','影片','这么','那么','怎么','如果','\n','一部','这部','没有','还有']#根据实际情况来调整过滤词列表，具体问题具体分析。
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
	#筛选出前十个评论里最多的关键词
def  get_comment_keywords_counts(movie_id,count):
	 comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
	 comment_str_all = ''
	 for comment in comment_list:
		 comment_str_all += comment + '\n'
	 seg_list = list(jieba.cut(comment_str_all))
	 #转换成Pandas的Series类型数据
	 keywords_counts = pd.Series(seg_list)
	 #利用str.len()筛选字符串长度
	 keywords_counts = pd.Series(seg_list)
	 keywords_counts = keywords_counts[keywords_counts.str.len()>1]

	 return keywords_counts
#写为函数方便调用	 
def get_movie_name_and_score(movie_id):
	   #根据电影ID在douban_movie_data找出电影名和评分
	#douban_movie_data中体现ID的是链接
	movie_link = 'https://movie.douban.com/subject/{}/'.format(movie_id)
	
	search_result = movie_data[movie_data['链接']==movie_link].iloc[0]#只把第一行的内容给筛选出来，通过".iloc[0]"
	movie_name = search_result['电影名']
	movie_score = search_result['评分']
	return(movie_name,movie_score)


#词云老版本函数构造，理解思路
def generate_word_cloud(world_list,path_name):
	wordcloud = pec.WordCloud(width=1300,height=620)
	wordcloud.add("",word_list.index,word_list.values
		word_size_range=[20,100],
		shape='diamond')
	wordcloud.render(path=path_name)
	print('Generate word cloud file done:{}'.format)

#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
movie_data = pd.read_excel('douban_movie_data.xlsx')


movie_id = '1292052'
keywords_counts = get_comment_keywords_counts(movie_id,30)#取前30个关键词
wordcloud = pec.WordCloud(width=1280,height=720)
wordcloud.add("",keywords_counts.index,keywords_counts.values,
	word_size_range=[20,100],
	shape='diamond')
wordcloud.render()
movie_name,movie_score = get_movie_name_and_score(movie_id)

#调用函数的方法
path_name = 'wordcloud/{}_{}.html'.format(movie_name,movie_score)
generate_word_cloud(word_list,path_name)
generate_word_cloud(keywords_counts,path_name)


#关键词及评分的关系分析
#以电影评论关键词作为切入
#展示与评分的联系
#不同评分下的关键词还具有不同的热度
#所以，一共有几个维度的数据三个维度，可用3D柱状图和热力图展示1，不同的关键词，2不同的打分，3，不同的关键词在不同的打分下还有不同的热度。
#创建两个列表，存储关键词和出现次数把每部电影的30个关键词按评分区间放进去
#每个列表都含十个列表
kw_list_by_score = [[]for _ in range(10)]
kw_counts_list_by_score = [[] for _ in range(10)]
#每个列表都含有十个列表
movie_id_list=get_movie_id_list(300)
for movie_id in movie_id_list:
      word_list = get_comment_kw_counts(movie_id,30)
      movie_name,movie_score=get_movie_name_and_score(movie_id)
      try:
      	  
      	  kw_counts_list_by_score[math.floor(movie_score)].extend(word_list.index)#通过extend，把列表movie_score加进word_list
      	  kw_list_by_score[math.floor(movie_score)].extend(word_list.values)
      except:
      	  print(movie_id)

#每次创建一个DataFrame数据
#保存该得分区间的TOP3-关键词和出现总次数
for i in range(10)
    if kw_list_by_score[i]:
    	kw30_with_counts = pd.DataFrame({
             'kw': kw_list_by_score[i],
             'counts': kw_counts_list_by_score[i]
    		})


#统计关键词的出现总次数，并算出百分比，并储存为文件
kw30_with_counts = kw30_with_counts.groupby('kw').sum()
kw30_with_counts = kw30_with_counts.sort_values(by='counts',ascending=False)[:30]#第一步，通过sort_values按照计算次数（counts）来排序，再通过ascending=False进行降序排列
counts_sum = kw30_with_counts['counts'].sum()#将每部电影前30位关键词取出来后，把它们打分的次数进行求和（相当于按比例显示）
kw30_with_counts['percentage'] = kw30_with_counts['counts']/counts_sum
kw30_with_counts.to_csv('movie_keywords_by_score/{}_movie_keywords.csv'.format(i))#将其存入一个CSV文件





kw_counts_list_by_score = [[] for i in range(10)]
for i in range(4,10):
	kw_counts_list_by_score[i] = pd.read_csv('movie_keywords_by_score/{}_movie_keywords.csv'.formt(i))
	#索引为关键词，列为得分
	kw_percentage_df = pd.DataFrame([],
        cokumns=list(range(4,10)),
        index=kw_counts_list_by_score[9]['kw'][:10]
		)
#筛选数据并填充进DataFrame中
#没有找到关键词填0
for i in range(4,10)
    kw = kw_counts_list_by_score[i]
    kw = kw[kw['kw'].isin(kw_percentage_df.index)]
    kw_percentage_df[i] = Series(list(kw['percentage']),index=kw['kw'])#index表示索引
kw_percentage_df.fillna(0,inplace=True)#implace表示更改原始表格
#一个列表，里面的数据项也是一个列表，数据项由三个数字构成，xyz坐标

data = []
i = 0
for index in kw_percentage_df.index;
     j=0
     for column in kw_percentage_df.columns:
     	  data.append([j,i,kw_percentage_df[column][index]*100])#乘以100，防止数值太小不好观看
     	  j+=1
     i+=1
#绘制热力图
#标记点和标记线
heatmap = pec.HratMap()
heatmap.add("电影评论关键词的热力图",
    kw_percentage_df.columns,
    kw_percentage_df.index,
    data,
    is_visualmap=True,
    visual_text_color="#000",
    visual_range=[0,10],
    visual_orient='horizontal'
    )




#机器学习分类

from sklearn import svm#LinearSVC是SVM的一种
from sklearn.model_selection import train_test_split
#本次的鸢尾花数据为模块自带。
from sklearn import datasets#导入模块，注意：scikit-learn在python中是sklearn
#数据切分
#直接loar_iris()即可获取自带数据
iris = datasets.load_iris()
#print(iris)#输出结果看看
X = iris.data
y = iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)#sklearn.model selection模块的train test split,train test split可将数据分为两个部分，一部分为train，即训练用数据，一部分为test即测试用数据，test size可以调节训练和测试数据比例，random state可以确保切分状态一致
#创建列表的快速方法
easy_list = [i*i for i in range(10)]
print(easy_list)
#只需要循环不需要循环变量时用下划线代替，表示不需要，只是占个位置
for _ in range(10):
	print('Hello makerbean')#这里的目的只是输出十个Hello makerbean


#创建一个LinearSVC分类器
clf = svm.LinearSVC()
clf.fit(X_train,y_train)
#通用流程
#1.创建分类器/回归器等
#2.xxx.fitx(训练数据输入值，对应正确结果)
#3.xxx.predict(待检测数据输入值)



#模型得分
#通过.score()计算模型得分
print('得分:{}'.format(clf.score(X_test,y_test)))#得分=正确数量/数据总数
#通过.predict()预测新数据
y_predict = clf.predict(X_test)
print(y_predict)
print(y_test)





#load_boston()#获取数据
#boston.DESCR获取数据说明
boston = datasets.load_boston()
print(boston.DESCR)







from sklearn import svm#LinearSVC是SVM的一种
from sklearn.model_selection import train_test_split
#本次的鸢尾花数据为模块自带。
from sklearn import datasets#导入模块，注意：scikit-learn在python中是sklearn
import pyecharts as pec
from pyecharts.charts import Scatter



#load_boston()#获取数据
#boston.DESCR获取数据说明
boston = datasets.load_boston()
print(boston.DESCR)

#绘制散点图直观感受数据分布
scatter_list = []
for i in range(13):
	scatter = pec.Scatter(boston.feature_names[i],
		title_pos='center')
	scatter.add('',boston.data[:,i],boston.target)
	scatter_list.append(Scatter)
page = pec.Page()
for i in range(13):
	page.add(scatter_list[i])
page.render(path='scatter by feature.html')





from sklearn import svm#LinearSVC是SVM的一种
from sklearn.model_selection import train_test_split
#本次的鸢尾花数据为模块自带。
from sklearn import datasets#导入模块，注意：scikit-learn在python中是sklearn
import pyecharts as pec
from pyecharts.charts import Scatter


#波士顿房价预测完整版
#load_boston()#获取数据
#boston.DESCR获取数据说明
boston = datasets.load_boston()
print(boston.DESCR)

#绘制散点图直观感受数据分布
scatter_list = []
for i in range(13):
	scatter = pec.Scatter(boston.feature_names[i],
		title_pos='center')
	scatter.add('',boston.data[:,i],boston.target)
	scatter_list.append(Scatter)
page = pec.Page()
for i in range(13):
	page.add(scatter_list[i])
page.render(path='scatter by feature.html')

#切分为训练数据集和测试数据集
X = boston.data
y = boston.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=)
#判断属于回归类算法
#导入模块先
from sklearn import linear_model
#创建回归器并训练
lasso = linear_model.Lasso()
lasso.fit(X_train,y_train)
#引入均方差
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,lasso.predict(X_test))
score = lasso.score(X_test,y_test)
print('MSE:{}'.format(mse))
print('Score:{}'.format(score))
#调节参数
lasso = linear_model.Lasso(alpha=0.1)#具体参数参考官方文档


#利用scikit-learn的网格搜索调节参数
from sklearn.model_selection import GridSearchCV
alpha_range = np.alpha_range(0,1,0.05)#要调整的alpha值的参数
param_grid = {'alpha':alpha_range}#将参数名称写入''冒号后为参数值的列表
lasso_search = GridSearchCV(lasso,param_grid)#用GridSearchCV函数写入要调整的模型lasso及该模型的参数param_grid
lasso_search.fit(X_train,y_train)#直接使用模型训练
for result in lasso_search.cv_results_:#输出最好的数值
	print(result,lasso_search.cv_results_[result])
print(lasso_search.best_score_)
print(lasso_search.best_params_)
print(lasso_search.best_estimator_)
#各个回归模型都可以测试一下
lasso = linear_model.Lasso()
eln_reg = linear_model.ElasticNext()
svr_reg = svm.SVR()
nusvr_reg = svm.NuSVR()
ridge_reg = linear_model.Ridge()
gbr_reg = ensemble.GradientBoostingRegressor()
#查看各个特征的重要程度
feature_importance_df = pd.DataFrame({
	'name':boston.feature_names,
    'importance':gbr_reg.feature_importance_
	})
feature_importance_df.sort_values(by='importance',ascending=False,inplace=True)
bar = pec.Bar('各特征重要性',width=1280,height=720)
bar.add('',feature_importance_df.name,feature_importance_df.importance)
bar.render(path='各特征重要性.html')



#利用随机搜索来降低搜索复杂度
#注意添加n_iter=测试次数，确定需要测试的次数
n_estimators_range = np.arange(100,1000,100)
max_depth_range = np.arange(3,10)
learning_rate_range = [0.0001,0.001,0.01,0.1]#调整三个参数
param_grid = {
        'n_estimators':n_estimators_range,
        'max_depth':max_depth_range,
        'learning_rate'	:learning_rate_range
}
gbr_search = RandomizedSearchCV(gbr_reg,param_grid,n_iter=30)#n_iter表示随机多少次
gbr_search.fit(X_train,y_train)
for result in gbr_search.cv_results_:
	print(result)
print(gbr_search.best_score_)
print(lasso_search.best_params_)
print(lasso_search.best_estimator_)











#文本数据处理问题
#自然语言处理(NLP)即将机器学习与文本数据处理相结合
#文本的分类
from sklearn import datasets
#直接fetch_20newsgroups()即可获得新闻数据
data_train = datasets.fetch_20newsgroups(subset='train',remove=('headers','footers','quotes'),
)#subset='train'参数，意为获取一部分,再利用remove参数移走不需要的部分，这里去除了帖子的头尾，只保留正文内容
print(data_train.data[0])
print(type(data_train.data[0]))#看下数据是什么类型
print(data_train.target_names)#查看都有哪些分类名称
print(data_train.target_names[data_train.target[0]])#查看一篇文章对应的分类




#scikit-learn的计数向量转化
from sklearn.feature_extraction.text import CountVectorizer#引入包，用来处理提取文本特征
count_vect = CountVectorizer(stop_words='english')#与scikit-learn的计数向量转化配套，转化为词频矩阵过滤停用词此处为过滤英文停用词
#若要过滤中文停用词，将停用词整理为一个列表数据后也可传入
#chinese_stop_words=['第一','第二','一直']
#stop_words=chinese_stop_words
X_train_counts = count_vect.fit_transform(data_train.data)#数据统计转换
print(X_train_counts.shape)




#文本的分类
#需要过滤掉的字词即被称为Stop Words(停用词)
#scikit-learn的计数向量转化
from sklearn.feature_extraction.text import CountVectorizer#引入包，用来处理提取文本特征
from sklearn import datasets
count_vext = CountVectorizer(stop_words='english')#与scikit-learn的计数向量转化配套，转化为词频矩阵过滤停用词
#直接fetch_20newsgroups()即可获得新闻数据
data_train = datasets.fetch_20newsgroups(subset='train',remove=('headers','footers','quotes'),
)#subset='train'参数，意为获取一部分,再利用remove参数移走不需要的部分，这里去除了帖子的头尾，只保留正文内容
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(data_train.data)#数据统计转换,统计行数文章数
print(data_train.data[0])
print(type(data_train.data[0]))#看下数据是什么类型
print(data_train.target_names)#查看都有哪些分类名称
print(data_train.target_names[data_train.target[0]])#查看一篇文章对应的分类
print(X_train_counts.shape)
#对应文本分类的基本原理：根据文章常出现的词语来确定分类

#TF-IDF方法
#TF(Term Frequency):词汇频率
#IDF(Inverse Document Frequency):逆向文件频率
#核心思想：如果某个词或短语再一篇文章中出现的频率TF高，并且在其他文章中很少出现，则认为此词或短语具有很好的类别区分能力，适合用来分类
#如car一词在一篇文章中出现的次数为4次，而该文章总词数为91，则car的词频（TF）为4/91=0.044
#如car在100篇文章中出现，文章总数为10000篇，则逆向词频IDF=In(10000/100)=4.605
#则car的TF-IDF得分：TF-IDF = 0.044*4.605 =0.20262，该值越高，筛选的作用就越大



#scikit-learn中的TF-IDF方法
#TfidfTransformer
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf_transformer.transform(X_train_counts)



#使用朴素贝叶斯方法
#朴素贝叶斯非常适合于文档分类和垃圾邮件过滤任务
from sklearn.naive_bayes import MultinomialNB#MultinomialNB--多项分布朴素贝叶斯
clf = MultinomialNB().fit(X_train_tfidf,data_train.target)


#写一段待预测的文字列表并计算TF-IDF,需要以TF-IDF作为预测的输入
text_test = ['Do you use Mac','God loves you','OpenGL on the GPU is fast']
X_test_counts = count_vect.transform(text_test)#统计词频
X_test_tfidf = tfidf_transformer.transform(X_test_counts)#计算TF-IDF值
predicted = clf.predict(X_test_tfidf)
print(predicted)








#多项分布朴素贝叶斯
#文本数据处理问题
#自然语言处理(NLP)即将机器学习与文本数据处理相结合
#文本的分类
#需要过滤掉的字词即被称为Stop Words(停用词)
#scikit-learn的计数向量转化
from sklearn.feature_extraction.text import CountVectorizer#引入包，用来处理提取文本特征
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfTransformer#scikit-learn中的TF-IDF方法
from sklearn.naive_bayes import MultinomialNB#MultinomialNB--多项分布朴素贝叶斯

count_vext = CountVectorizer(stop_words='english')#与scikit-learn的计数向量转化配套，转化为词频矩阵过滤停用词
#直接fetch_20newsgroups()即可获得新闻数据
data_train = datasets.fetch_20newsgroups(subset='train',remove=('headers','footers','quotes'),
)#subset='train'参数，意为获取一部分,再利用remove参数移走不需要的部分，这里去除了帖子的头尾，只保留正文内容
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(data_train.data)#数据统计转换
tfidf_transformer = TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf_transformer.transform(X_train_counts)
text_test = ['Do you use Mac','God loves you','OpenGL on the GPU is fast']
X_test_counts = count_vect.transform(text_test)#统计词频
X_test_tfidf = tfidf_transformer.transform(X_test_counts)#计算TF-IDF值
clf = MultinomialNB().fit(X_train_tfidf,data_train.target)
predicted = clf.predict(X_test_tfidf)
print(data_train.data[0])
print(type(data_train.data[0]))#看下数据是什么类型
print(data_train.target_names)#查看都有哪些分类名称
print(data_train.target_names[data_train.target[0]])#查看一篇文章对应的分类
#对应文本分类的基本原理：根据文章常出现的词语来确定分类
print(X_train_counts.shape)
print(X_train_tfidf.shape)
print(predicted)




#将结果与target结合起来
for doc,category in zip(text_test,predicted):
    print('{}--------> {}'.format(doc,data_train.target_names[category]))




#多项分布朴素贝叶斯#将结果与target结合起来
#文本数据处理问题
#自然语言处理(NLP)即将机器学习与文本数据处理相结合
#文本的分类
#需要过滤掉的字词即被称为Stop Words(停用词)
#scikit-learn的计数向量转化
from sklearn.feature_extraction.text import CountVectorizer#引入包，用来处理提取文本特征
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfTransformer#scikit-learn中的TF-IDF方法
from sklearn.naive_bayes import MultinomialNB#MultinomialNB--多项分布朴素贝叶斯

count_vext = CountVectorizer(stop_words='english')#与scikit-learn的计数向量转化配套，转化为词频矩阵过滤停用词
#直接fetch_20newsgroups()即可获得新闻数据
data_train = datasets.fetch_20newsgroups(subset='train',remove=('headers','footers','quotes'),
)#subset='train'参数，意为获取一部分,再利用remove参数移走不需要的部分，这里去除了帖子的头尾，只保留正文内容
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(data_train.data)#数据统计转换
tfidf_transformer = TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf_transformer.transform(X_train_counts)
text_test = ['Do you use Mac','God loves you','OpenGL on the GPU is fast']
X_test_counts = count_vect.transform(text_test)#统计词频
X_test_tfidf = tfidf_transformer.transform(X_test_counts)#计算TF-IDF值
clf = MultinomialNB().fit(X_train_tfidf,data_train.target)
predicted = clf.predict(X_test_tfidf)
#将结果与target结合起来
for doc,category in zip(text_test,predicted):
	print('{}--------> {}'.format(doc,data_train.target_names[category]))
print(data_train.data[0])
print(type(data_train.data[0]))#看下数据是什么类型
print(data_train.target_names)#查看都有哪些分类名称
print(data_train.target_names[data_train.target[0]])#查看一篇文章对应的分类
#对应文本分类的基本原理：根据文章常出现的词语来确定分类
print(X_train_counts.shape)
print(X_train_tfidf.shape)
print(predicted)



#zip()函数
#将两个或多个列表按顺序打包成一个个元祖
student = ['lilei','hanmeimei','madongmei']
score = [98,99,100]
print(list(zip(student,score)))








#导入tushare模块
import tushare as ts
stock_df = ts.get_hs300s()#沪深
print(stock_df)

#利用MeanShift分类
from sklearn.cluster import MeanShift,estimate_bandwidt
bandwidth = estimate_bandwidth(X)
ms = MeanShift(bandwidth=bandwidth,bin_seeding=True)
ms.fit(X)

#labels_属性
labels = ms.labels_
for company,label in zip(stock_basics['name'],labels):
	print(f'{company}-->{label}')






#导入tushare模块
#去掉名字，领域，地域
#分类
import tushare as ts
from sklearn.cluster import MeanShift,estimate_bandwidth
from sklearn.cluster import KMeans
#去掉名字，领域，地域
stock_df = ts.get_hs300s()#沪深（简短信息）
stock_basics = ts.get_stock_basics()#找出详细信息
stock_basics = stock_basics.loc[stock_df['code'].values]
X = stock_basics.drop(['name','industry','area'],1)
bandwidth = estimate_bandwidth(X)
ms = MeanShift(bandwidth=bandwidth,bin_seeding=True)#MeanShift聚类
ms.fit(X)
#print(stock_df)
#print(stock_basics)
#再利用pandas筛选数据
#print(stock_basics)
labels = ms.labels_
for company,label in zip(stock_basics['name'],labels):
	print(f'{company}-->{label}')


#KMeans分类
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4,random_state=0).fit(X)#分成四类
labels=kmeans.labels_
for company,label in zip(stock_basics['name'],labels):
	print(f'{company}--->{label}')






#导入tushare模块
#KMeans分类
#去掉名字，领域，地域
#分类
import tushare as ts
from sklearn.cluster import MeanShift,estimate_bandwidth
from sklearn.cluster import KMeans
#去掉名字，领域，地域
stock_df = ts.get_hs300s()#沪深（简短信息）
stock_basics = ts.get_stock_basics()#找出详细信息
stock_basics = stock_basics.loc[stock_df['code'].values]
X = stock_basics.drop(['name','industry','area'],1)
bandwidth = estimate_bandwidth(X)
ms = MeanShift(bandwidth=bandwidth,bin_seeding=True)#MeanShift聚类
ms.fit(X)
#print(stock_df)
#print(stock_basics)
#再利用pandas筛选数据
#print(stock_basics)
labels = ms.labels_
#for company,label in zip(stock_basics['name'],labels):
#	print(f'{company}-->{label}')
kmeans = KMeans(n_clusters=4,random_state=0).fit(X)
labels=kmeans.labels_
for company,label in zip(stock_basics['name'],labels):
 	print(f'{company}--->{label}')
 




#算法研习社
#第一步，去掉各种标点符号，使之成为列表
words = []
with open('同一目录下的文件名','r') as f:
	lines = f.readlines()
	for line in lines:
		line = line.replace(',','')
		line = line.replace('.','')
		line = line.replace('"','')
		line = line.replace('!','')
		line = line.replace('?','')
		line = line.replace(':','')
		line = line.replace('\'','')#注意如果要分离'用的斜杠
		line = line.replace('-','')
		line = line.replace('\n','')
		for word in line.split(''):
			if word:
				words.append(word)
print(words)
print(len(words))#用len函数就知道整个文章有多少单词
words_set = set(words)#去掉重复单词
print(len(words_set))#再看下这个时候还有多少单词
print(find_word_count(words,words_set))#做个词频统计，这里假设已经有find_word_count()函数



#算法研习社
#第一步，去掉各种标点符号，使之成为列表
def find_word_count(words,words_set):
	words_count = {}#用字典，单词不会重复且要储存答案（即词汇出现的次数）
	for word in words:
		if word in words_count:#如果单词已经存在里面，把对应数字加一即可
		    words_count[word] += 1#如果单词已经存在里面，把对应数字加一即可
		else:words_count[word] = 1#本身已经是第一个单词，故直接=1
return words_count
words = []
with open('同一目录下的文件名','r') as f:
	lines = f.readlines()
	for line in lines:
		line = line.replace(',','')
		line = line.replace('.','')
		line = line.replace('"','')
		line = line.replace('!','')
		line = line.replace('?','')
		line = line.replace(':','')
		line = line.replace('\'','')#注意如果要分离'用的斜杠
		line = line.replace('-','')
		line = line.replace('\n','')
		for word in line.split(''):
			if word:
				words.append(word)
print(len(words))#用len函数就知道整个文章有多少单词
words_set = set(words)#去掉重复单词
print(len(words_set))#再看下这个时候还有多少单词
print(find_word_count(words,words_set))#做个词频统计，这里假设已经有find_word_count()函数











#算法研习社
#加了一个for循环
#第一步，去掉各种标点符号，使之成为列表
def find_word_count(words,words_set):
	words_count = {}#用字典，单词不会重复且要储存答案（即词汇出现的次数）
	for word in words_set:
		words_count[word] = 0
	for word in words:
		words_count[word] += 1
		#if word in words_count:#如果单词已经存在里面，把对应数字加一即可
		##    words_count[word] += 1#如果单词已经存在里面，把对应数字加一即可
		#else:words_count[word] = 1#本身已经是第一个单词，故直接=1
words = []
with open('同一目录下的文件名','r') as f:
	lines = f.readlines()
	for line in lines:
		line = line.replace(',','')
		line = line.replace('.','')
		line = line.replace('"','')
		line = line.replace('!','')
		line = line.replace('?','')
		line = line.replace(':','')
		line = line.replace('\'','')#注意如果要分离'用的斜杠
		line = line.replace('-','')
		line = line.replace('\n','')
		for word in line.split(''):
			if word:
				words.append(word)
print(len(words))#用len函数就知道整个文章有多少单词
words_set = set(words)#去掉重复单词
print(len(words_set))#再看下这个时候还有多少单词
print(find_word_count(words,words_set))#做个词频统计，这里假设已经有find_word_count()函数




#链表
#python自带链表
L = [3,5,6]
L.append(7)




#实现一个结构，可以自己查询元素，添加元素，插入元素，删除元素
#定义一个最简单的链表
class IntList(object):
	def __init__(self):
		self.first = None
		self.rest = None
l1 = IntList()
l2 = IntList()
l3 = IntList()
l1.first = 5
l2.first = 10
l3.first = 15
l1.rest = l2
l2.rest = l3

print(l1.rest.rest.first)#得到l3的数据5，因为l1.rest=l2，l2.rest=l3









#改进
#实现一个结构，可以自己查询元素，添加元素，插入元素，删除元素
#定义一个最简单的链表
class IntList(object):
	def __init__(self,f,r):
		self.first = f
		self.rest = r

l = IntList(5,None)
l = IntList(10,l)
l = IntList(15,l)
print(l.rest.rest.first)








