import pandas as pd
import urllib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import pickle
import numpy as np

filename = 'finalized_model.sav'

# load the model from disk
print("Loading model from disk")
clf = pickle.load(open(filename, 'rb'))
print("Successfully loaded model from disk")

print("Attempting to load file..")
df_youtube_videos = pd.read_pickle("US_Videos_Unclean")
print("Loaded pickled file")

print("Attempting to load file..")
df = pd.read_pickle("US_Comments_Unclean")
print("Loaded pickled file")

#df.dropna(subset=['video_id'])

id_column = df['video_id'].values
comment_column = df['comment_text'].values
length = len(comment_column)
scores_dict = {}
score = 0
id_old = id_column[0]
id_new = id_column[0]
comment_count = 0


# Cycle through every row
for i in range(2, length):
    # Check to see if the new ID is equal to the old ID
    if not isinstance(comment_column[i], basestring):
        temp_score = 0.0
        comment_count += 1.0
        score+= temp_score
    else:
        id_new = id_column[i]
        if id_old != id_new:
            score = score / comment_count
            print(i, id_old, id_new, score)
            scores_dict.update({id_old : score})
            score = 0.0
            comment_count = 0.0
            id_old = id_new

        temp_score = clf.predict([comment_column[i]])
        score += temp_score
        comment_count += 1.0

print("Finished scoring list. Size: ", len(scores_dict))
print("Beginning pickleing file")
pickle.dump( scores_dict, open( "scores_dict.p", "wb" ) )
print("Finished Pickleing file")
