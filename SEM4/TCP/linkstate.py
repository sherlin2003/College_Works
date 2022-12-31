import sys
ROUTERS = 9
NETWORK = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];

class Graph():  
    def __init__(self, routers):
        self.routers = routers
        self.network = [[0 for _ in range(routers)] for _ in range(routers)]
        self.distance = [sys.maxsize] * self.routers
        
    def display(self):
        print("Router\tDistance")
        for router in range(self.routers):
            print(router, "\t\t", self.distance[router])
            
    def minDistance(self, distance, graph):       
        min = sys.maxsize
        for i in range(self.routers):
            if distance[i] < min and graph[i] == False:
                min = distance[i]
                minIndex = i
        return minIndex
    
    def dijikstra(self, src):
        self.distance = [sys.maxsize] * self.routers
        self.distance[src] = 0
        graph = [False] * self.routers
        
        for i in range(self.routers):
             index = self.minDistance(self.distance, graph)
             graph[index] = True
             
             for j in range(self.routers):
                 if self.network[index][j] > 0 and graph[j] == False and self.distance[j] > self.distance[index] + self.network[index][j]:
                     self.distance[j] = self.distance[index] + self.network[index][j]
                     
g = Graph(ROUTERS)
g.network = NETWORK

for i in range(ROUTERS):
    print("\nNETWORK ", i+1, ":\n")
    g.dijikstra(i)
    g.display()