# Import the Libs 
import networkx as nx
import matplotlib.pyplot as plt


#Create a Graph 

G = nx.Graph()                #Undirected Simple Graph 
G1 = nx.DiGraph()             #Directed Simple Graph 


#View Graph Information 
print("####### ############################### #######")
print("Generic Information about the Graph", "\n")
print(G , '\n')
print("####### ############################### #######", '\n')

#View Graph Information via method 
print("####### ############################### #######")
print("Generic Information about the Graph via Method", "\n")
print(nx.info(G) , '\n')
print("####### ############################### #######", '\n')

#View Graph nodes and edge information
print("####### ############################### #######")
print("Generic Information about the Graph nodes and edges ", "\n")
print("Graph Nodes : ")
print(G.nodes())
print("Graph Edges : ")
print(G.edges())
print("Graph Node Type : ")
print(type(G.nodes()))
print("Graph Edge Type : ")
print(type(G.edges()))
print("####### ############################### #######", '\n')


#Addind Nodes 
print("####### ############################### #######")
print("Addins Nodes and Viewing the info ", "\n")

# adding a single Node 

G.add_node("a")

# adding multiple nodes 
G.add_nodes_from(["b","c", "d","e"])

print("Graph Nodes : ")
print(G.nodes())
print("####### ############################### #######", '\n')

#Addind Edges
print("####### ############################### #######")
print("Addins Nodes and Viewing the info ", "\n")

# adding a single Edge

G.add_edge("a","b")

# adding via tuple 
edge = ("b", "c")
G.add_edge(*edge)

#adding multiple edges 
G.add_edges_from([("c","e"), ("d","e"),("a","e")])

print("Graph Edges : ")
print(G.edges())
print("####### ############################### #######", '\n')
 
