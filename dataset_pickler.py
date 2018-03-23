import pandas as pd
print("Attempting to load file..")
df = pd.read_excel("USvideos.xlsx")
df = df.dropna(axis=1, how='any')
print("Loaded excel file")
print("Pickling file")
df.to_pickle("US_Videos_Unclean")
print("Finished Pickling File")

