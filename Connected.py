from Graph import UnweightedGraph

"""
The function "explore" explores all the vertices 
that are reachable from a given vertex in a graph
The function "connected" determines which how many
subgraphs there are in the function
"""

n = 5
g = UnweightedGraph(n)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 3)
counter = 0
cc = [0] * n
visited = [0] * n

def explore(g, v):
    global counter
    visited[v] = 1
    cc[v] = counter
    for j in g.neighbors(v):
        if not visited[j]:
            explore(g, j)


def connected(g):
    global counter
    for i in range(g.get_n()):
        if not visited[i]:
            counter += 1
            explore(g, i)


connected(g)

print(cc)