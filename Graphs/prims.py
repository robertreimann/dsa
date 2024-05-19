from collections import defaultdict
from heapq import heappop, heappush

class Prims:
    # https://leetcode.com/problems/min-cost-to-connect-all-points/
    # Prim's itself is O(ElogV), but in this case we have to construct the adjacency list which is O(n^2)
    # Note to self: you can't carry the total_weight in the heap itself like you would a path because when you add the final node
    # the path does not necessarily contain all nodes - other paths might have visited other nodes and they must be counted as well
    # so it is important to keep a global total weight sum that is update every time you visit a new vertice.
    def prims_adjacency_list(self, points):
        adj_list = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                adj_list[i].append(j)

        heap = [(0, 0)]
        visited = set()
        total_weight = 0
        while heap:
            weight, node = heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            total_weight += weight
            if len(visited) == len(points):
                return total_weight

            for neighbor in adj_list[node]:
                if neighbor in visited: continue
                heappush(heap, (self.get_manhattan_distance(points[node], points[neighbor]), neighbor))
    
    def get_manhattan_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
