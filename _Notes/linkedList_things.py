"""
Linked List(鏈結串列) 

1. Node資料型態、記憶體大小不必相同
2. 只能做循序存取 (Sequential access)
3. 有head(第一個node)、tail(最後一個node)、current(當前node)

圖示:
    (1) -> (2) -> (3) -> NULL
    其中(1)為head，(3)為tail，最後指向NULL

注意:
1. 對Node進行增加或修改時，通常是對(某個Node).next下指令
    如:
        增加一個Node到尾端: self.tail.next = newNode
        刪除一個Node: self.tail.next = None
2. 找到鍊表中的特定位置可以使用以下Pattern
    如找到N的位子:
        N
    

"""

class Node:
    def __init__(self ,data=None, next=None):
      self.data = data
      self.next = next

class SingleLinkedList:
    def __init__(self):
      self.head = None   # 起始Linked List沒有資料，所以head跟tail都初始化為None
      self.tail = None

    def append(self, data):
      new_node = Node(data)
      
      if self.head == None:       # 如果head為None，此Data為第一個值，設定其為head跟tail(將head跟tail指向new_node)
        self.head = new_node
        self.tail = new_node

      else:
        self.tail.next = new_node      # 設定tail的node的next指向new_node
        self.tail = self.tail.next     # 在將tail的指向new_node

    def delete(self):
        if self.head == None:     # 確定Linked List有資料
            return
        else:
            if len(self) == 1:    # Linked List只有一個值
                self.head = None
            else:
                current_node = self.head
                while current_node.next != None: # 只要當前下一個的node有值
                    self.tail = current_node     # tail就繼續指向當前node，最終目的為將tail指向倒數第二個node，才能用self.tail.next = None
                    current_node = current_node.next  # 當前node就繼續指向下一個node
                self.tail.next = None # 刪除最後的Node

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:    #插入第0個
            new_node.next = self.head     # 設置新node的下一個為現在的head
            self.head = new_node          # 設置新node為現在的head
        
        if index > 0 and index < len(self):    # 確定不會out of range且不是第0個
            current_node = self.head           # current指向head
            current_index = 1
            while current_index != index:         
                current_node = current_node.next    # current指向下一個node，目的是將currentNode指向第N-1個Node，才能使用current_node.next = new_node
                current_index += 1
            new_node.next = current_node.next     # 先將指定位置後的所有Node接到新Node上
            current_node.next = new_node          # 再將currentNode的下一個指向new_node
                
            
            
