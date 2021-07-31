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

 
