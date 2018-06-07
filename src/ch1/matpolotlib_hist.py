import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas_learning

mpl.use('TkAgg')
fig, ax = plt.subplots(figsize=(6,4))
ax.hist(pandas_learning.df['petal width'], color='black')
ax.set_ylabel('Count', fontsize=12)
ax.set_xlabel('Width', fontsize=12)
plt.title('Iris Petal Width', fontsize=14, y=1.01)
plt.show()