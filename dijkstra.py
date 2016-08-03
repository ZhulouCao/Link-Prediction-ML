import networkx as nx
import numpy as np
A = np.array([[0, 1,5, 0],
              [1, 0, 0, 1],
              [5, 0, 0, 1],
              [0, 1, 1, 0]])
G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
print(nx.dijkstra_path(G, 0, 1))
print(nx.dijkstra_path_length(G, 0, 3))
print(nx.dijkstra_path_length(G, 1, 0))
print(nx.shortest_path(G, 0, 1))	
print(nx.shortest_path(G, 0, 3))
print(nx.shortest_path(G, 1, 0))
