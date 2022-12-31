import pandas as pd
data = pd.read_csv("Z:\\5th-sem\\MLL\\iris.csv")
data.head()
print(data)
print("DESCRIBE:")
print(data.describe())
print("MODE:\n", data.mode(),"\n")
df=pd.DataFrame(data)
print("SKWENESS \n",df.skew(),"\n")

print("KURTOSIS\n",df.kurt(),"\n")

print("CORRELATION:\n",data.corr(),"\n")
print("COVARIANCE:\n" ,data.cov(),"\n")
# sum_data = data["sepallength"].sum()
# mean_data = data["sepallength"].mean()
# median_data = data["sepallength"].median()
# mode_data = data["sepallength"].mode()
# print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data,"\n mode:",mode_data)
