from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis(['音乐', '阅读', '足球', '小提琴', '象棋', '舞蹈'])
bar.add_yaxis('班级1', [21, 22, 16, 9, 19, 7])
bar.add_yaxis('班级2', [26, 30, 10, 17, 26, 30])
bar.add_yaxis('班级3', [13, 20, 5, 18, 10, 16])

bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title='各班兴趣调查',
        subtitle='2019/5/10'
    )

)
bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),
    markpoint_opts=opts.MarkPointOpts(
        data=[opts.MarkPointItem(type_='max', name='最大值'), opts.MarkPointItem(type_='min', name='最大值')]

    )
)
bar.render()
