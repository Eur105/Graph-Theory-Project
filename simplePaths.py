# Import necessary modules
from sage.graphs.digraph_generators import digraphs
from sage.graphs.graph_generators import graphs

# Create a directed graph
n = 6  # Ensure n > 5
G = digraphs.RandomDirectedGNP(n, 0.3)

# Display the graph
G.show()

# Find all simple paths with max length 2
max_length = 2
simple_paths = []
for v in G.vertices():
    for u in G.neighbors_out(v):
        for w in G.neighbors_out(u):
            if w != v and G.has_edge(v, u) and G.has_edge(u, w):
                simple_paths.append([v, u, w])

# Display the simple paths
print("All simple paths with max length 2:")
print(simple_paths)
