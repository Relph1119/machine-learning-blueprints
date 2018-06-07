import os
import sys
import pandas as pd
import requests
import numpy as np

PATH = os.path.dirname(sys.path[0])+ os.path.sep + 'data' + os.path.sep

#r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
#with open(PATH + 'iris.data', 'w') as f:
#    f.write(r.text)

os.chdir(PATH)
df = pd.read_csv(PATH + 'iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
df.head()
#print(df.ix[:3,:2])
#print(df.ix[:3, [x for x in df.columns if 'width' in x]])
#print(df['class'].unique())
#print(df[df['class']=='Iris-virginica'])
#virginica = df[df['class']=='Iris-virginica'].reset_index(drop=True)
#print(virginica)
#print(df[(df['class']=='Iris-virginica')&(df['petal width']>2.2)])
#print(df.describe(percentiles=[.20,.40,.80,.90,.95]))
#print(df.corr())
#df['class'] = df['class'].map({'Iris-setosa':'SET', 'Iris-virginica':'VIR', 'Iris-versicolor':'VER'})
#df['wide petal'] = df['petal width'].apply(lambda v: 1 if v>=1.3 else 0)
#df['petal area'] = df.apply(lambda r: r['petal length']*r['petal width'], axis=1)
#df = df.applymap(lambda v: np.log(v) if isinstance(v, float) else v)
#print(df)