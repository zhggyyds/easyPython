import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 选择内置样式
plt.style.use('Solarize_Light2')
flg, ax = plt.subplots()

# 绘制图表
ax.plot(input_values, squares, linewidth=3)

ax.set_title("squares", fontsize=10)
ax.set_xlabel("value", fontsize=10)
ax.set_ylabel("squares of value", fontsize=10)
ax.tick_params(axis="both", labelsize=10)

# 使用matplotlib查看器显示绘制的图表
plt.show()
