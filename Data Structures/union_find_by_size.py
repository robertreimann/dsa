class UnionFind:
    # Union Find by size with path compression, assumes nodes are hashable
    # Returns True if nodes are connected on union, False if they were already connected
    def __init__(self, nodes):
        self.size = {}
        self.reps = {}
        for node in nodes:
            self.reps[node] = node
            self.size[node] = 1

    def find(self, target):
        if target == self.reps[target]:
            return target
        
        self.reps[target] = self.find(self.reps[target])
        return self.reps[target]
    
    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)

        if ru == rv:
            return False
        
        if self.size[ru] < self.size[rv]:
            ru, rv = rv, ru
        self.size[ru] += self.size[rv]
        self.reps[rv] = ru
        return True