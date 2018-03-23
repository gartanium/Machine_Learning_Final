import pandas as pd
print("Attempting to load file..")
df = pd.read_excel("UScomments.xlsx")
df = df.dropna(axis=1, how='any')
print("Loaded excel file")
print("Pickling file")
df.to_pickle("US_Comments_Unclean")
print("Finished Pickling File")


