# 使用plotly的go模块实现散点图

import plotly as pl
import plotly.graph_objs as go
from plotly.graph_objects import Layout
from random_walk import RandomWalk

fig = go.Figure()

rm1 = RandomWalk(5000)
rm1.fill_walk()

rm2 = RandomWalk(5000)
rm2.fill_walk()

rm3 = RandomWalk(5000)
rm3.fill_walk()

# x轴数据，y轴数据，点的形状， 点的样式
# trace1 = go.Scatter(x=rm1.x_values, y=rm1.y_values, mode='lines', 
#     marker=dict(
#         size=10, 
#         color='rgba(255, 0, 0, 255)', 
#         line=dict(width=2)
#         )
#     )

# trace2 = go.Scatter(x=rm2.x_values, y=rm2.y_values, mode='markers',
#     marker=dict(
#         size=5, 
#         color='rgba(0, 255, 0, 255)', 
#         line=dict(width=2)
#         )
# )

# trace3 = go.Scatter(x=rm3.x_values, y=rm3.y_values, mode='markers+lines',
#     marker=dict(
#         size=5, 
#         color='rgba(0, 0, 255, 255)', 
#         line=dict(width=2)
#         )
# )
#数据,以下为线下模式的生成图像，并加以保存html文件
# data = [trace1, trace2, trace3]
# pl.offline.plot(data, filename='basic-scatter.html')

# 使用go中的Figure函数创建的变量进行画图
fig.add_trace(go.Scatter(x=rm1.x_values, y=rm1.y_values,
                    mode='markers',
                    name='markers',
                     marker=dict(
                        size=5, 
                        color='rgba(255, 0, 0, 255)', 
                        line=dict(width=2)
        )))
fig.add_trace(go.Scatter(x=rm2.x_values, y=rm2.y_values,
                    mode='lines+markers',
                    name='lines+markers',
                     marker=dict(
                        size=5, 
                        color='rgba(0, 255, 0, 255)', 
                        line=dict(width=2)
        )))
fig.add_trace(go.Scatter(x=rm3.x_values, y=rm3.y_values,
                    mode='lines',
                    name='lines',
                     marker=dict(
                        size=5, 
                        color='rgba(0, 0, 255, 255)', 
                        line=dict(width=2)
        )))

fig.show()

