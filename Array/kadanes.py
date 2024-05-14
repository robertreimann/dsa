from typing import List

class Kadane:
    def Kadanes(self, nums: List[int]):
        max_sum = float('-inf')
        cur_sum = 0
        for n in nums:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(max_sum, cur_sum)
        return max_sum
    
k = Kadane()

print(k.Kadanes([-2,1,-3,4,-1,2,1,-5,4]))