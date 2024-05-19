class UnionFind:
    def __init__(self, nodes) -> None:
        self.reps = {}
        self.size = {}
        for n in nodes:
            self.reps[n] = n
            self.size[n] = 1

    def find(self, t):
        if t == self.reps[t]:
            return t
        self.reps[t] = self.find(self.reps[t])
        return self.reps[t]
    
    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return False
        
        if self.size[ru] < self.size[rv]:
            ru, rv = rv, ru

        self.reps[rv] = ru
        self.size[ru] += self.size[rv]
        return True

class Kruskal:
    # https://leetcode.com/problems/min-cost-to-connect-all-points/
    def kruskal(self, points):
        indexes = [i for i in range(len(points))]
        uf = UnionFind(indexes)

        heap = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                distance = get_manhattan_distance()