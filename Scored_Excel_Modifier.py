import pandas as pd
import urllib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import pickle
import numpy as np

print("Attempting to load file US_Videos_Unclean")
df_youtube_videos = pd.read_pickle("US_Videos_Unclean")
print("Loaded pickled file")
print("Attempting to load file scores_dict..")
scores_dict = pickle.load( open( "scores_dict.p", "rb" ) )
print("Loaded pickled file")

video_id_column = df_youtube_videos['video_id']
scores_list = list()
length = len(video_id_column)
dict_id_values = scores_dict.keys()
zero_count = 0

print("Length of videos: ", length)

# For every ID in the youtube video ID column
for i in range(length):
    print("I:", i)
    current_id = video_id_column[i]
    if current_id in dict_id_values:
        scores_list.append(scores_dict[current_id][0])
        print("Appending: ", scores_dict[current_id][0])
    else:
        scores_list.append(0) # FOr now we will assume 0 comments means 0 toxcity.
        print("Appending 0")
        zero_count += 1

print("Length of scores_list: ", len(scores_list))
print("Length of dictionary: ", len(scores_dict))
print("Zero count: ", zero_count)

if len(scores_list) != 7998:
    print("ERROR JAROM MESSUED UP SOMEWHERE")

df_youtube_videos['toxic_scores'] = scores_list

print("Pickling file")
df_youtube_videos.to_pickle("US_Videos_Score_Added_Unclean")
print("Finished Pickling File")

