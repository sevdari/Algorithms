from sqMatrix import SqMatrix
import math
class UnweightedGraph:
    """
    A graph class that uses an adjacency matrix as its internal
    representation. The graph is undirected (i.e. the matrix
    is symmetric) and unweighted (the matrix elements are only 0 or 1).
    Each node in the graph is labeled by an integer between 0 and n-1.
    """
    def __init__(self, n):
        """
        The constructor takes the number of nodes as argument.
        The graph is initially empty (no edges).
        """
        self.adj = SqMatrix(n) # creates an adj. matrix filled with zeros

    def __repr__(self):
        return f"{type(self).__name__} with adj. matrix:\n{self.adj}"

    def __eq__(self, other):
        if isinstance(other, UnweightedGraph):
            return self.adj == other.adj
        return NotImplemented

    def get_n(self):
        """
        Return the number of nodes in the graph"
        """
        return self.adj.shape()[0]

    def add_edge(self, i, j):
        """
        Adds an edge between nodes i and j.
        If the edge already exists, do nothing.
        """
        self.adj[i,j] = 1
        self.adj[j,i] = 1

    def del_edge(self, i, j):
        """
        Deletes an edge between nodes i and j.
        If the edge doesn't exist, do nothing.
        """
        self.adj[i, j] = 0
        self.adj[j, i] = 0

    def neighbors(self, i):
        """
        Returns a set of the nodes connected to the given one.
        """
        n = self.get_n()
        return {j for j in range(n) if self.adj[i, j] == 1}
