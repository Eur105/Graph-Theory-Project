import networkx as nx
import matplotlib.pyplot as plt

# Function to create a complete graph with given vertices
def complete_graph_with_names(vertices):
    g = nx.complete_graph(vertices)
    return g

# Function to plot the complete graph with vertex names
def plot_complete_graph(graph):
    pos = nx.spring_layout(graph)  
    # Layout algorithm, you can use other algorithms as well
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700)
    plt.show()


# Enter manually the number of vertices you want to enter:
n = 11
if n <= 10:
    print("Invalid Input")
else:
    # Enter the vertices manually
    vertices = []
    for i in range(n):
        vertices.append(chr(ord('A') + i))

    # Check if the number of vertices matches the specified number
    if len(vertices) != n:
        print("Invalid number of vertices")
    else:
        complete_graph = complete_graph_with_names(vertices)
        plot_complete_graph(complete_graph)
