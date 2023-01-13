import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

df = pd.read_csv("virat.csv")
def show_pie_plots(df, key):
    counts = df[key].value_counts()
    print(counts)
    count_value= counts.values
    count_label= counts.index
    fig = plt.figure(figsize= (18,7))
    plt.pie(count_value, labels=count_label)
    plt.show()

show_pie_plots(df, "Opposition")


