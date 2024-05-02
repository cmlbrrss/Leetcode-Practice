"""
Linked List(鏈結串列) 

1. Node資料型態、記憶體大小不必相同
2. 只能做循序存取 (Sequential access)
3. 實際上python沒有SingleLinkedList要自己宣告
4. 常用可以宣告head(第一個node)、tail(最後一個node)、current(當前node)，方便進行撰寫
5. 每個ListNode的組成為val(這個Node的值)與Next(下一個Node的資訊)，因為Next包含了下一個Node值與他的Next，所以某個Node的next其實等同於儲存了此node以後所有node的資訊

圖示:
    (1) -> (2) -> (3) -> None

實際結構，以[1 2 3 4 5]為例:
    ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
    所以[1 2 3 4 5].next實際上就是[2 3 4 5]

說明:
1. 對Node進行增加或修改時，通常是對(某個Node).next下指令
    如:
        增加一個Node到尾端: (倒數第二個Node).next = newNode
        刪除一個Node到尾端: (倒數第二個Node).next = None
2. 最後要return整個鏈表就要return第一個Node(head)
3. 找到鍊表中的特定位置可以使用以下Pattern
        對head的部分進行處理(因為沒有head沒有上一個node讓他next)
        currentNode = head
        while 特定位置的否定條件:    (例如: 用ctr找特定位置 -> ctr != N-1，最後的位置可以用None -> currentNode.next != None)
            currentNode = currentNode.next
        (進行目標操作)  
        return head
4. 如果要slice，例:[1 2 3 4 5]保留[1 2 3 5]
        先用第二點中，while配合currentNode = currentNode.next到達currentNode指向Node3
        利用宣告變數的方式暫存某段的鏈表
        first3Nodes = currentNode
        forthNode = currentNode.next 
        first3Nodes.next = forthNode.next
        最後return head
5. 若沒有宣告class SingleLinkedList(包含head、tail等)，一個已宣告的linkedList可直接對其操作，因為會直接指向第一個node
"""

class Node:
    def __init__(self ,data=None, next=None):
      self.val = data
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
                
            
            
