import pandas as pd
import urllib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import pickle

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

id_column = df['video_id'].values
comment_column = df['comment_text'].values
length = len(comment_column)
scores_list = list()
score = 0
id_old = id_column[0]
id_new = id_column[0]
comment_count = 0

# Cycle through every row
for i in range(length):
    # Check to see if the new ID is equal to the old ID
    print(i)
    id_new = id_column[i]
    temp_score = clf.predict(comment_column[i])
    score += temp_score
    comment_count += 1

    if id_old != id_new:
      score = score / comment_count
      scores_list.append(score)
      score = 0
      comment_count = 0
      id_old = id_new


video_count_const = 7998

if len(scores_list) != video_count_const:
    print("ERROR JAROM MESSUED UP SOMEWHERE")

df_youtube_videos['toxicity_score'] = scores_list

print("Pickling file")
df_youtube_videos.to_pickle("US_Videos_Score_Added_Unclean")
print("Finished Pickling File")


