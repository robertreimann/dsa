class Dfs:
    # O(V + E)

    # Did you forget something checklist:
    # 1. Did you add a base case?
    # 2. Did you add node to visited set (if you don't know for sure that graph is acyclic)
    # 3. Did you recursively call dfs? (if you forget this then what are you even doing?!)
    # 4. Did you compute and return the answer?

    # Standards:
    # 1. Use nested dfs function to avoid global variables and having to pass in adjacency lists etc which complicate caching.
    # 2. Pass in a visited set instead of using a global one so the @cache decorator can be slapped on for ez DP.
    # 3. Name the current node vertex, if tracking index in a list of nodes instead, use index.

    def dfs_neighbors(node):
        if not node:
            return None
        
        def dfs(vertex, visited):
            if vertex in visited:
                return
            visited.add(vertex)

            for neighbor in vertex.neighbors:
                dfs(neighbor, visited)
        dfs(node, set())