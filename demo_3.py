import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
tips = sns.load_dataset('tips')
print(tips.head())

# 指定中文字体（Windows 下常见的“SimHei”或“Microsoft YaHei”）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
# 让负号正常显示
plt.rcParams['axes.unicode_minus'] = False

# 绘制折线图
sns.lineplot(data=tips, x="size", y="total_bill", estimator='mean', errorbar='sd')
plt.title("不同用餐人数的平均账单（含标准差）")
plt.show()
