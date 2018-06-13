from sklearn.metrics import jaccard_similarity_score
from scipy.stats import pearsonr
import getStarted as gs
import pandas as pd

fdf = gs.fdf

sim_score = {}
for i in range(len(fdf)):
    ss = pearsonr(fdf.iloc[-1,:], fdf.iloc[i,:])
    sim_score.update({i: ss[0]})

sf = pd.Series(sim_score).to_frame('similarity')
sf.sort_values('similarity', ascending=False)

