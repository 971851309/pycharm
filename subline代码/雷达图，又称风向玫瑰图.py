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
