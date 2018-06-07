import getIPOData as getData
import matplotlib.pyplot as plt

ipos = getData.ipos

#ipos.groupby(ipos['Date'].dt.year)['1st Day % Px Chng '].mean().plot(kind='bar', figsize=(15, 10), color='k',
  #                                                                   title='1st Day Mean IPO Percentage Change')
#plt.show()
#ipos.groupby(ipos['Date'].dt.year)['1st Day % Px Chng '].median().plot(kind='bar', figsize=(15, 10), color='k',
  #                                                                     title='1st Day Median IPO Percentage Change')
#plt.show()
#print(ipos['1st Day % Px Chng '].describe())

#ipos['1st Day % Px Chng '].hist(figsize=(15, 7), bins=100, color='grey')
#plt.show()
ipos['$ Chg Open to Close'] = ipos['$ Change Close'] - ipos['$ Change Opening']
ipos['% Chg Open to Close'] = (ipos['$ Chg Open to Close']/ipos['Opening Price']) * 100

#print(ipos['% Chg Open to Close'].describe())
#ipos['% Chg Open to Close'].hist(figsize=(15, 7), bins=100, color='grey')
#plt.show()

#print(ipos[ipos['Date']>='2015-01-01']['$ Chg Open to Close'].describe())
#print(ipos[ipos['Date']>='2015-01-01']['$ Chg Open to Close'].sum())
#print(ipos[(ipos['Date']>='2015-01-01')&(ipos['$ Chg Open to Close']>0)]['$ Chg Open to Close'].describe())
#print(ipos[(ipos['Date']>='2015-01-01')&(ipos['$ Chg Open to Close']<0)]['$ Chg Open to Close'].describe())