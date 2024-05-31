class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, nums) -> None:
        self.length = len(nums) - 1
        self.root = self.build(nums)

    def build(self, nums):
        def _build(l = 0, r = self.length):
            if l == r:
                return Node(nums[l])
            
            mid = (l + r) // 2
            left = _build(l, mid)
            right = _build(mid + 1, r)

            current = Node(left.val + right.val, left, right)
            return current
        return _build()

    def update(self, index, value):
        def _update(node = self.root, l = 0, r = self.length):
            if l == r:
                node.val = value
                return
            
            mid = (l + r) // 2
            if index <= mid:
                _update(node.left, l, mid)
            else:
                _update(node.right, mid + 1, r)
            node.val = node.left.val + node.right.val
        _update()
    
    def query(self, left, right):
        def _query(ql, qr, node = self.root, l = 0, r = self.length):
            if ql > qr:
                return 0
            
            if ql == l and qr == r:
                return node.val
            
            mid = (l + r) // 2
            left = _query(ql, min(mid, qr), node.left, l, mid)
            right = _query(max(ql, mid + 1), qr, node.right, mid + 1, r)
            return left + right
        return _query(left, right)