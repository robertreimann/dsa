class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class Reverse:
    def simple_iterative(head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def concise_iterative(head):
        prev = None
        #while head: head.next, prev, head = prev, head, head.next
        while head: head.next, head, prev = prev, head.next, head
        return prev

    def preorder_recursive(head):
        def recurse(head, prev):
            if not head:
                return prev
            next = head.next
            head.next = prev
            return recurse(next, head)
        return recurse(head, None)
    
    def postorder_recursive(head):
        if not head or not head.next:
            return head
        node = Reverse.postorder_recursive(head.next)
        head.next.next = head
        head.next = None
        return node
        
class Test:
    def generate_ll():
        head = ListNode(0)
        head_ptr = head
        for i in range(1, 10):
            head.next = ListNode(i)
            head = head.next
        return head_ptr

    def traverse(head):
        print('[', end="")
        while head:
            if head.next:
                print(head.val, end=" -> ")
            else:
                print(head.val, end="]")
            head = head.next
        print()

# 1
# [0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9]
Test.traverse(Test.generate_ll())
# [9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0]
Test.traverse(Reverse.simple_iterative(Test.generate_ll()))
print()

# 2
# [0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9]
Test.traverse(Test.generate_ll())
# [9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0]
Test.traverse(Reverse.concise_iterative(Test.generate_ll()))
print()

# 3
# [0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9]
Test.traverse(Test.generate_ll())
# [9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0]
Test.traverse(Reverse.preorder_recursive(Test.generate_ll()))
print()

# 4
# [0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9]
Test.traverse(Test.generate_ll())
# [9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0]
Test.traverse(Reverse.postorder_recursive(Test.generate_ll()))
print()