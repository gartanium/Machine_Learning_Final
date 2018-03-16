import pandas as pd
from sklearn.model_selection import train_test_split

print("Attempting to load file..")
df = pd.read_pickle("US_Videos_Unclean")
print("Loaded pickled file")

course_types = ['GS', 'MATH', 'FDREL', 'ENG', 'Devotional', 'ECI', 'EIL']











print("Pickling file")
df.to_pickle("US_Videos_Cleaned")
print("Finished Pickling File")
