import getFeature as gft
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model

X = gft.X
ipos = gft.ipos
X_train, X_test = X[173:], X[:173]
y_train = ipos['$ Chg Open to Close'][173:].map(lambda x: 1 if x>=1 else 0)
y_test = ipos['$ Chg Open to Close'][:173].map(lambda x: 1 if x>=1 else 0)

clf = linear_model.LogisticRegression()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)