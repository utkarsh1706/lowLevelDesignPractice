from Node import Node

class LRU:
    def __init__(self, c: int) -> None:
        self.capacity = c
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def getValue(self, key):
        if key in self.cache:
            nodeStored = self.cache[key]
            self.moveToHead(nodeStored)
            return nodeStored.value
        return None

    def putValue(self, key, value):
        if key in self.cache:
            nodeStored = self.cache[key]
            nodeStored.value = value
            self.moveToHead(nodeStored)
        else:
            if len(self.cache) >= self.capacity:
                self.removeNode(self.tail.prev)
            newNode = Node(key, value)
            self.addtoHead(newNode)
            self.cache[key] = newNode

    def addtoHead(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addtoHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]

    def removeKey(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
