# 使用plotly的express模块实现散点图

import json
import plotly.express as px 
import pandas as pd

filename = "/Users/zhouhao/Desktop/本地仓库/Python/py源代码文件/chapter_16/the_csv_file_format/data/eq_data_30_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

# 运行以下代码，将原本不适合人阅读的json文件以适合人类阅读的方式写入另一个json文件（由于文件信息多不适合直接输出）
# readable_file = "/Users/zhouhao/Desktop/本地仓库/Python/py源代码文件/chapter_16/the_csv_file_format/data/readable_file.json"
# with open(readable_file, 'w') as f:
#     readable_data = json.dump(all_eq_data, f, indent= 4) # indent代表缩进量为4

# 此处生成一个列表,包含所有关于地震的信息,列表中嵌套着字典, 每个字典内是每次地震的信息
all_eq_list = all_eq_data['features']
title = all_eq_data['metadata']['title']

mags, titles, lons, lats = [], [], [], []
# 遍历整个列表
for dict in all_eq_list:
    mags.append(dict['properties']['mag'])
    titles.append(dict['properties']['title'])
    lons.append(dict['geometry']['coordinates'][0])
    lats.append(dict['geometry']['coordinates'][1])

data = pd.DataFrame(
    zip(lons, lats, titles, mags), columns = ['longitude', 'latitude', 'title', 'magtitude']
) 

fig = px.scatter(
    data,
    x= 'longitude',
    y= 'latitude',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title=title,
    # size='magtitude',
    # size_max=10,
    color='magtitude',
    hover_name='title'
)

fig.show()

