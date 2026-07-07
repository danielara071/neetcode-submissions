class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nextt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.nextt = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nextt = node.nextt
        prev.nextt = nextt
        nextt.prev = prev

    def insert(self, node):
        mru = self.right.prev
        mru.nextt = node
        node.prev = mru
        node.nextt = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]= Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.nextt
            self.remove(lru)
            del(self.cache[lru.key])


