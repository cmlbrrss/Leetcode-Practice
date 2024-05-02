"""
Linked List Notes
1. Node中的資料型態不必相同
2. 有head, tail, current的概念
    (1) head: 第一個node
    (2) tail: 最後一個node
    (3) current: 當前的node

"""
class Node:
    def __init__(self ,data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None
    
