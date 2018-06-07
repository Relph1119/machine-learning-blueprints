import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas_learning as pdl

fig, ax = plt.subplots(2,2, figsize=(6,4))

ax[0][0].hist(pdl.df['petal width'], color='black')
ax[0][0].set_ylabel('Count', fontsize=12)
ax[0][0].set_xlabel('Width', fontsize=12)
ax[0][0].set_title('Iris Petal Width', fontsize=14, y=1.01)

ax[0][1].hist(pdl.df['petal length'], color='black')
ax[0][1].set_ylabel('Count', fontsize=12)
ax[0][1].set_xlabel('Length', fontsize=12)
ax[0][1].set_title('Iris Petal Length', fontsize=14, y=1.01)

ax[1][0].hist(pdl.df['sepal width'], color='black')
ax[1][0].set_ylabel('Count', fontsize=12)
ax[1][0].set_xlabel('Width', fontsize=12)
ax[1][0].set_title('Iris Sepal Width', fontsize=14, y=1.01)

ax[1][1].hist(pdl.df['sepal length'], color='black')
ax[1][1].set_ylabel('Count', fontsize=12)
ax[1][1].set_xlabel('Length', fontsize=12)
ax[1][1].set_title('Iris Sepal Length', fontsize=14, y=1.01)

plt.tight_layout()
plt.show()