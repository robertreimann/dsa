class Subsets:
    def generate(self, arr):
        subsets = []
        def dfs(i, sub):
            if i == len(arr):
                subsets.append(sub.copy())
                return

            # pick
            sub.append(arr[i])
            dfs(i + 1, sub)
            sub.pop()

            # don't pick
            dfs(i + 1, sub)
        dfs(0, [])
        return subsets
    
    def generate2(self, arr):
        subsets = []
        def dfs(i, sub):
            subsets.append(sub.copy())

            # No explicit base case necessary, because the for loop stops the recursion when i >= len(arr)
            for j in range(i, len(arr)):
                sub.append(arr[j])
                dfs(j + 1, sub)
                sub.pop()
    
        dfs(0, [])
        return subsets

    def sum(self, arr):
        def dfs(i, sub_sum):
            if i == len(arr):
                return sub_sum
            
            pick = dfs(i + 1, sub_sum + arr[i])
            dont_pick = dfs(i + 1, sub_sum)

            return pick + dont_pick
        return dfs(0, 0)


subsets = Subsets()
arr = [1, 2, 3]
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
print(subsets.generate(arr))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(subsets.generate2(arr))
# 24
print(subsets.sum(arr))
