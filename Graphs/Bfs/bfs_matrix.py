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
    # 3. Always use inclusive comparison for matrix bound checks, both for 0 and length - 1

    def bfs_matrix(self, grid):
        # This traverses the entire matrix, so if you need to not include some values in the
        # traversal then canGoX functions should be modified. For example, in 695. Max Area of Island
        # you only want to include 1s (land) in your queue.
        visited = set()
        q = deque([(grid[0][0], grid[0][1])])
        while q:
            node = q.popleft()
            if node in visited or not self.is_in_bounds(grid, node):
                continue
            visited.add(node)

            q.append((node[0], node[1] - 1))
            q.append((node[0], node[1] + 1))            
            q.append((node[0] - 1, node[1]))
            q.append((node[0] + 1, node[1]))
    
    def is_in_bounds(self, grid, node):
        row_size = len(grid) - 1
        column_size = len(grid[0]) - 1
        row_index, column_index = node
        return row_index >= 0 and row_index <= row_size and column_index >= 0 and column_index <= column_size