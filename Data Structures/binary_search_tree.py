class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST:
    def construct(nums, left, right):
        if left > right: 
            return None
        
        mid = (left + right) // 2
        node = Node(nums[mid])
        node.left = BST.construct(nums, left, mid - 1)
        node.right = BST.construct(nums, mid + 1, right)
        return node

traversal_result = []
def dfs(node):
    if not node:
        return
    
    dfs(node.left)
    traversal_result.append(node.val)
    dfs(node.right)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = BST.construct(array, 0, len(array) - 1)
dfs(root)
assert(array == traversal_result)