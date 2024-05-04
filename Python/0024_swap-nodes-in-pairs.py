"""
Ans
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:   # 建立nest停止條件，head == None為上一組剛好完成交換後就無Node(偶數個Node)
                                                # head.next == None則為剛好還剩一個(奇數個Node)
            return head                         # 最後將剩下的部分回傳

        swapNode1 = head                # 交換Node(前):第1個
        swapNode2 = head.next           # 交換Node(後):第2個
        connectNode = head.next.next    # 被交換的Node後面的Node:第3個

        swapNode2.next = swapNode1      #交換
        #swapNode1.next = connectNode    原來應該要像這樣，然後connectNode變成下一輪的swapNode1也就是head進行交換，所以這裡呼叫自己(nest)
        swapNode1.next = self.swapPairs(connectNode)

        return swapNode2


"""
Ans2
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)        #建立一個Dummy來當作頭讓他去接整個鏈表 -> Dummy,1 ,2 ,3 ,4...
        dummy.next = head
        prev = dummy

        while head and head.next:    #建立交換迴圈停止條件，理由同上面解法
            first_node = head
            second_node = head.next

            prev.next = second_node    # 讓前面的Nodes接上這輪，prev為上一輪最後的Node
            first_node.next = second_node.next
            second_node.next = first_node

            # Move to the next pair of nodes
            prev = first_node
            head = first_node.next

        return dummy.next
        
