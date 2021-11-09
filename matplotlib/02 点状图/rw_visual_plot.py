from random_walk import RandomWalk

import matplotlib.pyplot as plt

while(1):
    rm = RandomWalk()
    rm.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (20,10))# 设置图像大小
    point_num = list(range(rm.num))

    ax.plot(rm.x_values, rm.y_values, linewidth = 3)

    plt.show()
    
    keep_running = 'n' # input("Make another walk ? [Y/N]")
    if keep_running == 'n':
        break