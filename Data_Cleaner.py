import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

print("Attempting to load file..")
df = pd.read_pickle("US_Videos_Score_Added_Unclean")
print("Loaded pickled file")


print("Dropping columns")
df.drop('video_id', axis = 1, inplace=True)
df.drop('title', axis = 1, inplace=True)
df.drop('channel_title', axis = 1, inplace=True)
df.drop('tags', axis = 1, inplace=True)
df.drop('thumbnail_link', axis = 1, inplace=True)
df.drop('date', axis = 1, inplace=True)
print("Finished dropping columns")

print("Min Max Scaling comments")
#scaler = MinMaxScaler(feature_range=(0, 1))


df['views'] = df['views'] / df['views'].max()
df['likes'] = df['likes'] / df['likes'].max()
df['dislikes'] = df['dislikes'] / df['dislikes'].max()

df = df.dropna(axis=1, how='any')

print("Finished Min Max Scaling comments")


print("Pickling file")
df.to_pickle("US_Videos_Cleaned")
print("Finished Pickling File")
