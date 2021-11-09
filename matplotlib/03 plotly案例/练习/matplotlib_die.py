"""使用matplolib绘制柱状图"""

import matplotlib.pyplot as plt
import numpy as np
from die import Die

die = Die()

# 获得抛骰子结果
results=[die.roll()for result in range(1000)]
# 获得对应的频率
frequencies=[results.count(side) for side in range(1, die.sides_num+1)]

x_value = list(range(1,die.sides_num+1))
width = 0.35
x_std = [2, 3, 4, 1, 2,1] # 设置柱状图上的黑线

fig, ax = plt.subplots()

ax.bar(x_value, frequencies, width, yerr=x_std, label='points')
ax.set_ylabel('times')

plt.show()