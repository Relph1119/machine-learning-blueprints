from sklearn.metrics.pairwise import chi2_kernel
import getDigitsData as gdd
import pandas as pd
from getDigitsData import display_img

digits = gdd.digits
X = digits.data

k_sim = chi2_kernel(X[0].reshape(1, -1), X)
kf = pd.DataFrame(k_sim).T
kf.columns = ['similarity']
kf.sort_values('similarity', ascending=False)
display_img(1167)
display_img(609)
