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

#View Graph Information 
print("####### ############################### #######")
print("Generic Information about the Graph", "\n")
print("Number of Nodes : ")
print("Method 1 : ", G.number_of_nodes() )
print("Method 2 : ",len(G))
print("Method 3 : ",G.order())
print("Number of Edges : ")
print(G.number_of_edges(), '\n')
print("####### ############################### #######", '\n')

#View Presense of Node and Edge 
print("####### ############################### #######")
print("View Presense of Node and Edge ", "\n")
print("Presence of Nodes : ")
print("Dose Node a Exist ?  : ", G.has_node("a") )
print("Dose Node 1 Exist ?  : ", G.has_node(1) )
print("Presence of Edges : ")
print("Is there edge b/n a and b ?  : ", G.has_edge("a", "b") )
print("Is there edge b/n d and c ?  : ", G.has_edge("d", "c") )
print("####### ############################### #######", '\n')

#View Neighbors [The method return need to be converted to list]
print("####### ############################### #######")
print("View Neighbors of Nodes", "\n")
print("Neighbors of A: ")
print(list(G.neighbors("a")))
print("####### ############################### #######", '\n')

#View Node Degree
print("####### ############################### #######")
print("View Degree of Nodes", "\n")
print("Degree of A: ")
print(G.degree("a"))
print("Degree of b, c: ")
print(G.degree(["b","c"]))
print("Degree of each node ")
print(G.degree())


print("####### ############################### #######", '\n')

