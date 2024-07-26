import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Matriz de adyacencia
AD = np.array([[0, 4, 0, 0, 0, 0],
               [4, 0, 1, 2, 0, 0],
               [0, 1, 0, 7, 9, 0],
               [0, 2, 7, 0, 0, 0],
               [0, 0, 9, 0, 0, 3],
               [0, 0, 0, 0, 3, 0]])

# Crear grafo a partir de la matriz de adyacencia
G = nx.from_numpy_array(AD)

# Renombrar los nodos
valores = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
G = nx.relabel_nodes(G, valores)

# Obtener el grado de cada nodo
grados = dict(G.degree())
print("Grado de cada nodo:", grados)

# Layout del grafo
pos = nx.spring_layout(G)

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

# Dibujar las etiquetas de los bordes (weights)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Añadir texto al gráfico para mostrar el grado de cada nodo
for node, (x, y) in pos.items():
    plt.text(x, y + 0.1, f"Grado: {grados[node]}", fontsize=12, ha='center')

# Añadir título al gráfico
plt.text(-1.68, 1.109, "Grafito", fontsize=15, fontweight='bold')

# Mostrar el gráfico
plt.show()
