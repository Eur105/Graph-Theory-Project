# Import necessary modules
from sage.graphs.graph_generators import graphs
import networkx as nx

# Create a graph
n = 12  # Ensure n > 10
G = graphs.RandomGNP(n, 0.3)

# Display the graph
G.show()

# Convert Sage graph to NetworkX graph
G_nx = G.networkx_graph()

# Find a maximum cardinality matching using NetworkX
matching = nx.algorithms.matching.max_weight_matching(G_nx)

# Display the matching edges
print("Maximum Cardinality Matching:")
print(matching)
