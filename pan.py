import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

df = pd.read_csv("virat.csv")
#print(df.head())
# print(" Total runs:", df["Runs"].sum())
# print("Total balls", df["BF"].sum())
# print(" Avg SR",df["SR"].mean())
#print(df["Pos"].value_counts())

pos = df["Pos"].unique()
df["Pos"] = df["Pos"].map(
    {3.0:"Batting at 3",
    4.0: "Batting at 4",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6",
    2.0: "Batting at 2",
    1.0: "Batting at 1"
    }
)

# print(df[["Runs", "Pos"]])
#t= df["Pos"].value_counts()
# print(df["Pos"].value_counts())

# pos_coount= t.values
# label = t.index

# fig = plt.figure(figsize=(18,7))
# plt.pie(pos_coount, labels= label)

# plt.show()

#
# +
# print(df)
#...Total run scored with diff grounds
# def show_pie_plots(df, key):
#     counts = df[key].value_counts()
#     print(counts)
#     count_value= counts.values
#     count_label= counts.index
#     fig = plt.figure(figsize= (18,7))
#     plt.pie(count_value, labels=count_label)
#     plt.show()

# show_pie_plots(df, "Ground")

# bat_at_pos =  df.groupby("Pos")["6s"].sum()
# print(bat_at_pos)
# run_at_pos_values = bat_at_pos.values
# run_at_pos_label = bat_at_pos.index

# fig = plt.figure(figsize= (9,5))
# plt.bar(
#     run_at_pos_label,
#     run_at_pos_values,
#     color="green",
#     width=0.2
# )
# plt.show()

#runs at diff country
#run_at_count = df.groupby("Opposition")["Runs"].sum()
# run_at_pos_values = run_at_count.values
# run_at_pos_label = run_at_count.index

fig = plt.figure(figsize= (9,5))
# plt.bar(
#     run_at_pos_label,
#     run_at_pos_values,
#     color="green",
#     width=0.2
# )
# plt.show()

# centuries = df.query("Runs >= 100")
# print(centuries)

# innings = centuries["Inns"].value_counts()
# inns = centuries["Runs"]
# plt.pie(innings.values, labels=innings.index)
# plt.show()

dis = df["Dismissal"].value_counts()
plt.pie(dis.values, labels= dis.index)
plt.show()
# plt.bar(innings, inns)
# plt.show()

# print(df.tail(10))
# df.info()
# print(df.shape)
# print(df["Runs"].describe())
# runfrequency = df["Opposition"].value_counts()
# print(runfrequency)

# new_df = df[["Runs","SR","Opposition"]]
# print(new_df)

# v_aus = df[df["Opposition"] == "v Australia"]
# print(v_aus)
#  v_cen = df[]


# print(df[df["Runs"]>= 100])#Virat scored a century
# print(df[df["SR"]>100])#SR Greater than century
# cen = (df["Opposition"]== "v Sri Lanka") & (df["Runs"]>= 100)
# print(df[cen])

# def fun_cent(x):
#     if x>=100:
#         return "OG"
#     else:
#         return "NOOB"
# df["Centuries"] = df["Runs"].apply(fun_cent)
# print(df.head(-10))

