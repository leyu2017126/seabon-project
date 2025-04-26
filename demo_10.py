import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
iris = sns.load_dataset('iris')
print(iris.head())

# 指定中文字体（Windows 下常见的“SimHei”或“Microsoft YaHei”）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
# 让负号正常显示
plt.rcParams['axes.unicode_minus'] = False

sns.pairplot(data=iris, hue="species", diag_kind="kde")
plt.show()
