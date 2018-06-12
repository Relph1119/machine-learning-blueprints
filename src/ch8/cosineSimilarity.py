import getDigitsData as gdd
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from getDigitsData import display_img

digits = gdd.digits

X = digits.data
co_sim = cosine_similarity(X[0].reshape(1, -1), X)
cosf = pd.DataFrame(co_sim).T
cosf.columns = ['similarity']
cosf.sort_values('similarity', ascending=False)
display_img(0)
display_img(877)
display_img(1626)

