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


