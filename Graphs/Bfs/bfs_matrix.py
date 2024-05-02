from collections import deque

class Bfs:
    # O(V + E)

    # Did you forget something checklist:
    # 1. Are you popping the node off the left?
    # 2. Are you checking if it is in visited?
    # 3. Are you adding new nodes?

    # Standards
    # 1. Name the deque 'q'
    # 2. Use functions to check if a node can be added to the queue

    def bfs_matrix(self, grid):
        # This traverses the entire matrix, so if you need to not include some values in the
        # traversal then canGoX functions should be modified. For example, in 695. Max Area of Island
        # you only want to include 1s (land) in your queue.
        visited = set()
        q = deque([(grid[0][0], grid[0][1])])
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)

            if self.canGoLeft(node, grid):
                q.append((node[0], node[1] - 1))
            if self.canGoRight(node, grid):
                q.append((node[0], node[1] + 1))
            if self.canGoUp(node, grid):
                q.append((node[0] - 1, node[1]))
            if self.canGoDown(node, grid):
                q.append((node[0] + 1, node[1]))

    def canGoLeft(self, node, grid):
        i, j = node
        if j == 0:
            return False
        return True

    def canGoRight(self, node, grid):
        i, j = node
        if j == len(grid[0]) - 1:
            return False
        return True

    def canGoUp(self, node, grid):
        i, j = node
        if i == 0:
            return False
        return True

    def canGoDown(self, node, grid):
        i, j = node
        if i == len(grid) - 1:
            return False
        return True

        