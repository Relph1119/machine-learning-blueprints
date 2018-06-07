import analysisData as ald
import sys
import os
import pandas as pd

ipos = ald.ipos
sp = pd.read_csv(os.path.dirname(sys.path[0])+ os.path.sep + 'data' + os.path.sep + 'spy.csv')
sp.sort_values('Date', inplace=True)
sp.reset_index(drop=True, inplace=True)
#print(sp)

def get_week_chg(ipo_dt):
    try:
        day_ago_idx = sp[sp['Date']==str(ipo_dt.date())].index[0] - 1
        week_ago_idx = sp[sp['Date']==str(ipo_dt.date())].index[0] - 8
        chg = (sp.iloc[day_ago_idx]['Close'] - sp.iloc[week_ago_idx]['Close'])/(sp.iloc[week_ago_idx]['Close'])
        return chg*100
    except:
        print('error', ipo_dt.date())

#error 2015-02-21
#error 2015-02-21
#error 2013-11-16
#error 2009-08-01
ipos.ix[1155, 'Date'] = pd.to_datetime('2009-08-12')
ipos.ix[656, 'Date'] = pd.to_datetime('2012-11-20')
ipos.ix[27, 'Date'] = pd.to_datetime('2015-05-21')
ipos.ix[28, 'Date'] = pd.to_datetime('2015-05-21')

ipos['SP Week Change'] = ipos['Date'].map(get_week_chg)

def get_cto_chg(ipo_dt):
    try:
        today_open_idx = sp[sp['Date']==str(ipo_dt.date())].index[0]
        yday_close_idx = sp[sp['Date']==str(ipo_dt.date())].index[0] - 1
        chg = (sp.iloc[today_open_idx]['Open'] - sp.iloc[yday_close_idx]['Close'])/(sp.iloc[yday_close_idx]['Close'])
        return chg * 100
    except:
        print('error', ipo_dt)
ipos['SP Close to Open Chg Pct'] = ipos['Date'].map(get_cto_chg)

ipos['Lead Mgr'] = ipos['Lead/Joint-Lead Managers'].map(lambda x: x.split('/')[0])
ipos['Lead Mgr'] = ipos['Lead Mgr'].map(lambda x: x.strip())
