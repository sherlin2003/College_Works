import matplotlib.pyplot as py
import pandas as pd

data = pd.read_csv("linear.csv")
print(data)

# x= data['X']
# y=data['Y']

eta =0.088
bold=[0,0]
bnew=[0,0]
B0=[]
B1=[]
sse1=[]
sse2=0
n=len(data['X'])
while True :
    grad =[0,0]
    for i in range (n):
        ycap = bold[0] + bold[1] * ((data['X'])[i])
        grad[0] = grad[0]+((data['Y'])[i]-ycap)
        grad[1]= grad[0]+ ((data['Y'])[i]-ycap) *((data['X'])[i])
        sse2 =((data['Y'])-ycap)**2
        
    sse1.append(sse2)
    B0.append(bold[0])
    B1.append(bold[1])
    
    bnew[0]= bold[0] + eta * grad[0]
    bnew[1]= bold[1] + eta * grad[1]
    
    if (bold[0]==bnew[0] and bold[1]==bnew[1]):
        break
    else:
        bold[0] = bnew[0]
        bold[1] = bnew[1]
    