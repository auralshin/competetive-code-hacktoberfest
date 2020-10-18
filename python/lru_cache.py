class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.value.__repr__()


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head is not None:
            self.head.prev = node
            node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = node

    def delete(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

    def move_to_head(self, node):
        self.delete(node)
        self.add(node)

    def get_iter(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next


class LRU:
    def __init__(self, cap):
        self.map = {}
        self.items = DoubleLinkedList()
        self.cap = cap

    def delete_lru(self):
        if self.items.tail is None:
            return

        lru_node = self.items.tail
        self.delete(lru_node.value[0])

    def store(self, key, val):
        if len(self.map) >= self.cap:
            self.delete_lru()

        node = Node((key, val))
        self.map[key] = node
        self.items.add(node)

    def get(self, key):
        if key not in self.map:
            return None

        node = self.map[key]
        self.items.move_to_head(node)
        return node.value[1]

    def delete(self, key):
        if key not in self.map:
            return

        node = self.map[key]
        self.items.delete(node)
        del self.map[key]


# ============================= Examples of use =============================

def to_list(cache):
    return list(map(lambda node: node.value[0], cache.items.get_iter()))


cache = LRU(5)
for i in range(10):
    cache.store(i, 'dummy value')
    print(i, to_list(cache))
    if i % 2 == 0:
        print(i, cache.get(i // 2), i // 2, end=' ')
        print(to_list(cache))


print('='*50)

cache.delete(3)
print(3, to_list(cache))

print('none?', cache.get(3))

print('7', cache.get(7))

cache.store(10, 'dummy value')
print('10', to_list(cache))

cache.store(20, 'dummy value')
print('20', to_list(cache))
