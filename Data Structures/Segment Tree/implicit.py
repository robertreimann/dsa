class SegmentTree:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        self.build()

    def build(self):
        def _build(v = 1, l = 0, r = len(self.nums) - 1):
            if l == r:
                self.tree[v] = self.nums[l]
                return
            
            mid = (l + r) // 2
            _build(v * 2, l, mid)
            _build(v * 2 + 1, mid + 1, r)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
        _build()

    def update(self, index, value):
        def _update(v = 1, l = 0, r = len(self.nums) - 1):
            if l == r:
                self.tree[v] = value
                return
            
            mid = (l + r) // 2
            if index <= mid:
                _update(v * 2, l, mid)
            else:
                _update(v * 2 + 1, mid + 1, r)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
        _update()
    
    def query(self, left, right):
        def _query(ql, qr, v = 1, l = 0, r = len(self.nums) - 1):
            if ql > qr:
                return 0
            
            if ql == l and qr == r:
                return self.tree[v]
            
            mid = (l + r) // 2
            left = _query(ql, min(qr, mid), v * 2, l, mid)
            right = _query(max(ql, mid + 1), qr, v * 2 + 1, mid + 1, r)
            return left + right
        return _query(left, right)

tree = SegmentTree([1,3,5])

# [0, 9, 4, 5, 1, 3, 0, 0, 0, 0, 0, 0]
print(tree.tree)

# 9
print(tree.query(0,2))

tree.update(1, 2)

# [0, 8, 3, 5, 1, 2, 0, 0, 0, 0, 0, 0]
print(tree.tree)

# 8
print(tree.query(0,2))
