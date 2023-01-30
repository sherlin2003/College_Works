import networkx as nx

def DFS(graph, index, target):
    if(visited[index] == False):
        visited[index] = True
    
    print(index)
    route.append(index)
    if(target == index):
        return True
    
    for i in graph[index]:
        if(visited[i] == False):
            if DFS(graph, i, target):
                return True
    return False

def findPaths(route):
    paths = []
    for i in range(1, len(route)):
        path = [route[i-1], route[i]]
        paths.append(path)
    return paths

graph = {
    
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
    
    }

print("Graph: ", graph)

visited = [False for _ in range(len(graph))]

start = 2
target = 3

flag = False

route = []

for i in range(len(graph)):
    if(visited[i] == False):
        flag = DFS(graph, start, target)
    if flag:
        break

paths = findPaths(route)

G = nx.Graph()

for x in graph:
    G.add_node(x)
    
for x in graph:
    for y in graph[x]:
        G.add_edge(x, y)

pos = nx.spring_layout(G)

nx.draw(G, pos)

nx.draw_networkx_edges(G, pos, edgelist = paths, width = 3, edge_color='r')


