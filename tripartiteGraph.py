import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to create a connected random tripartite graph
def connected_tripartite_graph(num_vertices_set1, num_vertices_set2, num_vertices_set3, num_edges):
    while True:
        g = nx.Graph()
        g.add_nodes_from(range(num_vertices_set1 + num_vertices_set2 + num_vertices_set3))
        for _ in range(num_edges):
            u = random.randint(0, num_vertices_set1 - 1)
            v = random.randint(num_vertices_set1, num_vertices_set1 + num_vertices_set2 - 1)
            w = random.randint(num_vertices_set1 + num_vertices_set2, num_vertices_set1 + num_vertices_set2 + num_vertices_set3 - 1)
            g.add_edge(u, v)
            g.add_edge(v, w)
        if nx.is_connected(g):
            return g

# Function to plot the tripartite graph with different colors for each part
def plot_tripartite_graph(graph, set1_color, set2_color, set3_color):
    pos = nx.spring_layout(graph)
    set1_nodes = {n for n, d in graph.nodes(data=True) if n < n_set1}
    set2_nodes = {n for n, d in graph.nodes(data=True) if n >= n_set1 and n < n_set1 + n_set2}
    set3_nodes = set(graph) - set1_nodes - set2_nodes

    nx.draw(graph, pos, nodelist=set1_nodes, node_color=set1_color, with_labels=True, font_weight='bold', node_size=700)
    nx.draw(graph, pos, nodelist=set2_nodes, node_color=set2_color, with_labels=True, font_weight='bold', node_size=700)
    nx.draw(graph, pos, nodelist=set3_nodes, node_color=set3_color, with_labels=True, font_weight='bold', node_size=700)
    plt.show()

# Enter the number of vertices in each set and edges
n_set1 = 4
n_set2 = 4
n_set3 = 4
m = 8

# Check if the entered values are valid
if n_set1 < 1 or n_set2 < 1 or n_set3 < 1 or m < 0:
    print("Invalid input. Please enter valid numbers for vertices and edges.")
else:
    # Create a connected random tripartite graph
    tripartite_graph = connected_tripartite_graph(n_set1, n_set2, n_set3, m)

    # Select three colors for the sets
    color_set1 = 'blue'
    color_set2 = 'red'
    color_set3 = 'green'

    # Plot the tripartite graph
    plot_tripartite_graph(tripartite_graph, color_set1, color_set2, color_set3)
