import pandas as pd
import numpy as np
data=pd.read_csv("E:\\SEM5\\MLL\\linearReg.csv")
# print("DESCRIBE:")
#  print(data.describe())
# data.plot.scatter("SOAP","SUD");
# print("DATASET");
# x=data.head()
#  print(x);
# xT = data.transpose();
# print(xT)
n=len(data)
print("n =",n)
Xi=np.sum(data['SOAP'])
print("Xi =",Xi)
Yi=np.sum(data['SUD'])
print("Yi =",Yi)
a=np.square(data['SOAP'])
xi=np.sum(a)
print("xi^2 = ",xi)
xiyi=np.sum(data['SOAP']*data["SUD"])
print("xiyi =",xiyi)

