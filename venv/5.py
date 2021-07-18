from pyecharts import options as opts
from pyecharts.charts import Grid, Line, Scatter, Bar,Page
from pyecharts.charts import Boxplot
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
import random

min_ = 600
max_ = 1000
v1 = [
    [random.randint(min_, max_) for i in range(50)],
    [random.randint(min_, max_) for i in range(50)],
    [random.randint(min_, max_) for i in range(50)],
    [random.randint(min_, max_) for i in range(50)],
]

line = (
    Line()
        .add_xaxis(['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天'])
        .add_yaxis('最低气温', [11, 11, 15, 13, 12, 13, 10])
        .add_yaxis('最高气温', [1, -2, 2, 5, 3, 2, 0])
        .set_global_opts(
        yaxis_opts=opts.AxisOpts(type_='value', axislabel_opts=opts.LabelOpts(formatter='{value} ℃')),
        title_opts=opts.TitleOpts(title='折线示例图',pos_top="50%",pos_left='45%' ),
        legend_opts=opts.LegendOpts(pos_top="50%",pos_right='25%')
    )
)

scatter = (
    Scatter()
        .add_xaxis(['可乐', '雪碧', '橙汁', '绿茶', '奶茶', '百威', '青岛'])  # x轴
        .add_yaxis('es', [100, 78, 27, 48, 34, 93, 76])  # y轴

        # 全局配置项
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Scatter",pos_top="50%",pos_left='5%'),
        # 设置图例位置
        legend_opts=opts.LegendOpts(pos_top="50%",pos_left='27%'),
    )
)

bar = (
    Bar()
        .add_xaxis(['苹果', '芒果', '猕猴桃', '香蕉', '车厘子'])
        .add_yaxis('bar', [200, 160, 120, 289, 105])
        .set_global_opts(
        title_opts=opts.TitleOpts(title='柱状图-水果销量',pos_left='49%' ),
        legend_opts=opts.LegendOpts(pos_right='30%'),
)
)
c = Boxplot()
c.add_xaxis(['项目A', '项目B', '项目C', '项目D'])
c.add_yaxis('boxplot', c.prepare_data(v1))


c.set_global_opts(title_opts=opts.TitleOpts(title="箱型图示例"),legend_opts=opts.LegendOpts(pos_left='25%'),)

grid = (
    Grid(init_opts=opts.InitOpts(width="1600px", height="1000px"))
        .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%", pos_left='55%'))
        .add(line, grid_opts=opts.GridOpts(pos_top="60%",pos_left='50%'))

        .add(c, grid_opts=opts.GridOpts(pos_bottom="60%",pos_right='55%'))
        .add(scatter, grid_opts=opts.GridOpts(pos_top="60%",pos_right='55%'))
        .render()
)
