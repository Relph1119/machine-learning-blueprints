import analysisData as ald
import patsy

import statsmodels.api as sm

sudf = ald.sudf
su_lt_two = sudf[sudf['Beds']<2]

f = 'Rent ~ Zip + Beds'
y, X = patsy.dmatrices(f, su_lt_two, return_type='dataframe')

results = sm.OLS(y, X).fit()
#print(results.summary())