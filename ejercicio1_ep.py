import networkx as nx
import matplotlib.pyplot as plt


def alg_floyd_warshall(distancia, num):
    dist_copy = [row[:] for row in distancia]
    for k in range(num):
        for i in range(num):
            for j in range(num):
                dist_copy[i][j] = min(dist_copy[i][j], dist_copy[i][k] + dist_copy[k][j])
    return dist_copy


def remove_unnecessary(distancia, num):
    for i in range(num):
        for j in range(i + 1, num):
            for k in range(j + 1, num):
                if distancia[i][j] == distancia[i][k] + distancia[k][j]:
                    distancia[i][j] = distancia[j][i] = 0
                    break
    return distancia    


with open('tabla_caminos.txt') as f:
    t = int(f.readline())
    for _ in range(t):
        num_nodos = int(f.readline())
        dist = [list(map(int, f.readline().split())) for _ in range(num_nodos)]

    alg_floyd_warshall(dist, num_nodos)

    G = nx.Graph()
    for i in range(num_nodos):
        G.add_node(i + 1)
    for i in range(num_nodos):
        for j in range(num_nodos):
            if dist[i][j] != float('inf'):
                G.add_edge(i + 1, j + 1, weight=dist[i][j])

    nx.draw(G, with_labels=True)
    plt.show()

    vecinos = set()
    for i in range(num_nodos):
        for j in range(i + 1, num_nodos):
            for k in range(num_nodos):
                if k != i and k != j and dist[i][j] == dist[i][k] + dist[k][j]:
                    vecinos.add((i + 1, k + 1))
                    vecinos.add((k + 1, j + 1))
                    break

    for pares in sorted(list(vecinos)):
        print(pares[0], pares[1])

""" Usamos el algoritmo de Floyd-Warshall en este problema porque este es un algoritmo capaz de
    encontrar las distancias más cortas entre cada par de nodos en un grafo ponderado, como en este ejercicio,
    las distancias más cortas entre cada par de ciudades en una red de carreteras. Una vez que se han encontrado estas
    distancias, se puede buscar los pares de ciudades que sean vecinas.
    La complejidad de este algoritmo es O(n^3), ya que se itera sobre todas las combinaciones posibles de ciudades.
"""
