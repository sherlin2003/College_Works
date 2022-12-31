 
# X=[4,4.5,5,5.5,6,6.5,7]
# Y=[33,42,45,51,53,61,62]

# eta=0.0088
# Bold=[0,0]
# Bnew=[0,0]

# while(True):
#    grad=[0,0]
#    for i in range(len(X)):
#         grad[0] += ( Y[i]-( Bold[0]+Bold[1]*X[i] ) )
#         grad[1] += ((Y[i]-( Bold[0]+Bold[1]*X[i] ) )*X[i]) 
 
#    Bnew[0]= Bold[0]+eta*grad[0]
#    Bnew[1]= Bold[1]+eta*grad[1]
   
#    if(Bold[0]==Bnew[0] and Bold[1]==Bnew[1]):
#        break
#    Bold[0]=Bnew[0]
#    Bold[1]=Bnew[1]
          
        
# print(Bold)
# plt.scatter(X,Y)

     
import matplotlib.pyplot as plt
import numpy as np
print("Enter the X-values :")  #4 4.5 5 5.5 6 6.5 7
x=[float(i) for i in input().split()]

print("Enter the Y-values :") #33 42 45 51 53 61 63
y=[float(i) for i in input().split()]

eta=0.00008
bold=[0,0]
bnew=[0,0]
B0=[]
B1=[]
sse1=[]
sse2=0

while(True):
    grad=[0,0]
    
    for i in range(len(x)):
        ycap=bold[0]+bold[1]*x[i]
        grad[0]+=(y[i]-ycap)
        grad[1]+=(y[i]-ycap)*x[i]
        sse2+=(y[i]-ycap)**2
        
    sse1.append(sse2)
    B0.append(bold[0])
    B1.append(bold[1])
    bnew[0]=bold[0]+eta*(grad[0])
    bnew[1]=bold[1]+eta*(grad[1])
    
    if(bold[0]==bnew[0] and bold[1]==bnew[1]):
        break
    
    bold[0]=bnew[0]
    bold[1]=bnew[1]

print(bold)

mean=sum(y)/len(x)

sse=sst=0

print("SSE")
for i in range(len(x)):
    sse+=(y[i]-(bold[0]+bold[1]*x[i]))**2
print(sse)

print("SST")
for i in range(len(x)):
    sst+=(y[i]-mean)**2
print(sst)

print("SSR")
ssr=sst-sse
print(ssr)

print("Coefficient of determination , r2 : ")
r=ssr/sst
print(r)

plt.plot(B0,B1,sse1)
       