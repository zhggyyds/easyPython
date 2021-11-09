from plotly.graph_objects import Bar, Layout
from plotly import offline
from die import Die

die = Die(8)
die_10 = Die(8)

max_result = die_10.sides_num + die.sides_num

# 获得抛骰子结果
results=[]
for result in range(1000):
    result = die.roll()+die_10.roll()
    results.append(result)

# 获得对应的频率
frequencies=[]
for side in range(2, max_result+1):
    frequencies.append(results.count(side))

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# 布局设置   dtick设置显示刻度的间距大小
x_axis_config = {'title':'result','dtick':1}
y_axis_config = {'title':'frequences'}
myLayout = Layout(title = '1000 times roll of two different die', xaxis = x_axis_config, yaxis = y_axis_config)

# 画图
offline.plot({'data':data, 'layout':myLayout}, filename = 'd8.html')