import networkx as nx
import matplotlib.pyplot as plt

def max_black_nodes(G):
    # Ordenar los nodos por grado descendente
    nodes = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    # Crear un diccionario para almacenar la coloración de cada nodo
    colors = {node: None for node in nodes}
    # Asignar el color negro a los nodos en orden descendente de grado
    for node in nodes:
        neighbors = set(G.neighbors(node))
        black_neighbors = [n for n in neighbors if colors[n] == 'black']
        if not black_neighbors:
            colors[node] = 'black'
        else:
            colors[node] = 'white'
    # Crear un grafo nuevo con la coloración resultante
    H = nx.Graph()
    for node, color in colors.items():
        H.add_node(node, color=color)
    for u, v in G.edges():
        if colors[u] != 'black' or colors[v] != 'black':
            H.add_edge(u, v)
    return H

# Ejemplo de uso
G = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5),(4,6),(5,6)])
H = max_black_nodes(G)
print("Coloración óptima:")
print(H.nodes(data=True))
print(H.edges())

# Dibujar el grafo resultante
pos = nx.spring_layout(H) # Obtener la posición de los nodos para dibujar el grafo
node_colors = [data['color'] for _, data in H.nodes(data=True)] # Obtener los colores de los nodos
edge_colors = ['black' if H[u][v].get('color', 'white') != 'black' else 'red' for u, v in H.edges()] # Obtener los colores de las aristas
nx.draw(H, pos, node_color=node_colors, edge_color=edge_colors, with_labels=True) # Dibujar el grafo
plt.show() # Mostrar el grafo dibujado