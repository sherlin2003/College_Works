import pandas as pd
import numpy as np
import seaborn as sbn
from scipy.stats import pearsonr
#from scipy.stats import kurtosis


'''Iris Dataset Exploration'''
data = pd.read_csv("Z:/collegeThings/Sem5/ML/iris.csv")
#data.head()
#print(data.describe())
#meanData = []
#stdDevData = []
#medianData = []
#modeData = []
#meanData = data.mean()
#medianData = data.median()
#modeData = data.mode()
#stdDevData = np.std(data)
#print(stdDevData)
#df = pd.DataFrame(data)
#print(df.skew())
#print(df.kurt()) 
#X = np.stack((data['sepal.length'], data['sepal.width']), axis=0)
#print(np.cov(X))
#X = np.stack((data['petal.length'], data['petal.width']), axis=0)
#print(np.cov(X))
#corr,_ = pearsonr(data['sepal.length'], data['sepal.width'])
#print(corr)
#corr,_ = pearsonr(data['petal.length'], data['petal.width'])
#print(corr)
# boxplot = data.boxplot(figsize=(6,6))
# sbn.boxplot(data['sepal.length'])
# sbn.boxplot(data['sepal.width'])
# sbn.boxplot(data['petal.length'])
# sbn.boxplot(data['petal.width'])

'''Housing Price Prediction Dataset Exploration'''
data = pd.read_csv("Z:/collegeThings/Sem5/ML/data.csv")
#data.head()
#print(data.describe())
#meanData = []
#stdDevData = []
#medianData = []
#modeData = []
#meanData = data.mean()
#medianData = data.median()
#modeData = data.mode()
#stdDevData = np.std(data)
#print(stdDevData)
#df = pd.DataFrame(data)
#print(df.skew())
#print(df.kurt()) 
#X = np.stack((data['price'], data['sqft_lot']), axis=0)
#print(np.cov(X))
#corr,_ = pearsonr(data['price'], data['sqft_lot'])
#print(corr)
 boxplot = data.boxplot(figsize=(4,3))
# sbn.boxplot(data['sepal.length'])
# sbn.boxplot(data['sepal.width'])
# sbn.boxplot(data['petal.length'])
# sbn.boxplot(data['petal.width'])




