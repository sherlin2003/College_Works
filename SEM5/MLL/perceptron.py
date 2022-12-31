
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
from sklearn.linear_model import Perceptron
p = Perceptron()
p.fit(X_train, y_train)


from sklearn.metrics import accuracy_score
trainPredictions = p.predict(X_train)
testPredictions = p.predict(X_test)
train_score = accuracy_score(trainPredictions, y_train)
print("score on train data: ", train_score)
test_score = accuracy_score(testPredictions, y_test)
print("score on test data: ", test_score)
for i in zip(y_test, testPredictions):
    if(i[0]==i[1]):
        print(i, ":D")
    else:
        print(i, "D:")