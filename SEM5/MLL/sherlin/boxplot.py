import pandas as pd

file = pd.read_csv('iris.csv')

mean = file['petal_length'].mean()
print("Mean: ", mean)

median = file['sepal_width'].median()
print("Median: ", median)

mode = file['petal_width'].mode()
print("Mode: ", mode[0])

std = file['petal_length'].std()
print("Standard Deviation: ", std)

skew = file['sepal_width'].skew()
print("Skewness: ", skew)

kurt = file['petal_width'].kurt()
print("Kurtosis: ", kurt)

covar = file['petal_length'].cov(file['petal_width'])
print("Covariance between petal_length and petal_width: ", covar)

corr = file['petal_length'].corr(file['petal_width'])
print("Coefficient of correlation between petal_length and petal_width: ", corr)


# boxplot = file.boxplot(figsize=(5, 5))
# file.boxplot(by=['species'], figsize=(10, 10))

#iris_setosa - yellow, iris_versicolor - red, iris_virginica - blue
iris_setosa = file.loc[file['species']=='Iris-setosa']
iris_setosa_plot = iris_setosa.boxplot(patch_artist=True, boxprops=dict(facecolor='yellow'), return_type='axes')

iris_versicolor = file.loc[file['species']=='Iris-versicolor']
iris_versicolor_plot = iris_versicolor.boxplot(patch_artist=True, boxprops=dict(facecolor='red'), ax=iris_setosa_plot, return_type='axes')

iris_virginica = file.loc[file['species']=='Iris-virginica']
iris_virginica.boxplot(patch_artist=True, boxprops=dict(facecolor='blue'), ax=iris_versicolor_plot, figsize=(10, 10))



