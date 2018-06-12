import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb
import pandas_datareader as pdr
import fix_yahoo_finance as yf
import os
import sys

yf.pdr_override()

pd.set_option('display.max_colwidth', 200)
FILE_PATH = os.path.dirname(sys.path[0])+ os.path.sep + 'data' + os.path.sep + 'spy_2010_2016.csv'

# get the spy data from yahoo
#start_date = pd.to_datetime('2010-01-04')
#stop_date = pd.to_datetime('2016-03-01')
#spy = pdr.data.get_data_yahoo('SPY', start_date, stop_date)
#spy.to_csv(FILE_PATH, index_label='Date',columns=spy.columns)

spy = pd.read_csv(FILE_PATH)
