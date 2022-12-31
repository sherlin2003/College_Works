import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def findPriors(train, output):
    return train.groupby(output).size().div(len(train))

def constructCPT(train, features, output):
    class_probs = findPriors(train, output)
    cpt = dict()
    for i in features:
        cpt[i] = train.groupby([i, output]).size().div(len(train)).div(class_probs)
    return cpt
    
def predict(test, cpt, label):
    Ypred = []
    class_probs = findPriors(train, output)
    
    for i in range(len(test)):
        X = test[features].iloc[i].tolist()
        probs = []
        for j in label:
            prob = 1
            for i in range(len(X)):
                _cpt = cpt[features[i]]
                if (X[i], j) in _cpt.index:
                    prob *= _cpt[X[i]][j]
            prob *= class_probs[j]
            probs.append((prob, j))
        
        Ypred.append(max(probs)[1])
    return Ypred 


def calcMisclass(Y, Ypred):
    res = 0
    for i in range(len(Y)):
        if Y[i]!=Ypred[i]:
            res+=1
    return res


df = pd.read_csv('breast-cancer-wisconsin.csv', sep=",")

N = len(df)
# (2 for benign, 4 for malignant)

features = [df.columns[i] for i in range(1, 10)]
output = 'Class'

print("FEATURES: ", features)

#  replacing ? with mean
for i in features:
    data = [x for x in df[i] if x!='?']
    data = list(map(int, data))
    mean =  round(np.mean(data))
    df[i] = df[i].replace('?', mean)

df = df.apply(pd.to_numeric)

train, test = train_test_split(df, test_size = 0.2)

trainSize = len(test)
testSize = len(train)
    
    
c1 = df['Class'].value_counts()[2]
c2 = df['Class'].value_counts()[4]

print(c1, c2)

cpt = constructCPT(train, features, output)

label = df[output].unique()

Y = test[output].tolist()
Ypred = predict(test, cpt, label)

print("[Size of testing set] ", len(test))
print("[Misclassifications] ", calcMisclass(Y, Ypred))

