import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
tips = sns.load_dataset('tips')
print(tips.head())

# 指定中文字体（Windows 下常见的“SimHei”或“Microsoft YaHei”）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
# 让负号正常显示
plt.rcParams['axes.unicode_minus'] = False

sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={'alpha': 0.5})
plt.title("回归直线示例")
plt.show()

# lmplot：更方便地支持 facet 分组
sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex", col="smoker")
plt.show()
