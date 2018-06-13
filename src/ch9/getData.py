import pandas as pd
import re
import os
import sys

pd.set_option('display.max_colwidth', 200)

FILE_PATH = os.path.dirname(sys.path[0])+ os.path.sep + 'data' + os.path.sep + 'nscb.csv'
df = pd.read_csv(FILE_PATH)

convo = df.iloc[:,0]
#print(convo)

clist = []
def qa_pairs(x):
    cpairs = re.findall(": (.*?)(?:$|\n)", x)
    clist.extend(list(zip(cpairs, cpairs[1:])))
convo.map(qa_pairs)
convo_frame = pd.Series(dict(clist)).to_frame().reset_index()
convo_frame.columns = ['q','a']
