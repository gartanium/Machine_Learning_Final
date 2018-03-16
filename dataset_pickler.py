import pandas as pd
print("Attempting to load file..")
df = pd.read_excel("USvideos.xlsx")
print("Loaded excel file")
print("Pickling file")
df.to_pickle("US_Videos_Unclean")
print("Finished Pickling File")

