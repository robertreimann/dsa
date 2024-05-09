class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    #    The idea is to hold values with pointer to the ListNode in the map
    # 1. Initialize capacity, map, doubly linked list head and tail pointers
    # 2. On get, if it is not in map, return -1
    #            otherwise, removeFromList & insertToHead
    # 3. On put, if is in the map:
    #               removeFromList & insertToHead
    #            otherwise,
    #               if capacity is full:
    #                   removeTail
    #               insertToHead 
    # Create functions, insertToHead, removeFromList, removeTail, don't forget to adjust tail
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.dummy = ListNode(-1)
        self.tail = self.dummy

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value, node = self.map[key]
        self.remove_from_list(node)
        self.insert_to_head(node)
        return value

    def put(self, key: int, value: int) -> None:
        node = ListNode(key)
        if key in self.map:
            node = self.map[key][1]
            self.remove_from_list(node)
        elif len(self.map) == self.capacity:
            self.remove_tail()
        self.insert_to_head(node)
        self.map[key] = (value, node)

    def remove_from_list(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        if next:
            next.prev = prev
        else: 
            # node was tail, so we have to update tail
            self.tail = prev
    
    def insert_to_head(self, node):
        previous_head = self.dummy.next
        # Tie it to dummy node
        node.prev = self.dummy
        self.dummy.next = node
        node.next = previous_head
        if previous_head:
            # Tie to previous node
            previous_head.prev = node
        else:
            # if previous_head didn't exist, that means we just added the first element
            # so the head is also the tail
            self.tail = node
    
    def remove_tail(self):
        del self.map[self.tail.val]
        self.tail = self.tail.prev
        self.tail.next = None