from collections import deque

class LRUCache:
    # 1. Initialize capacity, map, dequeue
    # 2. On get, update index of key to be 0 in the queue if it already exists
    #            otherwise, return -1
    # 3. On put, update index of key to be 0 in the queue if it already exists
    #            otherwise, delete the last element from map and queue.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.q = deque([])

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.remove_index(key)
        self.q.appendleft(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove_index(key)
        elif len(self.q) == self.capacity:
            least_recently_used = self.q.pop()
            del self.map[least_recently_used]

        self.q.appendleft(key)
        self.map[key] = value

    def remove_index(self, key):
        current_index = self.q.index(key) # O(n) operation
        del self.q[current_index]