from pyecharts.charts import ThemeRiver
import pyecharts.options as opts
import pandas as pd
# 导入数据
data = pd.read_csv('E:\python\sale_amount.csv',index_col='date')
series = data.columns.values

data_list = []
for se in series:
    for x,y in zip(data[se].index,data[se].values):
        data_list.append([x,int(y),se])




# 绘制，设置类型为时间
wc = ThemeRiver(init_opts=opts.InitOpts(height='600px'))\
    .add(series_name=series, data=data_list, singleaxis_opts=opts.SingleAxisOpts(type_='time'))\
    .render()
