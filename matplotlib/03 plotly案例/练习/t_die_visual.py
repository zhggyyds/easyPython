from plotly.graph_objects import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

max_result = die_1.sides_num + die_2.sides_num+die_3.sides_num

# 获得抛骰子结果
results=[]
for result in range(5000):
    result = die_1.roll()+die_2.roll()+die_3.roll()
    results.append(result)

# 获得对应的频率
frequencies=[]
for side in range(3, max_result+1):
    frequencies.append(results.count(side))

x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# 布局设置   dtick设置显示刻度的间距大小
x_axis_config = {'title':'result','dtick':1}
y_axis_config = {'title':'frequences'}
myLayout = Layout(title = '5000 times roll of two different die', xaxis = x_axis_config, yaxis = y_axis_config)

# 画图
offline.plot({'data':data, 'layout':myLayout}, filename = 'td6.html')