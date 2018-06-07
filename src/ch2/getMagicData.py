import os
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import sys

pd.set_option("display.max_columns", 30)
pd.set_option("display.max_colwidth", 100)
pd.set_option("display.precision", 3)

CSV_PATH = os.path.dirname(sys.path[0])+ os.path.sep + 'data' + os.path.sep + 'magic.csv'
df = pd.read_csv(CSV_PATH)
#print(df.columns)
#df.head().T

mu = df[df['listingtype_value'].str.contains('Apartments For')]
su = df[df['listingtype_value'].str.contains('Apartment For')]
#print(len(mu))
#print(len(su))

#print(su['propertyinfo_value'])

bd_studio_num = len(su[~(su['propertyinfo_value'].str.contains('Studio') | su['propertyinfo_value'].str.contains('bd'))])
#print(bd_studio_num)

ba_num = len(su[~(su['propertyinfo_value'].str.contains('ba'))])
#print(ba_num)

no_baths = su[~(su['propertyinfo_value'].str.contains('ba'))]
sucln = su[~su.index.isin(no_baths.index)]

def parse_info (row):
    if not 'sqft' in row:
        br, ba = row.split('•')[:2]
        sqft = np.nan
    else:
        br, ba, sqft = row.split('•')[:3]
    return pd.Series({'Beds':br, 'Baths':ba, 'Sqft':sqft})
attr = sucln['propertyinfo_value'].apply(parse_info)
attr_cln = attr.applymap(lambda x: x.strip().split(' ')[0] if isinstance(x, str) else np.nan)
#print(attr_cln)

sujnd = sucln.join(attr_cln)

def parse_addy(r):
    so_zip = re.search(', NY(\d+)', r)
    so_flr = re.search('(?:APT|#)\s+(\d+)[A-Z]+', r)
    if so_zip:
        zipc = so_zip.group(1)
    else:
        zipc = np.nan
    if so_flr:
        flr = so_flr.group(1)
    else:
        flr = np.nan
    return pd.Series({'Zip':zipc, 'Floor':flr})

flrzip = sujnd['routable_link/_text'].apply(parse_addy)
suf = sujnd.join(flrzip)
#print(suf.T)

sudf = suf.loc[:,['pricelarge_value_prices', 'Beds', 'Baths', 'Sqft', 'Floor', 'Zip']]
sudf.rename(columns={'pricelarge_value_prices':'Rent'}, inplace=True)
sudf.reset_index(drop=True, inplace=True)
