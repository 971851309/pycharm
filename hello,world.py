# 以解析百度为例
# 爬取该页面所有标题
# https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xe216863e00003e86&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=02049043_6_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=7&rsv_sug7=101&rsv_sug2=0&inputT=3277&rsv_sug4=13494
from requests import get
from lxml import etree


def get_html(url: str):
    html = get(url)
    if html.status_code == 200:
        print('ok')
        soup = etree.HTML(html.text)
        # soup=etree.HTML(html.text)
        titles = soup.xpath('//div[@id="content_left"]/div[starts-with(@class,"result")')
        for t in titles:
            title = (t.xpath('h3/a/text()'))
            print(''.join(titles))  # 用join把标题连接在一起
            try:
                url = t.xpath('h3/a/@href')[0]
                print(url)
            except:
                print('no href')
        else:
            print('error')


def main():
    url = 'http://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xa2060c2800014031&issp=1&f=8' \
          '&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=7' \
          '&rsv_sug1=7&rsv_sug7=101&rsv_sug2=0&inputT=1836&rsv_sug4=2778'  # 用换行符，便于观看
    get_html(url)


if __name__ == '__main__':
    main()

# //div[@id="content_left"]/div[starts-with(@class,"result")]




