import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#matriz de adyacencia
AD = np.array([[0,2,4],
               [1,0,5],
               [0,4,0]])

# crar grafo a base de la matriz
G =nx.from_numpy_array(AD)
valores = {0:"A",1:"B",2:"C"}
G = nx.relabel_nodes(G, valores)
#Vizualizar grafo
GUI = nx.spectral_layout(G)
nx.draw(G, GUI, with_labels=True)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, GUI, edge_labels=labels)
plt.text(0.5, 0.5, "Grafito")
plt.show()
