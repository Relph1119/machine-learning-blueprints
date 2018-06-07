import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas_learning as pdl

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(pdl.df['petal length'], color='blue')
ax.set_ylabel('Sepecimen Number')
ax.set_xlabel('Petal Length')
ax.set_title('Petal Length Plot')
plt.show()