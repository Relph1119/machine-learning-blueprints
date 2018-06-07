import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas_learning as pdl

fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(pdl.df['petal width'], pdl.df['petal length'], color='green')
ax.set_ylabel('Petal Width')
ax.set_xlabel('Petal Length')
ax.set_title('Petal Scatterplot')
plt.show()