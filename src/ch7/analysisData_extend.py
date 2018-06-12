import getData_extend as gd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sp = gd.sp

fig, ax = plt.subplots(figsize=(15, 10))
sp['Close'].plot(color='k')
plt.title("SPY", fontsize=20)
#plt.show()

long_day_rtn = ((sp['Close'] - sp['Close'].shift(1))/sp['Close'].shift(1)) * 100

long_id_rtn = ((sp['Close'] - sp['Open'])/sp['Open']) * 100
long_on_rtn = ((sp['Open'] - sp['Close'].shift(1))/sp['Close'].shift(1)) * 100

#print((sp['Close'] - sp['Close'].shift(1)).sum())
#print((sp['Close'] - sp['Open']).sum())
#print((sp['Open'] - sp['Close'].shift(1)).sum())
def get_stats(s, n=252):
    s = s.dropna()
    wins = len(s[s>0])
    losses = len(s[s<0])
    evens = len(s[s==0])
    mean_w = round(s[s>0].mean(), 3)
    mean_l = round(s[s<0].mean(), 3)
    win_r = round(wins/losses, 3)
    mean_trd = round(s.mean(), 3)
    sd = round(np.std(s), 3)
    max_l = round(s.min(), 3)
    max_w = round(s.max(), 3)
    sharpe_r = round((s.mean()/np.std(s)) * np.sqrt(n), 4)
    cnt = len(s)
    print('Trades:', cnt,
          '\nWins:', wins,
          '\nLosses:', losses,
          '\nBreakeven:', evens,
          '\nWin/Loss Ratio', win_r,
          '\nMean Win:', mean_w,
          '\nMean Loss:', mean_l,
          '\nMean:', mean_trd,
          '\nStd Dev:', sd,
          '\nMax Loss:', max_l,
          '\nMax Win:', max_w,
          '\nSharpe Ratio:', sharpe_r)

get_stats(long_day_rtn)
get_stats(long_id_rtn)
get_stats(long_on_rtn)