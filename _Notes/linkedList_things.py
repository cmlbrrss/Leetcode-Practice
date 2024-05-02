"""
Linked List(鏈結串列) 

1. Node資料型態、記憶體大小不必相同
2. 只能做循序存取 (Sequential access)
3. 實際上python沒有SingleLinkedList、ListNode要自己宣告
4. 常用可以宣告有head(第一個node)、tail(最後一個node)、current(當前node)，進行撰寫

圖示:
    (1) -> (2) -> (3) -> NULL
    其中(1)為head，(3)為tail，最後指向NULL

注意:
1. 對Node進行增加或修改時，通常是對(某個Node).next下指令
    如:
        增加一個Node到尾端: self.tail.next = newNode
        刪除一個Node: self.tail.next = None
2. 找到鍊表中的特定位置可以使用以下Pattern
        對self.head的部分進行處理    
        currentNode = self.head
        while 特定位置的否定條件(用ctr找特定位置: ctr != N-1，tail位置可以用None: currentNode.next != None):
            currentNode = currentNode.next
        (對currentNode.next進行目標操作)  
3. 若沒有宣告class SingleLinkedList(包含head、tail等)，一個linkedList的head
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
      newNode = Node(data)
      
      if self.head == None:       # 如果head為None，此Data為第一個值，設定其為head跟tail(將head跟tail指向new_node)
        self.head = newNode
        self.tail = newNode

      else:
        self.tail.next = newNode      # 設定tail的node的next指向new_node
        self.tail = self.tail.next     # 在將tail的指向new_node

    def delete(self):
        if self.head == None:     # 確定Linked List有資料
            return
        else:
            if len(self) == 1:    # Linked List只有一個值
                self.head = None
            else:
                currentNode = self.head
                while currentNode.next != None: # 只要當前下一個的node有值
                    self.tail = currentNode     # tail就繼續指向當前node，最終目的為將tail指向倒數第二個node，才能用self.tail.next = None
                    currentNode = currentNode.next  # 當前node就繼續指向下一個node
                self.tail.next = None # 刪除最後的Node

    def insert(self, idx, data):
        newNode = Node(data)
        if idx == 0:    #插入第0個
            newNode.next = self.head     # 設置新node的下一個為現在的head
            self.head = newNode          # 設置新node為現在的head
        
        if idx > 0 and idx < len(self):    # 確定不會out of range且不是第0個
            currentNode = self.head           # current指向head
            currentIdx = 1
            while currentIdx != index:         
                currentNode = currentNode.next    # current指向下一個node，目的是將currentNode指向第N-1個Node，才能使用current_node.next = new_node
                currentIdx += 1
            newNode.next = currentNode.next     # 先將指定位置後的所有Node接到新Node上
            currentNode.next = newNode          # 再將currentNode的下一個指向new_node
                
            
            
