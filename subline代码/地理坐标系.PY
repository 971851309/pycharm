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