import getData as gd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

spy = gd.spy

spy_c = spy['Close']

fig, ax = plt.subplots(figsize=(15, 10))
spy_c.plot(color='k')
plt.title("SPY", fontsize=20)
#plt.show()

first_open = spy['Open'].iloc[0]
last_open = spy['Close'].iloc[-1]

spy['Daily Change'] = pd.Series(spy['Close'] - spy['Open'])
#print(spy['Daily Change'].sum())

#print(np.std(spy['Daily Change']))

spy['Overnight Change'] = pd.Series(spy['Open'] - spy['Close'].shift(1))
#print(np.std(spy['Overnight Change']))

print(spy[spy['Daily Change']<0]['Daily Change'].mean())
print(spy[spy['Overnight Change']<0]['Overnight Change'].mean())