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
	"G",#此为图表总名称
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


