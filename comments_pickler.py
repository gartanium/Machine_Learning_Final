import pandas as pd
print("Attempting to load file..")
df = pd.read_excel("UScomments.xlsx")

print("Loaded excel file")
print("Pickling file")
df.to_pickle("US_Comments_Unclean")
print(df.head(5))
print("Finished Pickling File")


