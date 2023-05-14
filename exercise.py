import heapq


def dijkstra(grafo, inicio, final):
    distances = {node: float("inf") for node in grafo}
    distances[inicio] = 0
    pq = [(0, inicio)]
    while len(pq) > 0:
        current_distance, current_node = heapq.heappop(pq)
        if current_node == final:
            return current_distance
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in grafo[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return "Ninguno"


n_cases = int(input())
for _ in range(n_cases):
    n, m, start, end = map(int, input().split())
    graph = {i: {} for i in range(1, n + 1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w
    result = dijkstra(graph, start, end)
    print(result)
