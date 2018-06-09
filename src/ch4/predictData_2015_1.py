import getFeature as gft
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

#2015 1LR
X = gft.X
ipos = gft.ipos
X_train, X_test = X[173:], X[:173]
y_train = ipos['$ Chg Open to Close'][173:].map(lambda x: 1 if x>=1 else 0)
y_test = ipos['$ Chg Open to Close'][:173].map(lambda x: 1 if x>=1 else 0)

clf = linear_model.LogisticRegression()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

#print(ipos[(ipos['Date']>='2015-01-01')]['$ Chg Open to Close'].describe())

pred_label=clf.predict(X_test)
results=[]
for pl, tl, idx, chg in zip(pred_label, y_test, y_test.index, ipos.iloc[y_test.index]['$ Chg Open to Close']):
    if pl == tl:
        results.append([idx, chg, pl, tl, 1])
    else:
        results.append([idx, chg, pl, tl, 0])
rf = pd.DataFrame(results, columns=['index', '$ chg', 'predicted', 'actual', 'correct'])
#print(rf[rf['predicted']==1]['$ chg'].describe())

fig, ax = plt.subplots(figsize=(15, 10))
rf[rf['predicted']==1]['$ chg'].plot(kind='bar')
ax.set_title('Model Predicted Buys', y=1.01)
ax.set_ylabel('$ Change Open to Close')
ax.set_xlabel('Index')
plt.show()