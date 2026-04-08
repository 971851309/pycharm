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
    symbol=SymbolType.DIAMOND)#ARROW指箭头标识，除此之外，还有'cicle','rect','roundRect','triangle','diamond','pin','arrow','none'标识
effect_scatter.set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
	
effect_scatter.render()