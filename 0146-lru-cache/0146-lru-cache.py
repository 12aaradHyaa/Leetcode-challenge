class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()   # LRU
        self.right = Node()  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node at right (most recently used)
    def insert(self, node):
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Make it most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # If capacity exceeded
        if len(self.cache) > self.capacity:
            # Remove least recently used node
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]