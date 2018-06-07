import pandas_learning as pdl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

clf = OneVsRestClassifier(SVC(kernel='linear'))
df = pdl.df
X = df.ix[:,:4]
y = np.array(df.ix[:,4]).astype(str)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

rf = pd.DataFrame(list(zip(y_pred, y_test)), columns=['predicted', 'actual'])
rf['correct'] = rf.apply(lambda r: 1 if r['predicted']==r['actual'] else 0, axis=1)
print(rf)
print(rf['correct'].sum()/rf['correct'].count())