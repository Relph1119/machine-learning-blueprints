import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df = pd.DataFrame({'U1':[2, None, 1, None, 3],
                   'U2':[None, 3, None, 4, None],
                   'U3':[4, None, 5, 4, None],
                   'U4':[None, 3, None, 4, None],
                   'U5':[5, None, 4, None, 5]})
df.index =['S1', 'S2', 'S3', 'S4', 'S5']

def get_sim(ratings, target_user, target_item, k=2):
    centered_ratings = ratings.apply(lambda x: x - x.mean(), axis=1)
    csim_list = []
    for i in centered_ratings.index:
        csim_list.append(cosine_similarity(np.nan_to_num(centered_ratings.loc[i,:].values).reshape(1, -1),
                                           np.nan_to_num(centered_ratings.loc[target_item,:]).reshape(1, -1)).item())
    new_ratings = pd.DataFrame({'similarity': csim_list,'rating': ratings[target_user]},
                               index=ratings.index)
    top = new_ratings.dropna().sort_values('similarity', ascending=False)[:k].copy()
    top['multiple'] = top['rating'] * top['similarity']
    result = top['multiple'].sum()/top['similarity'].sum()
    return result

print(get_sim(df, 'U3', 'S5', 2))



