"""
Linked List(鏈結串列) 

1. Node資料型態、記憶體大小不必相同
2. 只能做循序存取 (Sequential access)
3. 有head(第一個node)、tail(最後一個node)、current(當前node)
"""

class Node:
    def __init__(self ,data=None, next=None):
      self.data = data
      self.next = next

class SingleLinkedList:
    def __init__(self):
      self.head = None   #起始串列沒有資料，所以head跟tail都初始化為None
      self.tail = None

    def append(self, data):
      new_node = Node(data)
      
      if self.head == None:       # 如果head為None，此Data為第一個值，設定其為head跟tail(將head跟tail指向new_node)
        self.head = new_node
        self.tail = new_node

      else:
        self.tail.next = new_node      #設定現在
        self.tail = self.tail.next
