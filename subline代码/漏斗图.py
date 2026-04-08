#漏斗图
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Funnel#漏斗图的导入
funnel = Funnel()
funnel.add("商品",[list(z) for z in zip(Faker.choose(),Faker.values())])#直接添加列表里的一个数据
funnel.set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))#图表的总标题
funnel.render()