import pandas_learning as pdl
import seaborn as sns
import matplotlib.pyplot as plt

df = pdl.df
fig, ax = plt.subplots(2,2, figsize=(7, 7))
sns.set(style='white', palette='muted')
sns.violinplot(x=df['class'], y=df['sepal length'], ax=ax[0, 0])
sns.violinplot(x=df['class'], y=df['sepal width'], ax=ax[0, 1])
sns.violinplot(x=df['class'], y=df['petal length'], ax=ax[1, 0])
sns.violinplot(x=df['class'], y=df['petal width'], ax=ax[1, 1])
fig.suptitle('Violin Plots', fontsize=16, y=1.03)
for i in ax.flat:
    plt.setp(i.get_xticklabels(), rotation=-90)
fig.tight_layout()
plt.show()