from typing import List


class SegmentTree:

    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        self.tr = len(nums) - 1
        self.build(1, 0, self.tr)
        
    def build(self, v, l, r):
        if l == r:
            self.tree[v] = self.nums[l]
            return
        
        tm = (l + r) // 2
        self.build(v * 2, l, tm)
        self.build(v * 2 + 1, tm + 1, r)
        self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

    def update(self, index, val):
        def update_tree(v = 1, tl = 0, tr = self.tr):
            if tl == tr:
                self.tree[v] = val
                return
            
            tm = (tl + tr) // 2
            if index <= tm:
                update_tree(v * 2, tl, tm)
            else:
                update_tree(v * 2 + 1, tm + 1, tr)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
        update_tree()

    def sumRange(self, left, right):
        def query(l, r, v = 1, tl = 0, tr = self.tr):
            if l > r:
                return 0
            
            if l == tl and r == tr:
                return self.tree[v]
            
            tm = (tl + tr) // 2
            left = query(l, min(r, tm), v * 2, tl, tm)
            right = query(max(l, tm + 1), r, v * 2 + 1, tm + 1, tr)
            return left + right
        
        return query(left, right)

tree = SegmentTree([1,3,5])

# [0, 9, 4, 5, 1, 3, 0, 0, 0, 0, 0, 0]
print(tree.tree)

# 9
print(tree.sumRange(0,2))

tree.update(1, 2)

# [0, 8, 3, 5, 1, 2, 0, 0, 0, 0, 0, 0]
print(tree.tree)

# 8
print(tree.sumRange(0,2))
