import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
tips = sns.load_dataset('tips')
print(tips.head())

# 指定中文字体（Windows 下常见的“SimHei”或“Microsoft YaHei”）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
# 让负号正常显示
plt.rcParams['axes.unicode_minus'] = False

# 绘制箱图
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker")
plt.title("按是否吸烟绘制账单分布箱线图")
plt.show()
