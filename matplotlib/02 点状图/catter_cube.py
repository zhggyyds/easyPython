import matplotlib.pyplot as plt

x = range(1,10000)
y = [i**3 for i in x]

# 选择内置样式
plt.style.use('Solarize_Light2')
flg, ax = plt.subplots()

# 显示前5000个元素，并使用颜色映射
ax.scatter(x[0:5000], y[0:5000], c=y[0:5000], cmap=plt.cm.coolwarm, s=10)

ax.set_title("cube", fontsize=10)
ax.set_xlabel("value", fontsize=10)
ax.set_ylabel("cube of value", fontsize=10)
ax.tick_params(axis="both", labelsize=10)

# 使用matplotlib查看器显示绘制的图表
plt.show()

# plt.savefig('scatter.png', bbox_inches='tight')