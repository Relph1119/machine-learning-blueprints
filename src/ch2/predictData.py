import modelingData as mld
import numpy as np
import pandas as pd

X = mld.X
results = mld.results
#print(X.head())

to_pred_idx = X.iloc[0].index
to_pred_zeros = np.zeros(len(to_pred_idx))
tpdf = pd.DataFrame(to_pred_zeros, index=to_pred_idx, columns=['value'])
#print(tpdf)
tpdf.loc['Intercept'] = 1
tpdf.loc['Beds'] = 1
tpdf.loc['Zip[T.10009]'] = 1
#print(tpdf)

results.predict(tpdf['value'])
