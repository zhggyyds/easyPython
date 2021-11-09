import csv
from os import read
from matplotlib import pyplot as pl
from datetime import datetime
import numpy as np

filename = '/Users/zhouhao/Desktop/本地仓库/Python/py源代码文件/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv'
# filename = '/Users/zhouhao/Desktop/本地仓库/Python/py源代码文件/chapter_16/the_csv_file_format/data/death_valley_2018_simple.csv'

with open(filename) as f:
    # reader处理每行以逗号分隔的数据，并将其存放在列表中
    reader = csv.reader(f)
    header_row = next(reader)

    for index, type in enumerate(header_row):
          print(index,type)
    
    highs,dates,lows = [], [], []
    for row in reader:
        date = datetime.strptime(row['DATE'], '%Y-%m-%d')
        # 通过try-except-else的处理将因本缺失数据的文件又能正常的运行
        try:
            high = int(row['TMAX'])
            low = int(row['TMIN'])
        except ValueError:
            print(f"the data which have error from {date}")
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)
        
pl.style.use('seaborn')
fig, ax = pl.subplots()

ax.plot(dates, highs,'r-', dates, lows,'b-',alpha = 0.5)
# 设置两条折线之间空白处的格式
ax.fill_between(dates,lows,highs, facecolor = 'blue', alpha = 0.5)
ax.set_title(f"the temprature of every day in 2018",fontsize = 15)
ax.set_xlabel('date', fontsize = 15)
ax.set_ylabel('Fahrenheit', fontsize = 15)
ax.set_ylim(10,150)# 设置坐标的范围
fig.autofmt_xdate()
ax.tick_params(axis='both', which = 'major', labelsize = 15)

pl.show()
