from plotly.graph_objects import Bar, Layout
from plotly import offline
from die import Die

die = Die()
die_10 = Die(10)

max_result = die_10.sides_num + die.sides_num

# 获得抛骰子结果
results=[die.roll+die_10.roll for result in range(5000)]

# 获得对应的频率
frequencies=[results.count(side) for side in range(2, max_result+1)]

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# 布局设置   dtick设置显示刻度的间距大小
x_axis_config = {'title':'result','dtick':1}
y_axis_config = {'title':'frequences'}
myLayout = Layout(title = '1000 times roll of two different die', xaxis = x_axis_config, yaxis = y_axis_config)

# 画图
offline.plot({'data':data, 'layout':myLayout}, filename = 'dd6.html')