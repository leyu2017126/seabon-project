import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 指定中文字体（Windows 下常见的“SimHei”或“Microsoft YaHei”）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
# 让负号正常显示
plt.rcParams['axes.unicode_minus'] = False

# 1. 数据准备
df = pd.read_csv("sales.csv", parse_dates=["date"])
df['month'] = df['date'].dt.to_period('M').astype(str)

# 2. 月度销售趋势
sns.lineplot(data=df, x="month", y="revenue", estimator='sum')
plt.xticks(rotation=45)
plt.title("月度销售趋势")
plt.tight_layout()
plt.show()

# 3. 产品类别对比
sns.boxplot(data=df, x="category", y="revenue")
plt.title("各类别销售额分布")
plt.show()

# 4. 相关性热图
corr = df[['price', 'quantity', 'revenue']].corr()
sns.heatmap(corr, annot=True, fmt=".2f")
plt.title("关键字段相关性")
plt.show()
