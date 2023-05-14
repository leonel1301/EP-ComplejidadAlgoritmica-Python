import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8])

G.add_edges_from([(4, 0), (4, 3), (3, 1), (0, 1), (1, 4), (1, 2), (2, 5), (5, 7), (7, 8), (8, 5), (3, 6), (6, 4)])

plt.figure()
nx.draw(G, with_labels=True)
plt.title('Grafo original')
plt.show()

SCC = list(nx.strongly_connected_components(G))

print("Grupos de personas estrechamente vinculados:")
for group in SCC:
    print(group)

G_SCC = nx.DiGraph()
SCC_nodes = set().union(*SCC)
for edge in G.edges():
    if edge[0] in SCC_nodes and edge[1] in SCC_nodes:
        G_SCC.add_edge(edge[0], edge[1])

plt.figure()
nx.draw(G_SCC, with_labels=True)
plt.title('Grafo resultante con solo los nodos en SCC')
plt.show()

"""Usé SCC (Strongly Connected Components) para identificar grupos de nodos en un grafo dirigido que estén altamente 
conectados entre sí, lo cual pide el ejercicio. Estos componentes son subgrafos que cumplen la propiedad de que para cada par de nodos dentro de 
un componente, hay un camino dirigido desde uno de ellos hacia el otro."""