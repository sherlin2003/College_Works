import pandas as pd
data = pd.read_csv("Z:\\5th-sem\\MLL\\data.csv")
df= pd.DataFrame(data)
data.head()
print(data)
mean_data = df.mean()
median_data=df.median()
mode_data=df.mode()
std_data=df.std()
skew_data = df.skew()
kurt_data=df.kurt()
cov_data=df.cov()
corr_data=df.corr()
print("Mean:\n", mean_data,"\n")
print("Median:\n", median_data,"\n")
print("Mode:\n", mode_data,"\n")
print("Standard deviation:\n", std_data,"\n")
print("Skeweness:\n", skew_data,"\n")
print("Kurtosis:\n", kurt_data,"\n")
print("Covariance:\n", cov_data,"\n")
print("Correlation:\n", corr_data,"\n")




