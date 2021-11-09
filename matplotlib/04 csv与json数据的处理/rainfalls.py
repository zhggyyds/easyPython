import csv
from matplotlib import pyplot as pl
from datetime import datetime

# 死亡谷或者斯特卡天气数据csv文件
filename = '/Users/zhouhao/Desktop/本地仓库/Python/py源代码文件/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv'
# filename = '/Users/zhouhao/Desktop/本地仓库/Python/py源代码文件/chapter_16/the_csv_file_format/data/death_valley_2018_simple.csv'

with open(filename) as f:
    # reader处理每行以逗号分隔的数据，并将其存放在列表中
    reader = csv.reader(f)
    header_row = next(reader)

    for index, type in enumerate(header_row):
          print(index,type)
    
    dates, rainfalls = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        # 通过try-except-else的处理将因本缺失数据的文件又能正常的运行
        try:
            rainfall = row[3]
        except ValueError:
            print(f"the data which have error from {date}")
        else:
            dates.append(date)
            rainfalls.append(rainfall)
        
pl.style.use('seaborn')
fig, ax = pl.subplots(figsize = (20,13))
width = 0.5
# ax.plot(dates, rainfalls, c='red', alpha = 0.5)
ax.bar(dates, rainfalls, width, label='points')
ax.set_title("the rainfall of every day in 2018",fontsize = 15)
ax.set_xlabel('date', fontsize = 15)
ax.set_ylabel('Fahrenheit', fontsize = 15)
# 设置坐标轴旋转
pl.xticks(rotation=15) 
# 设置坐标刻度大小
ax.tick_params(axis='both', which = 'major', labelsize = 8)

pl.show()
