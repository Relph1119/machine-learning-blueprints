import getData_extend as gd
import pandas as pd
from ch7utils import get_stats

sp = gd.sp

for i in range(1, 21, 1):
    sp.loc[:, 'Close Minus ' + str(i)] = sp['Close'].shift(i)
sp20 = sp[[x for x in sp.columns if 'Close Minus' in x or x == 'Close']].iloc[20:,]
sp20 = sp20.iloc[:, ::-1]
#print(sp20)

from sklearn.svm import SVR
clf = SVR(kernel='linear')
X_train = sp20[:-2000]
y_train = sp20['Close'].shift(-1)[:-2000]
X_test = sp20[-2000:-1000]
y_test = sp20['Close'].shift(-1)[-2000:-1000]

model = clf.fit(X_train, y_train)
preds = model.predict(X_test)

tf = pd.DataFrame(list(zip(y_test, preds)), columns=['Next Day Close', 'Predicted Next Close'], index=y_test.index)
#print(tf)

cdc = sp[['Close']].iloc[-2000:-1000]
ndo = sp[['Open']].iloc[-2000:-1000].shift(-1)
tf1 = pd.merge(tf, cdc, left_index=True, right_index=True)
tf2 = pd.merge(tf1, ndo, left_index=True, right_index=True)
tf2.columns = ['Next Day Close', 'Predicted Next Close', 'Current Day Close', 'Next Day Open']
#print(tf2)

def get_signal(r):
    if r['Predicted Next Close'] > r['Next Day Open'] + 1:
        return 0
    else:
        return 1
def get_ret(r):
    if r['Signal'] == 1:
        return ((r['Next Day Close'] - r['Next Day Open'])/r['Next Day Open']) * 100
    else:
        return 0
tf2 = tf2.assign(Signal = tf2.apply(get_signal, axis=1))
tf2 = tf2.assign(PnL = tf2.apply(get_ret, axis=1))
#print(tf2)

print((tf2[tf2['Signal'] == 1]['Next Day Close'] - tf2[tf2['Signal']==1]['Next Day Open']).sum())
print((sp['Close'].iloc[-2000:-1000] -sp['Open'].iloc[-2000:-1000]).sum())