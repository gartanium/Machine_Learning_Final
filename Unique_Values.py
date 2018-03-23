import pandas as pd

print("Attempting to load file..")
df = pd.read_pickle("US_Videos_Unclean")
print("Loaded pickled file")

print("Unique values: ")
print(df['views'].unique())
