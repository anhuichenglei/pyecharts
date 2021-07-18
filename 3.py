import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

# 内部饼图
inner_x_data = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
inner_y_data = [11, 12, 13, 10, 10]
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]


# 外部环形（嵌套）
outer_x_data = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
outer_y_data = [19, 21, 32, 20, 33]
outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]

c = (
    # 初始化
    Pie(init_opts=opts.InitOpts(
        width="900px",  # 设置图形大小
        height="800px",
        theme=ThemeType.SHINE))  # 选择主题

        # 内部饼图
        .add(
        series_name="版本3.2.1",  # 图形名称
         # 饼图位置
        data_pair=inner_data_pair,  # 系列数据项，格式为 [(key1, value1), (key2, value2)]
        rosetype="area",
        radius=["10%", "40%"],
        center=["50%", "35%"],  # 饼图半径 数组的第一项是内半径，第二项是外半径
        label_opts=opts.LabelOpts(position='inner'),  # 标签设置在内部
    )

        # 外部嵌套环形图
        .add(
        series_name="版本3.2.9",  # 系列名称
        center=["50%", "35%"],  # 饼图位置
        radius=["40%", "80%"],  # 饼图半径 数组的第一项是内半径，第二项是外半径

        data_pair=outer_data_pair,  # 系列数据项，格式为 [(key1, value1), (key2, value2)]

        # 标签配置项
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999",
                      "lineHeight": 22,
                      "align": "center"},

                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },

                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },

                "b": {"fontSize": 16, "lineHeight": 33},

                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )

        # 全局配置项
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_show=False),  # 隐藏X轴刻度
        yaxis_opts=opts.AxisOpts(is_show=False),  # 隐藏Y轴刻度
        legend_opts=opts.LegendOpts(pos_left='left',orient='vertical'),  # 图例居左竖直
        title_opts=opts.TitleOpts(title='各分店销量对比',pos_left='center'),  # 标题

    )

        # 系统配置项
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(is_show=True)  # 隐藏每个触角标签
    )
)

c.render()