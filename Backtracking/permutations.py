class Permutations:
    def permute(array):
        answer = []
        def dfs(sub = []):
            if len(sub) == len(array):
                answer.append(sub.copy())
                return
            
            for i in range(len(array)):
                if array[i] not in sub:
                    sub.append(array[i])
                    dfs(sub)
                    sub.pop()
        dfs()
        return answer
    
    def permute_carry(array):
        def dfs(sub = []):
            if len(sub) == len(array):
                return [sub.copy()]
            
            answer = []
            for i in range(len(array)):
                if array[i] not in sub:
                    sub.append(array[i])
                    answer += dfs(sub)
                    sub.pop()
            return answer
        return dfs()