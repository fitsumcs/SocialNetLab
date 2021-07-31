# Import the Libs 
import networkx as nx
import matplotlib.pyplot as plt


# Part two : This part more focus on the Drawing part of  the Graph 

G = nx.Graph()                # Create a Graph  Undirected Simple Graph 

#Addind Nodes 
G.add_node("a")           # adding a single Node 
G.add_nodes_from(["b","c", "d","e"])      # adding multiple nodes 

#Addind Edges
G.add_edge("a","b")              # adding a single Edge
edge = ("b", "c")                # adding via tuple 
G.add_edge(*edge) 
G.add_edges_from([("c","e"), ("d","e"),("a","e")])        #adding multiple edges


# Draw the Graph with label and font  [Option One ]
#nx.draw(G , with_labels=True, font_weight='bold')

#Option for drawing the graph
options = {
    'node_color' : 'red', 
    'node_size' : 100,
    'edge_color' : 'blue',
    'with_labels' : True , 
    'font_weight' : 'bold'
    }

# Draw with options 
#nx.draw(G,**options)

# Draw Circular 
nx.draw_circular(G, **options) 

# other types  [You can only one type at a time ]

#nx. draw_random(G, **options)        Draw the graph G with a random layout.
#nx.draw_random(G, **options)         Draw the graph G with a random layout.
#nx.draw_spectral(G, **options)       Draw the graph G with a spectral layout.
#nx.draw_spring(G, **options)         Draw the graph G with a spring layout.
#nx.draw_shell(G, **options)          Draw the graph G with a shell layout.




# Add Title 
plt.title('Graph Demo', size=15)

# Plot the Graph
plt.show()

