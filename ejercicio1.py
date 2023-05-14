import networkx as nx
import matplotlib.pyplot as plt


def dfs(node, grafo, visitado):
    visitado[node] = True
    tamanio = 1
    for neighbor in grafo[node]:
        if not visitado[neighbor]:
            tamanio += dfs(neighbor, grafo, visitado)
    return tamanio


with open("ciudad_amistosos.txt", "r") as f:
    n_cases = int(f.readline())
    for i in range(n_cases):
        n, m = map(int, f.readline().split())

        graph = nx.Graph()
        for j in range(m):
            a, b = map(int, f.readline().split())
            graph.add_edge(a, b)

        visited = [False] * (n + 1)
        sizes = []
        for j in range(1, n + 1):
            if not visited[j]:
                size = dfs(j, graph, visited)
                sizes.append(size)

        max_size = max(sizes)
        print(f"Caso #{i + 1} - Tot. Residentes: {max_size}")

        # representación gráfica
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, font_weight='bold')
        plt.show()

"""Utilicé la búsqueda en profundidad (DFS) en este ejercicio porque el problema implica encontrar grupos de amigos 
en una red social. Lo que hace DFS es visitar todos los nodos conectados en un grafo, en este caso, todos los amigos 
de un residente de la ciudad. La complejidad del algoritmo implementado es O(N + M), donde N es el número de 
residentes y M es el número de relaciones de amistad entre ellos."""
