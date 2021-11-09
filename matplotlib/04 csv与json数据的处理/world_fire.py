import csv
import plotly.express as px
import pandas as pd

filename = '/Users/zhouhao/Desktop/本地仓库/Python/py源代码文件/chapter_16/the_csv_file_format/data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lons, lats, bris = [], [], []
    for row in reader:
        lon = float(row[1])
        lat = float(row[0])
        bri = float(row[2])

        lons.append(lon)
        lats.append(lat)
        bris.append(bri)

data = pd.DataFrame(
    zip(lons, lats, bris), columns=['lon', 'lat', 'bri']
)

fig = px.scatter(
    data,
    x = 'lon',
    y = 'lat',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title = '全球火灾图',
    size='bri',
    size_max=10,
    color = 'bri'
)

fig.show()
