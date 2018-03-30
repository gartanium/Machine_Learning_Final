import pandas as pd
print("Attempting to load file..")
#df = pd.read_excel("C:\Users\Matthew\Downloads\UScomments.csv.xlsx")
df = pd.read_csv("C:/Users/Matthew/Downloads/UsComments/New_US_Comments.csv")
print("Loaded excel file")
print("Pickling file")
df.to_pickle("US_Comments_Unclean")
print(df.head(5))
print("Finished Pickling File")


