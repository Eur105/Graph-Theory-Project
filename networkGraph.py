# Import necessary modules
from sage.graphs.graph import Graph
from sage.graphs.generators.random import RandomBarabasiAlbert

# Create a network graph
n = 15  # Ensure n > 10
m = 3   # Adjust the number of edges as needed
G = RandomBarabasiAlbert(n, m)

# Display the graph
G.show()
