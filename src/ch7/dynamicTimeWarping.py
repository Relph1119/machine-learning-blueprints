from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import getData_extend as gd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ch7utils import get_stats

sp = gd.sp

def dtw_dist(x, y):
    distance, path = fastdtw(x, y, dist=euclidean)
    return distance

tseries = []
tlen = 5
for i in range(tlen, len(sp), tlen):
    pctc = sp['Close'].iloc[i-tlen:i].pct_change()[1:].values * 100
    res = list(sp['Close'].iloc[i-tlen:i+1].pct_change())[-1] * 100
    tseries.append((pctc, res))

#print(tseries[0])
dist_pairs = []
for i in range(len(tseries)):
    for j in range(len(tseries)):
        dist = dtw_dist(tseries[i][0], tseries[j][0])
        dist_pairs.append((i, j, dist, tseries[i][1], tseries[j][1]))

dist_frame = pd.DataFrame(dist_pairs, columns=['A', 'B', 'Dist', 'A Ret', 'B Ret'])
sf = dist_frame[dist_frame['Dist']>0].sort_values(['A', 'B']).reset_index(drop=1)
sfe = sf[sf['A']<sf['B']]

winf = sfe[(sfe['Dist']<=1)&(sfe['A Ret']>0)]
#print(winf)

plt.plot(np.arange(4), tseries[6][0])
plt.show()

plt.plot(np.arange(4), tseries[598][0])
plt.show()

excluded = {}
return_list = []
def get_returns(r):
    if excluded.get(r['A']) is None:
        return_list.append(r['B Ret'])
        if r['B Ret'] < 0:
            excluded.update({r['A']:1})
winf.apply(get_returns, axis=1)

get_stats(pd.Series(return_list))