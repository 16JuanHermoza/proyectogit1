import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#matriz de adyacencia
AD = np.array([[0,4,0,0,0,0],
               [4,0,1,2,0,0],
               [0,1,0,7,9,0],
               [0,2,7,0,0,0],
               [0,0,9,0,0,3],
               [0,0,0,0,3,0]])
# crar grafo a base de la matriz
G =nx.from_numpy_array(AD)
valores = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
grados = dict(G.degree())
print("Grado de cada nodo:", grados)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
for node, (x, y) in pos.items():
    plt.text(x, y + 0.1, f"Grado: {grados[node]}", fontsize=12, ha='center')
plt.text(-1.68, 1.109, "Grafito", fontsize=15, fontweight='bold')
plt.show()
