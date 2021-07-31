# Import the Libs 
import networkx as nx
import matplotlib.pyplot as plt


# Part two : This part more focus on the Analysing the Graph 

G = nx.Graph()                # Create a Graph  Undirected Simple Graph 

#Addind Nodes 
G.add_node("a")           # adding a single Node 
G.add_nodes_from(["b","c", "d","e"])      # adding multiple nodes 

#Addind Edges
G.add_edge("a","b")              # adding a single Edge
edge = ("b", "c")                # adding via tuple 
G.add_edge(*edge) 
G.add_edges_from([("c","e"), ("d","e"),("a","e")])        #adding multiple edges




