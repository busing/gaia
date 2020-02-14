#! -*- encoding-utf-8 -*-
from computer_principle.DoubleLinkedList import  DoubleLinkedList,Node

class LRUCache(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.map ={}
        self.list = DoubleLinkedList(self.capacity)

    def get(self,key):
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self.list.append_front(node)
            return node.value
        else:
            return -1

    def put(self,key,value):
        if key in self.map:
            node = self.map[key]
            self.list.remove()
            node.value = value
            self.list.append_front(node)
        else:
            if self.list.size >= self.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)
            node = Node(key, value)
            self.list.append_front(node)
            self.map[key] = node

    def print(self):
        self.list.print()

if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1,1)
    cache.print()

    cache.put(2, 2)
    cache.print()

    cache.put(3, 3)
    cache.print()

    cache.get(1)
    cache.print()

    cache.get(1)
    cache.print()
