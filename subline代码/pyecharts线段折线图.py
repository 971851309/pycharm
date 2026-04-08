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
