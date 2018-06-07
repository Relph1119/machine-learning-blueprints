import pandas_learning as pdl
import seaborn as sns
import matplotlib.pyplot as plt

g = sns.pairplot(pdl.df, hue="class")
plt.show()