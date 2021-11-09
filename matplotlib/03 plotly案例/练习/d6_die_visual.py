from plotly.graph_objects import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()

max_result = die_1.sides_num * die_2.sides_num

# 获得抛骰子结果
results=[]
for result in range(5000):
    result = die_1.roll()*die_2.roll()
    results.append(result)

# 获得对应的频率
frequencies=[]
for side in range(1, max_result+1):
    frequencies.append(results.count(side))

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# 布局设置
x_axis_config = {'title':'result'}
y_axis_config = {'title':'frequences'}
myLayout = Layout(title = '5000 times roll of two different die', xaxis = x_axis_config, yaxis = y_axis_config)

# 画图
offline.plot({'data':data, 'layout':myLayout}, filename = 'd6*.html')