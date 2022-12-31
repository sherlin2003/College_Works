import pandas as pd
data = pd.read_csv("Z:\\5th-sem\\MLL\\iris.csv")
data.head()
sum_data = data["sepallength"].sum()
mean_data = data["sepallength"].mean()
median_data = data["sepallength"].median()
mode_data = data["sepallength"].mode()
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data,"\nmode:",mode_data)