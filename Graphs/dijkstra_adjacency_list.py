from collections import defaultdict
from heapq import heappop, heappush


class Dijkstra:
    # Edges are in a format [source, destination, weight]
    # [[2,1,1],[2,3,1],[3,4,1]]
    # Returns the cost of the minimum path if it is found.
    def dijkstra_adjacency_list(edges, start_node, end_node):
        adjacency_list = defaultdict(list)
        for source, destination, weight in edges:
            adjacency_list[source].append((weight, destination))

        heap = [(0, start_node)]
        visited = set()

        while heap:
            time, node = heappop(heap)
            if node == end_node:
                return time
            if node in visited:
                continue
            visited.add(node)

            for n_time, n_dest in adjacency_list[node]:
                heappush(heap, (n_time + time, n_dest))
        return -1

class Dijkstra_modified:
    # Edges are in a format [source, destination, weight]
    # [[2,1,1],[2,3,1],[3,4,1]]
    # Returns the minimum cost to reach all nodes if we can travel edges concurrently.
    # For example it answers if we send a signal from start node, how long does it take to reach all nodes?
    # Assumes that a connected graph is given.
    def dijkstra_adjacency_list_modified(edges, start_node):
        adjacency_list = defaultdict(list)
        for source, destination, weight in edges:
            adjacency_list[source].append((weight, destination))

        heap = [(0, start_node)]
        visited = set()

        total_weight = 0
        while heap:
            time, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            total_weight = time

            for n_time, n_dest in adjacency_list[node]:
                heappush(heap, (n_time + time, n_dest))
        return total_weight
        