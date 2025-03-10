import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to create a connected random bipartite graph
def connected_bipartite_graph(num_vertices_set1, num_vertices_set2, num_edges):
    while True:
        g = nx.bipartite.gnmk_random_graph(num_vertices_set1, num_vertices_set2, num_edges)
        if nx.is_connected(g):
            return g

# Function to plot the bipartite graph with different colors for each part
def plot_bipartite_graph(graph, set1_color, set2_color):
    pos = nx.spring_layout(graph)
    set1_nodes = {n for n, d in graph.nodes(data=True) if d['bipartite'] == 0}
    set2_nodes = set(graph) - set1_nodes

    nx.draw(graph, pos, nodelist=set1_nodes, node_color=set1_color, with_labels=True, font_weight='bold', node_size=700)
    nx.draw(graph, pos, nodelist=set2_nodes, node_color=set2_color, with_labels=True, font_weight='bold', node_size=700)
    plt.show()

# Enter the number of vertices in each set and edges
n_set1 = 4
n_set2 = 4
m = 8
# Check if the entered values are valid
if n_set1 < 1 or n_set2 < 1 or m < 0:
    print("Invalid input. Please enter valid numbers for vertices and edges.")
else:
    # Create a connected random bipartite graph
    bipartite_graph = connected_bipartite_graph(n_set1, n_set2, m)

    # Select two colors for the sets
    color_set1 = 'blue'
    color_set2 = 'red'

    # Plot the bipartite graph
    plot_bipartite_graph(bipartite_graph, color_set1, color_set2)
