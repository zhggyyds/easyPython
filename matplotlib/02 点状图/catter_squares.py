import matplotlib.pyplot as plt

x = range(1,100)
y = [i**2 for i in x]

# 选择内置样式
plt.style.use('Solarize_Light2')
flg, ax = plt.subplots()

# 绘制图表
ax.scatter(x, y, c=y, cmap=plt.cm.Reds, s=10)

ax.set_title("squares", fontsize=10)
ax.set_xlabel("value", fontsize=10)
ax.set_ylabel("squares of value", fontsize=10)
ax.tick_params(axis="both", labelsize=10)

# 使用matplotlib查看器显示绘制的图表
plt.show()

# plt.savefig('scatter.png', bbox_inches='tight')
