import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
tips = sns.load_dataset('tips')
print(tips.head())

# 指定中文字体（Windows 下常见的“SimHei”或“Microsoft YaHei”）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
# 让负号正常显示
plt.rcParams['axes.unicode_minus'] = False

# 绘制条形图
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", errorbar=None)
plt.title("不同星期天账单对比")
plt.show()
