import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
import sys

ipos = pd.read_csv(os.path.dirname(sys.path[0])+ os.path.sep + 'data' + os.path.sep + 'ipo_data.csv', encoding='latin-1')
#print(ipos)

ipos = ipos.applymap(lambda x: x if not '($' in str(x) else x.replace('($','-'))
ipos = ipos.applymap(lambda x: x if not ')' in str(x) else x.replace(')',''))
ipos = ipos.applymap(lambda x: x if not '$' in str(x) else x.replace('$',''))
ipos = ipos.applymap(lambda x: x if not '%' in str(x) else x.replace('%',''))

#print(ipos.info())

ipos.replace('N/C', 0, inplace=True)
ipos['Date'] = pd.to_datetime(ipos['Date'])
ipos['Offer Price'] = ipos['Offer Price'].astype('float')
ipos['Opening Price'] = ipos['Opening Price'].astype('float')
ipos['1st Day Close'] = ipos['1st Day Close'].astype('float')
ipos['1st Day % Px Chng '] = ipos['1st Day % Px Chng '].astype('float')
ipos['$ Change Close'] = ipos['$ Change Close'].astype('float')
ipos['$ Change Opening'] = ipos['$ Change Opening'].astype('float')
ipos['Star Ratings'] = ipos['Star Ratings'].astype('int')
#print(ipos.info())

