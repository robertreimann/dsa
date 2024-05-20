from collections import defaultdict
from functools import cache


class Partitions:
    # https://leetcode.com/problems/palindrome-partitioning/
    def partition_palindromically(self, s):
        answer = []
        def dfs(i, partition):
            if len(s) == i:
                answer.append(partition.copy())
                return
            
            substring = ""
            for j in range(i, len(s)):
                substring += s[j]
                if substring == substring[::-1]: # <-- This here is the key line, the partitioning condition
                    partition.append(substring)
                    dfs(j + 1, partition)
                    partition.pop()
        dfs(0, [])
        return answer
    
    # Minimum Substring Partition of Equal Character Frequency
    # https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description/
    # This is technically DP since we need to only count and not generate but close enough.
    def min_substring_partition(self, s):
        @cache
        def dfs(i):
            if i == len(s):
                return 0

            frequency_map = defaultdict(lambda: 0)
            count = float('inf')
            for j in range(i, len(s)):
                frequency_map[s[j]] += 1
                if len(set(frequency_map.values())) == 1: # <-- This here is the key line, the partitioning condition
                    count = min(count, 1 + dfs(j + 1))
            return count
        return dfs(0)
    

partitioner = Partitions()
s = "aab"
# [['a', 'a', 'b'], ['aa', 'b']]
print(partitioner.partition_palindromically(s))

s2 = "fabccddg"
# 3
print(partitioner.min_substring_partition(s2))