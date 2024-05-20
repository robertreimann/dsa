class Combinations:
    def n_choose_k(self, n, k):
        answer = []
        def dfs(i, sub):
            if i > n + 1:
                return
            if len(sub) == k:
                answer.append(sub.copy())
                return
            
            # pick
            sub.append(i)
            dfs(i + 1, sub)
            sub.pop()

            # don't pick
            dfs(i + 1, sub)
        dfs(1, [])
        return answer