import seaborn as sns
import matplotlib.pyplot as plt

print(sns.get_dataset_names())
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
penguins = sns.load_dataset("penguins")

print(tips.head())
