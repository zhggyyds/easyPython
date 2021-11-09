from random_walk import RandomWalk

import matplotlib.pyplot as plt

while(1):
    rm = RandomWalk(5000)
    rm.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()# 设置图像大小
    point_num = list(range(rm.num))

    ax.scatter(rm.x_values, rm.y_values, c=point_num, cmap=plt.cm.Blues,edgecolors='none',s=5)
    #单独设置起 终点
    ax.scatter(rm.x_values[0],rm.y_values[0], c='green',edgecolors='none', s=100)
    ax.scatter(rm.x_values[-1],rm.y_values[-1], c='red',edgecolors='none', s=100)

    # 设置坐标不可见
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = 'n' # input("Make another walk ? [Y/N]")
    if keep_running == 'n':
        break