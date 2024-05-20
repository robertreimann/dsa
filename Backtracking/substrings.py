class Substrings:
    # O(2^n) very inefficient though, idk why I would use this tbh
    def generate_backtrack(self, s):
        answer = set()
        def dfs(i, sub):
            if len(sub) > 0:
                answer.add(sub)
        
            substring = ""
            for j in range(i, len(s)):
                substring += s[j]
                dfs(j + 1, substring)
        dfs(0, "")
        return sorted(list(answer), key=lambda x: (len(x), x[0]))
    
    # O(n^2)
    def generate(self, s):
        answer = []
        for i in range(len(s)):
            substring = ""
            for j in range(i, len(s)):
                substring += s[j]
                answer.append(substring)

        return sorted(list(answer), key=lambda x: (len(x), x[0]))
substrings = Substrings()
s = "abc"
# ['a', 'b', 'c', 'ab', 'bc', 'abc']
print(substrings.generate_backtrack(s))
print(substrings.generate(s))
