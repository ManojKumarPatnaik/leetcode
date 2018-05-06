# Python program for finding min-cut in the given graph
# Complexity : (E*(V^3))
# Total augmenting path = VE and BFS with adj matrix takes :V^2 times
 
from collections import defaultdict
 
# This class represents a directed graph using adjacency matrix representation
class Graph:
 
    def __init__(self,graph):
        self.graph = graph # residual graph
        self.org_graph = [i[:] for i in graph]
        self. ROW = len(graph)
        self.COL = len(graph[0])
 
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)
 
        # Create a queue for BFS
        queue=[]
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            #Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False
 
 
    # Returns tne min-cut of the given graph
    def minCut(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        # print the edges which initially had weights
        # but now have 0 weight
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0:
                    print str(i) + " - " + str(j)

# Create a graph given in the above diagram
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
graph = [
        [87, 78, 16, 94, 36, 87, 93, 50, 22, 63, 28, 91, 60, 64, 27, 41, 27, 73, 37, 12, 69, 68, 30, 83, 31, 63, 24, 68, 36, 30, 3, 23, 59, 70],
        [68, 94, 57, 12, 43, 30, 74, 22, 20, 85, 38, 99, 25, 16, 71, 14, 27, 92, 81, 57, 74, 63, 71, 97, 82, 6, 26, 85, 28, 37, 6, 47, 30, 14],
        [58, 25, 96, 83, 46, 15, 68, 35, 65, 44, 51, 88, 9, 77, 79, 89, 85, 4, 52, 55, 100, 33, 61, 77, 69, 40, 13, 27, 87, 95, 40, 96, 71, 35],
        [79, 68, 2, 98, 3, 18, 93, 53, 57, 2, 81, 87, 42, 66, 90, 45, 20, 41, 30, 32, 18, 98, 72, 82, 76, 10, 28, 68, 57, 98, 54, 87, 66, 7],
        [84, 20, 25, 29, 72, 33, 30, 4, 20, 71, 69, 9, 16, 41, 50, 97, 24, 19, 46, 47, 52, 22, 56, 80, 89, 65, 29, 42, 51, 94, 1, 35, 65, 25],
        [15, 88, 57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22, 59, 96, 30, 38, 36, 94, 19, 29, 44, 12, 29, 30, 77, 5, 44, 64, 14],
        [39, 7, 41, 5, 19, 29, 89, 70, 18, 18, 97, 25, 44, 71, 84, 91, 100, 73, 26, 45, 91, 6, 40, 55, 87, 70, 83, 43, 65, 98, 8, 56, 5, 49],
        [12, 23, 29, 100, 44, 47, 69, 41, 23, 12, 11, 6, 2, 62, 31, 79, 6, 21, 37, 45, 27, 23, 66, 9, 17, 83, 59, 25, 38, 63, 25, 1, 37, 53],
        [100, 80, 51, 69, 72, 74, 32, 82, 31, 34, 95, 61, 64, 100, 82, 100, 97, 60, 74, 14, 69, 91, 96, 27, 67, 85, 41, 91, 85, 77, 43, 37, 8, 46],
        [57, 80, 19, 88, 13, 49, 73, 60, 10, 37, 11, 43, 88, 7, 2, 14, 73, 22, 56, 20, 100, 22, 5, 40, 12, 41, 68, 6, 29, 28, 51, 85, 59, 21],
        [25, 23, 70, 97, 82, 31, 85, 93, 73, 73, 51, 26, 86, 23, 100, 41, 43, 99, 14, 99, 91, 25, 91, 10, 82, 20, 37, 33, 56, 95, 5, 80, 70, 74],
        [77, 51, 56, 61, 43, 80, 85, 94, 6, 22, 68, 5, 14, 62, 55, 27, 60, 45, 3, 3, 7, 85, 22, 43, 69, 29, 90, 73, 9, 59, 99, 37, 9, 54],
        [49, 4, 34, 34, 49, 91, 55, 68, 47, 69, 30, 1, 47, 89, 98, 50, 91, 4, 34, 64, 98, 54, 93, 87, 26, 53, 97, 76, 89, 58, 30, 37, 61, 15],
        [22, 61, 5, 29, 28, 51, 49, 57, 3, 95, 98, 100, 44, 40, 3, 29, 4, 1, 82, 48, 39, 60, 52, 36, 35, 40, 93, 16, 28, 5, 30, 50, 65, 86],
        [30, 44, 36, 78, 1, 39, 72, 50, 90, 68, 89, 93, 96, 44, 45, 30, 91, 83, 41, 42, 70, 27, 33, 62, 43, 61, 18, 24, 62, 82, 10, 91, 26, 97],
        [68, 78, 35, 91, 27, 25, 58, 15, 69, 6, 59, 13, 87, 1, 47, 27, 95, 17, 53, 79, 30, 47, 91, 48, 71, 52, 81, 32, 94, 58, 28, 13, 87, 15],
        [56, 13, 91, 13, 80, 11, 70, 90, 75, 56, 42, 21, 34, 88, 89, 39, 67, 71, 85, 57, 18, 7, 61, 50, 38, 6, 60, 18, 19, 46, 84, 74, 59, 74],
        [38, 90, 84, 8, 79, 58, 15, 72, 30, 1, 60, 19, 39, 26, 89, 75, 34, 58, 82, 94, 59, 71, 100, 18, 40, 70, 64, 23, 95, 74, 48, 32, 63, 83],
        [91, 93, 92, 58, 16, 22, 58, 75, 92, 48, 52, 32, 22, 38, 41, 55, 31, 99, 26, 82, 17, 17, 3, 32, 40, 97, 5, 39, 81, 19, 22, 71, 63, 13],
        [80, 78, 86, 37, 5, 77, 84, 8, 60, 58, 45, 100, 12, 28, 51, 37, 61, 19, 6, 64, 50, 45, 12, 6, 35, 92, 76, 56, 15, 90, 69, 94, 19, 6],
        [83, 23, 83, 18, 31, 94, 75, 27, 94, 87, 54, 44, 75, 15, 14, 80, 78, 63, 76, 89, 20, 11, 33, 95, 18, 47, 36, 38, 92, 54, 44, 74, 29, 26],
        [92, 11, 19, 18, 37, 64, 56, 91, 59, 31, 5, 72, 62, 34, 86, 90, 74, 5, 52, 6, 51, 69, 4, 86, 7, 96, 40, 50, 21, 68, 27, 64, 78, 97],
        [82, 66, 61, 37, 56, 71, 19, 12, 43, 33, 97, 80, 22, 71, 85, 73, 28, 35, 41, 84, 73, 99, 31, 64, 48, 51, 31, 74, 15, 60, 23, 48, 25, 83],
        [36, 33, 5, 55, 44, 99, 87, 41, 79, 60, 63, 63, 84, 42, 49, 24, 25, 73, 23, 55, 36, 22, 58, 66, 48, 72, 77, 70, 19, 2, 4, 54, 34, 8],
        [60, 29, 7, 98, 21, 85, 9, 35, 99, 92, 77, 99, 16, 53, 72, 90, 60, 7, 11, 17, 25, 10, 40, 1, 79, 10, 54, 82, 15, 39, 90, 27, 68, 48],
        [24, 88, 32, 33, 23, 82, 76, 51, 80, 91, 55, 51, 32, 14, 58, 95, 82, 82, 4, 21, 34, 83, 82, 88, 16, 97, 26, 5, 23, 93, 52, 98, 33, 35],
        [82, 7, 16, 58, 9, 96, 100, 63, 98, 84, 77, 55, 78, 10, 88, 33, 83, 22, 67, 64, 61, 83, 12, 86, 87, 86, 31, 91, 84, 15, 77, 17, 21, 93],
        [26, 29, 40, 26, 91, 37, 61, 19, 44, 38, 29, 83, 22, 11, 56, 89, 26, 16, 71, 38, 54, 9, 23, 84, 51, 58, 98, 28, 27, 70, 72, 52, 50, 11],
        [29, 40, 99, 89, 11, 94, 78, 91, 77, 100, 53, 32, 88, 78, 100, 58, 67, 53, 18, 42, 36, 69, 99, 85, 96, 77, 6, 67, 29, 55, 29, 9, 94, 79],
        [98, 56, 73, 75, 46, 1, 26, 98, 84, 13, 28, 83, 22, 94, 35, 40, 35, 22, 60, 86, 58, 55, 62, 63, 73, 42, 17, 53, 51, 63, 83, 100, 18, 55],
        [74, 16, 7, 52, 65, 91, 64, 92, 73, 38, 38, 60, 29, 72, 81, 88, 57, 91, 42, 71, 53, 66, 12, 70, 18, 62, 84, 52, 13, 1, 7, 39, 68, 65],
        [90, 33, 55, 5, 76, 80, 42, 13, 39, 70, 37, 71, 57, 45, 61, 50, 15, 66, 15, 27, 87, 84, 40, 70, 36, 53, 22, 94, 91, 90, 10, 32, 74, 65],
        [36, 49, 96, 78, 14, 34, 99, 50, 56, 56, 94, 69, 57, 61, 34, 24, 87, 72, 59, 78, 41, 46, 82, 62, 91, 24, 51, 1, 55, 76, 65, 43, 25, 60],
        [20, 90, 45, 70, 39, 52, 77, 84, 20, 34, 44, 5, 57, 82, 76, 67, 12, 68, 13, 93, 30, 3, 69, 32, 3, 75, 8, 19, 17, 84, 78, 88, 73, 74],
        
    ]
 
show_graph(graph)
g = Graph(graph)
 
source = 24; sink = 33
 
g.minCut(source, sink)
 
# This code is contributed by Neelam Yadav
