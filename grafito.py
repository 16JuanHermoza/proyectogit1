import networkx as nx
import matplotlib.pyplot as plt

# crar grafo vacio 
G = nx.Graph()
#agregar nodos 
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("5")
G.add_node("2")
#agregar aristas
G.add_edge("A","B", peso=3)
G.add_edge("B","C", peso=1)
G.add_edge("C","5", peso=5)
G.add_edge("B","5", peso=3)
#Vizualizar grafo
GUI = nx.spectral_layout(G)
nx.draw(G, GUI, with_labels=True)
labels = nx.get_edge_attributes(G, "peso")
nx.draw_networkx_edge_labels(G, GUI, edge_labels=labels)
plt.show()
