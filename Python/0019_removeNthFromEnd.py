"""
My ans
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def lenOfLL(self, LL):
        ctr = 1
        curNode = LL
        while curNode.next != None:
            curNode = curNode.next
            ctr += 1
        return ctr

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lenLL = self.lenOfLL(head)
        del_idx = lenLL - n

        if del_idx == 0 and lenLL == 1: #把整個鏈表刪光的case，所以抓出來當特例
            return ListNode().next #直接輸出ListNode()會輸出默認值為0，.next才會是None

        elif del_idx == 0: #刪掉head的case，前面沒人next等於head，所以抓出來當特例
            return head.next

        elif del_idx == lenLL-1: #刪掉tail的case，因為tail後沒有其他Node需要接回前面的鏈表，所以抓出來當特例
            curNode = head
            while curNode.next != None:
                NodeLeft = curNode
                curNode = curNode.next
            NodeLeft.next = None
            return head

        elif del_idx > 0 and del_idx < lenLL-1: 
            ctr = 0
            curNode = head
            while ctr != del_idx - 1: #curNode指向被刪除的元素的上一個Node時跳出迴圈
                curNode = curNode.next
                ctr += 1                            
            NodeLeft = curNode         
            DelNode = curNode.next
            NodeLeft.next = DelNode.next

        return head
