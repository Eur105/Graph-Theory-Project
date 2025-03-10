# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

# Create a random graph
n = 15  # Ensure n > 10
G = nx.gnp_random_graph(n, 0.3)

# Display the graph
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

# Perform graph coloring
coloring = nx.coloring.greedy_color(G, strategy="largest_first")

# Display the coloring
print("Graph Coloring:")
print(coloring)
