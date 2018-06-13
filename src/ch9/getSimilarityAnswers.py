import getData as gd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

convo_frame = gd.convo_frame

vectorizer = TfidfVectorizer(ngram_range=(1,3))
vec = vectorizer.fit_transform(convo_frame['q'])

#my_q = vectorizer.transform(['Hi. My name is Alex.'])
#cs = cosine_similarity(my_q, vec)
#rs = pd.Series(cs[0]).sort_values(ascending=False)
#top5 = rs.iloc[0:5]
#print(top5)
#print(convo_frame.iloc[top5.index]['q'])
#rsi = rs.index[0]
#print(rsi)
#print(convo_frame.iloc[rsi]['a'])

def get_respsonse(q):
    my_q = vectorizer.transform([q])
    cs = cosine_similarity(my_q, vec)
    rs = pd.Series(cs[0]).sort_values(ascending=False)
    rsi = rs.index[0]
    print(convo_frame.iloc[rsi]['a'])
    return convo_frame.iloc[rsi]['a']

get_respsonse('Yes, I am clearly more clever than you will ever be!')
get_respsonse('You are a stupid machine. Why must I prove anything to you?')
get_respsonse('My spirit animal is a menacing cat. What is yours?')
get_respsonse("I mean I didn't actually name it")
get_respsonse("Do you have a name suggestion?")
get_respsonse("I think it might be a bit aggressive for a kitten")
get_respsonse("No need to involve the police")
get_respsonse("And I you, Cleverbot")