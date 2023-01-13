import pandas as pd

data = {
    "apples": [4,3,8,1],
    "oranges": [3,7,4,1]
}

# index_title = [
#     "AAaron", "Shands","Jesus", "Wilson"
# ]
df = pd.DataFrame(data ,index= [ "AAaron", "Shands","Jesus", "Wilson"])
#print(df["oranges"].loc[0:])
print(df)
print(df["apples"].iloc[0:3])
print(type(df))