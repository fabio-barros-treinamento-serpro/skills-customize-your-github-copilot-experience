from __future__ import annotations

from collections import deque
import heapq
from math import inf


# Grafo não ponderado para BFS
UNWEIGHTED_GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

# Grafo ponderado para Dijkstra
# Formato: no -> lista de tuplas (vizinho, peso)
WEIGHTED_GRAPH = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("D", 2), ("E", 7)],
    "C": [("A", 4), ("F", 3)],
    "D": [("B", 2), ("G", 6)],
    "E": [("B", 7), ("F", 1), ("G", 5)],
    "F": [("C", 3), ("E", 1), ("G", 2)],
    "G": [("D", 6), ("E", 5), ("F", 2)],
}


def bfs_shortest_path(graph: dict[str, list[str]], start: str, end: str) -> list[str]:
    """Retorna o menor caminho (em numero de arestas) de start ate end."""
    if start not in graph or end not in graph:
        return []

    queue = deque([start])
    parent: dict[str, str | None] = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break

        for neighbor in graph[current]:
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    if end not in parent:
        return []

    path: list[str] = []
    node: str | None = end
    while node is not None:
        path.append(node)
        node = parent[node]

    return list(reversed(path))


def validate_non_negative_weights(graph: dict[str, list[tuple[str, int]]]) -> None:
    for node, edges in graph.items():
        for neighbor, weight in edges:
            if weight < 0:
                raise ValueError(
                    f"Aresta invalida: {node} -> {neighbor} com peso negativo ({weight})"
                )


def dijkstra_shortest_path(
    graph: dict[str, list[tuple[str, int]]], start: str, end: str
) -> tuple[int, list[str]]:
    """Retorna (distancia_total, caminho) usando Dijkstra."""
    if start not in graph or end not in graph:
        return inf, []

    validate_non_negative_weights(graph)

    distances = {node: inf for node in graph}
    previous: dict[str, str | None] = {node: None for node in graph}
    distances[start] = 0

    heap: list[tuple[int, str]] = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        if current_node == end:
            break

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (new_distance, neighbor))

    if distances[end] == inf:
        return inf, []

    path: list[str] = []
    node: str | None = end
    while node is not None:
        path.append(node)
        node = previous[node]

    return int(distances[end]), list(reversed(path))


def compare_algorithms(start: str, end: str) -> None:
    bfs_path = bfs_shortest_path(UNWEIGHTED_GRAPH, start, end)
    dijkstra_cost, dijkstra_path = dijkstra_shortest_path(WEIGHTED_GRAPH, start, end)

    print(f"Origem: {start} | Destino: {end}")
    print("=" * 50)
    print(f"BFS - caminho por arestas: {bfs_path}")
    print(f"BFS - quantidade de arestas: {max(len(bfs_path) - 1, 0)}")
    print(f"Dijkstra - caminho por custo: {dijkstra_path}")
    print(f"Dijkstra - custo total: {dijkstra_cost}")


if __name__ == "__main__":
    print("Teste 1")
    compare_algorithms("A", "G")

    print("\nTeste 2")
    compare_algorithms("B", "F")

    print("\nAnalise teorica de complexidade:")
    print("- BFS: O(V + E)")
    print("- Dijkstra com heap binario: O((V + E) log V)")
