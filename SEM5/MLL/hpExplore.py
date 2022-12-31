import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("E:\\SEM5\\MLL\\data.csv")
# print(data.describe())

def plotScatter(X,Y):
    print(X + '  vs  ' + Y)
    
    plt.scatter(data[X],data[Y])
    n = len(data[X])
    sumX = np.sum(data[X])
    sumX2 = np.sum(data[X]*data[X])
    xtx = [[n, sumX],[sumX, sumX2]]
    xtxinv = np.linalg.inv(xtx)
    sumY = np.sum(data[Y])
    sumXY = np.sum(data[X]*data[Y])
    xty = [sumY, sumXY]
    b = np.matmul(xtxinv,xty)
    print(b)
    x = np.linspace(0,10000)
    y = b[0] + b[1]*x;
    plt.plot(x,y,'-r')
    plt.xlabel(X)
    plt.ylabel(Y)
    plt.show()
    
    ynew = []
    for i in data[X]:
        yval = b[0] + b[1]*i
        ynew.append(yval)
        
    e = []
    k = 0
    for i in data[Y]:
        erval = i-ynew[k]
        e.append(erval*erval)
        k+=1     
    print('SSE = ', sum(e))
    
    mean = np.mean(data[Y])
    s = 0
    for i in data[Y]:
        s += i-mean
    print('SST = ', s*s)

    e = []
    k = 0
    for i in data[Y]:
        erval = ynew[k]-mean
        e.append(erval*erval)
        k+=1    
    print('SSR = ', sum(e))
    print("\n\n")

plotScatter('bedrooms','price')
plotScatter('bathrooms','price')
plotScatter('sqft_living','price')
plotScatter('sqft_lot','price')
plotScatter('floors','price')
plotScatter('waterfront','price')
plotScatter('view','price')
plotScatter('condition','price')
plotScatter('sqft_above','price')
plotScatter('sqft_basement','price')
plotScatter('yr_built','price')
plotScatter('yr_renovated','price')


# # bedrooms vs price
# plt.scatter(data['bedrooms'],data['price'])
# n = len(data['bedrooms'])
# sumdata[X] = np.sum(data['bedrooms'])
# sumdata[X]2 = np.sum(data['bedrooms']*data['bedrooms'])
# data[X]tx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['bedrooms']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("Bedrooms vs Price")
# print(b)
# x = np.linspace(0,5)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("bedroom")
# plt.ylabel("price")
# plt.show()

# # bathrooms vs price
# plt.scatter(data['bathrooms'],data['price'])
# n = len(data['bathrooms'])
# sumX = np.sum(data['bathrooms'])
# sumX2 = np.sum(data['bathrooms']*data['bathrooms'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['bathrooms']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("Bathrooms vs Price")
# print(b)
# x = np.linspace(0,5)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("bathrooms")
# plt.ylabel("price")
# plt.show()


# # sqft_living vs price
# plt.scatter(data['sqft_living'],data['price'])
# n = len(data['sqft_living'])
# sumX = np.sum(data['sqft_living'])
# sumX2 = np.sum(data['sqft_living']*data['sqft_living'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['sqft_living']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("Sqft_living vs Price")
# print(b)
# x = np.linspace(0,10000)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("sqft_living")
# plt.ylabel("price")
# plt.show()


# # sqft_lot vs price
# plt.scatter(data['sqft_lot'],data['price'])
# n = len(data['sqft_lot'])
# sumX = np.sum(data['sqft_lot'])
# sumX2 = np.sum(data['sqft_lot']*data['sqft_lot'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['sqft_lot']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("Sqft_lot vs Price")
# print(b)
# x = np.linspace(0,1000000)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("sqft_lot")
# plt.ylabel("price")
# plt.show()


# # floors vs price
# plt.scatter(data['floors'],data['price'])
# n = len(data['floors'])
# sumX = np.sum(data['floors'])
# sumX2 = np.sum(data['floors']*data['floors'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['floors']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("Floors vs Price")
# print(b)
# x = np.linspace(0,4)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("floors")
# plt.ylabel("price")
# plt.show()


# # waterfront vs price
# plt.scatter(data['waterfront'],data['price'])
# n = len(data['waterfront'])
# sumX = np.sum(data['waterfront'])
# sumX2 = np.sum(data['waterfront']*data['waterfront'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['waterfront']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("waterfront vs Price")
# print(b)
# x = np.linspace(0,2)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("waterfront")
# plt.ylabel("price")
# plt.show()


# # view vs price
# plt.scatter(data['view'],data['price'])
# n = len(data['view'])
# sumX = np.sum(data['view'])
# sumX2 = np.sum(data['view']*data['view'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['view']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("view vs Price")
# print(b)
# x = np.linspace(0,5)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("view")
# plt.ylabel("price")
# plt.show()


# # condition vs price
# plt.scatter(data['condition'],data['price'])
# n = len(data['condition'])
# sumX = np.sum(data['condition'])
# sumX2 = np.sum(data['condition']*data['condition'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['condition']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("condition vs Price")
# print(b)
# x = np.linspace(0,5)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("condition")
# plt.ylabel("price")
# plt.show()


# # sqft_above vs price
# plt.scatter(data['sqft_above'],data['price'])
# n = len(data['sqft_above'])
# sumX = np.sum(data['sqft_above'])
# sumX2 = np.sum(data['sqft_above']*data['sqft_above'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['sqft_above']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("sqft_above vs Price")
# print(b)
# x = np.linspace(0,10000)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("sqft_above")
# plt.ylabel("price")
# plt.show()


# # sqft_basement vs price
# plt.scatter(data['sqft_basement'],data['price'])
# n = len(data['sqft_basement'])
# sumX = np.sum(data['sqft_basement'])
# sumX2 = np.sum(data['sqft_basement']*data['sqft_basement'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['sqft_basement']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("sqft_basement vs Price")
# print(b)
# x = np.linspace(0,5000)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("sqft_basement")
# plt.ylabel("price")
# plt.show()


# # yr_built vs price
# plt.scatter(data['yr_built'],data['price'])
# n = len(data['yr_built'])
# sumX = np.sum(data['yr_built'])
# sumX2 = np.sum(data['yr_built']*data['yr_built'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['yr_built']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("yr_built vs Price")
# print(b)
# x = np.linspace(1900,2020)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("yr_built")
# plt.ylabel("price")
# plt.show()

# # yr_renovated vs price
# plt.scatter(data['yr_renovated'],data['price'])
# n = len(data['yr_renovated'])
# sumX = np.sum(data['yr_renovated'])
# sumX2 = np.sum(data['yr_renovated']*data['yr_renovated'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['yr_renovated']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("yr_renovated vs Price")
# print(b)
# x = np.linspace(0,2020)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("yr_renovated")
# plt.ylabel("price")
# plt.show()


# # street vs price
# plt.scatter(data['street'],data['price'])
# n = len(data['street'])
# sumX = np.sum(data['street'])
# sumX2 = np.sum(data['street']*data['street'])
# xtx = [[n, sumX],[sumX, sumX2]]
# xtxinv = np.linalg.inv(xtx)
# sumY = np.sum(data['price'])
# sumXY = np.sum(data['street']*data['price'])
# xty = [sumY, sumXY]
# b = np.matmul(xtxinv,xty)
# print("street vs Price")
# print(b)
# x = np.linspace(0,2020)
# y = b[0] + b[1]*x;
# plt.plot(x,y,'-r')
# plt.xlabel("street")
# plt.ylabel("price")
# plt.show()