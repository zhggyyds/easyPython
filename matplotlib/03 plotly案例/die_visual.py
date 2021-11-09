from plotly.graph_objects import Bar, Layout
from plotly import offline
from die import Die

die = Die()

# 获得抛骰子结果
results=[die.roll()for result in range(1000)]

# 获得对应的频率
frequencies=[results.count(side) for side in range(1, die.sides_num+1)]

x_values = list(range(1,die.sides_num+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'result'}
y_axis_config = {'title':'frequences'}
myLayout = Layout(title = '1000 times roll', xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data':data, 'layout':myLayout}, filename = 'd6.html')