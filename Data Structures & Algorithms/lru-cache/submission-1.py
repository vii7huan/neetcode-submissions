# class Node:
#     def __init__(self, key: int, val: int):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.left, self.right = Node(0,0), Node(0,0)
#         self.left.next = self.right
#         self.right.prev = self.left

#     def _remove(self,node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
    
#     def _insert(self, node):
#         p = self.right.prev
#         p.next = node
#         node.prev = p
#         node.next = self.right
#         self.right.prev = node

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             n = self.cache[key]
#             self._remove(n)
#             self._insert(n)
#             return n.val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self._remove(self.cache[key])
#         n = Node(key,value)
#         self.cache[key] = n
#         self._insert(n)
#         if len(self.cache) > self.cap:
#             lru = self.left.next
#             self._remove(lru)
#             del self.cache[lru.key]


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
