import sys

ROUTERS = 6 #TOTAL NUMBER OF ROUTERS

NETWORK = [
            [0,1,0,0,0,1] , # DISTANCE FROM A TO OTHER NODES 
            [1,0,1,0,3,3],  # DISTANCE FROM B TO OTHER NODES 
            [0,1,0,1,1,0],  # DISTANCE FROM C TO OTHER NODES 
            [0,0,1,0,0,0],  # DISTANCE FROM D TO OTHER NODES 
            [0,3,1,0,0,2],  # DISTANCE FROM E TO OTHER NODES 
            [1,3,0,0,2,0]   # DISTANCE FROM F TO OTHER NODES 
        ]

class Graph():  
    def __init__(self, routers): 
        self.routers = routers
        self.network = []
        self.distance = [sys.maxsize] * self.routers
        self.nextHop = [0 for _ in range(routers)]
       
    def display(self):
        print("Router\t\t Distance \t Next Hop")   #print Routing table for all 6 routers A to E 
        for router in range(self.routers):
            print(router+1, "\t\t\t", self.distance[router], "\t\t\t", self.nextHop[router]+1)
           
    def minimum_Distance(self, distance, visited) : #To find the minimum distance 
        min = sys.maxsize
        for x in range(self.routers):
            if distance[x] < min and visited[x] == False:
                min = distance[x]
                minIndex = x
        return minIndex
    
    def dijikstra_Algorithm(self, src): #using dijikstra algorithm
        self.distance = [sys.maxsize] * self.routers
        self.distance[src] = 0
        self.nextHop[src] = src
        visited = [False] * self.routers
        
        for i in range(self.routers):
            index = self.minimum_Distance(self.distance, visited)
            visited[index] = True
            
            for j in range(self.routers):
                if self.network[index][j] > 0 and visited[j] == False and self.distance[j] > self.distance[index] + self.network[index][j]:
                    self.distance[j] = self.distance[index] + self.network[index][j]
                    if self.distance[index] == 0:
                        self.nextHop[j] = j
                    else:
                        hop = index
                        temp = src
                        while(True):
                            temp = self.nextHop[hop]
                            if temp != hop:
                                hop = temp
                            else:
                                self.nextHop[j] = hop
                                break

z = Graph(ROUTERS)
z.network = NETWORK

print("1.a")
for i in range(ROUTERS):
    print("\nRouting table of router ",i+1, ":\n" )
    z.dijikstra_Algorithm(i)
    z.display()
    

print("\n 1.c \n")   
print("NODE A  : 1")
print("NODE B  : 2")
print("NODE C  : 3")
print("NODE D  : 4")
print("NODE E  : 5")
print("NODE F  : 6")
source = int(input("Enter source node (starting node ) : "))
destination = int(input("Enter destination node (ending node) : "))
z.dijikstra_Algorithm(source-1)
print("The shortest distance from node",source,"to node", destination,"is", z.distance[destination-1]) 
print("\n")


print("1.b")  
source = 1
destination = 4
z.dijikstra_Algorithm(source-1)
print("The shortest distance from A to D is ", z.distance[destination-1]) 

print("\n")
print("1.b")  
source = 2
destination = 5
z.dijikstra_Algorithm(source-1)
print("The shortest distance from B to E is ", z.distance[destination-1]) 




