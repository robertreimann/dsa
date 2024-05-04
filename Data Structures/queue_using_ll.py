class ListNode:
    def __init__(self, val = None) -> None:
        self.val = val
        self.next = None

class Queue:
    # Time complexity of enqueue: O(1) 
    # Time complexity of dequeue: O(1) 
    # Time complexity of peek: O(1)
    def __init__(self, val = None) -> None:
        self.val = val
        self.next = None

    def enqueue(self, val) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self) -> int:
        head = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return head.val
    
    def peek(self) -> int:
        return self.head.val
    
    def empty(self) -> bool:
        return self.head
            