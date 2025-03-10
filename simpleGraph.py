import networkx as nx
import matplotlib.pyplot as plt

# Function to create a connected random graph
def connected_random_graph(num_vertices, num_edges):
    while True:
        g = nx.gnm_random_graph(num_vertices, num_edges)
        if nx.is_connected(g):
            return g

# Function to plot the graph with vertex names
def plot_graph(graph):
    pos = nx.spring_layout(graph)
    # Layout algorithm, you can use other algorithms as well
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700)
    plt.show()

# Enter the number of vertices and edges
n= 10
m = 12
# Check if the entered values are valid
if n < 1 or m < 0:
    print("Invalid input. Please enter a valid number of vertices (1 to 26) and non-negative edges.")
else:
    # Create a connected random graph
    connected_random_graph = connected_random_graph(n, m)
    plot_graph(connected_random_graph)
