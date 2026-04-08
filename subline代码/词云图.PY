
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
