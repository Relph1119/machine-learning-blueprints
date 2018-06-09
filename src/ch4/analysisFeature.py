import predictData_2015_1 as predictData
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt

X_train = predictData.X_train
y_train = predictData.y_train
clf = predictData.clf
ipos = predictData.ipos

fv = pd.DataFrame(X_train.columns, clf.coef_.T).reset_index()
fv.columns = ['Coef', 'Feature']
fv.sort_values('Coef', ascending=0).reset_index(drop=True)
#print(fv[fv['Feature'].str.contains('Week Day')])

#print(ipos[ipos['Lead Mgr'].str.contains('Keegan|Towbin')])

clf_rf = RandomForestClassifier(n_estimators=100)
clf_rf.fit(X_train, y_train)
f_importances = clf_rf.feature_importances_
f_names = X_train
f_std = np.std([tree.feature_importances_ for tree in clf_rf.estimators_], axis=0)
zz = zip(f_importances, f_names, f_std)
zzs = sorted(zz, key=lambda x: x[0], reverse=True)
imps = [x[0] for x in zzs[:20]]
labels = [x[1] for x in zzs[:20]]
eers = [x[2] for x in zzs[:20]]
plt.subplots(figsize=(15, 10))
plt.bar(range(20), imps, color="r", yerr=eers, align="center")
plt.xticks(range(20), labels, rotation=70)
plt.show()