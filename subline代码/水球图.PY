#调整水球图
from pyecharts import options as opts
from pyecharts.charts import Liquid
liquid = Liquid()
liquid.add("Liquid",[0.7,0.6,0.5],is_outline_show=False)#各比例is_outline_show是否显示外边框，is_animation_show是否显示动画效果，shape=("输入路径")边框形状和symbol可用的形状类似，还可以自定义.去Iconfont.cn找,选择SVG下载，用Sublime打开复制Path及其之后的数字
liquid.set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))#大标题的名字
liquid.render()
