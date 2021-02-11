from Graph import UnweightedGraph

"""
The function "explore" explores all the vertices 
that are reachable from a given vertex in a graph
"""

n = 5
g = UnweightedGraph(n)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)

visited = [0]*n

def explore(g,v):
    for j in g.neighbors(v):
        if not visited[j]:
            visited[j] = 1
            print(visited)
            explore(g, j)




visited[0] = 1
explore(g, 0)
print(visited)
