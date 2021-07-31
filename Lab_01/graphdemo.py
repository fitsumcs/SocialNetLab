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

#View Graph Information 
print("####### ############################### #######")
print("Generic Information about the Graph via Method", "\n")
print(nx.info(G) , '\n')
print("####### ############################### #######", '\n')

 
