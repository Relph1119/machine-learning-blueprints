import pandas_learning as pdl
import numpy as np

df = pdl.df
#g = df.groupby('class').mean()
# g = df.groupby('class').describe()
# g = df.groupby('petal width')['class'].unique().to_frame()
g = df.groupby('class')['petal width'].agg({'delta': lambda x: x.max() - x.min(), 'max':np.max, 'min':np.min})
print(g)
