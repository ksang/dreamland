class Node:

    __slots__ = ['key','value','prev','next']

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.mapping = {}
        self.head = self.tail = None

    def __insert_to_head(self, node):
        saved_head = self.head
        self.head = node
        node.prev = None
        if saved_head is None:
            # first node
            self.tail = node
            return
        node.next = saved_head
        saved_head.prev = node        

    def __move_to_head(self, node):
        # node is already the head
        if node.prev is None: 
            return
        # link node's neighbors        
        if node.next is None:
            # tail was this node, moving it will cause tail change.
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev.next = node.next
        self.__insert_to_head(node)

    def __cut_tail(self):
        if self.tail is None:
            return
        saved_tail = self.tail
        saved_key = saved_tail.key
        self.tail = saved_tail.prev
        self.tail.next = None
        self.mapping.pop(saved_key)
        self.size -= 1

    def __add_new(self, key, value):
        node = Node(key, value)
        self.__insert_to_head(node)
        self.mapping[key] = node
        self.size += 1
        if self.size > self.capacity:
            self.__cut_tail()

    def get(self, key):
        node = self.mapping.get(key)
        if node is not None:
            self.__move_to_head(node)
            return node.value
        else: 
            return None

    def set(self, key, value):
        node = self.mapping.get(key)
        if node is not None:
            node.value = value
            self.__move_to_head(node)
        else:
            self.__add_new(key, value)

    def touch(self, key, value):
        self.set(key, value)