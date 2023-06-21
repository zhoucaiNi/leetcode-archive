# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKthNode(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            
            groupPrev = self.reverseList(groupPrev, groupPrev.next, kth, groupNext)
            # return (groupPrev)
            
        return dummy.next
        
    def reverseList(self, groupPrev, groupStart, groupEnd, groupNext):
        prev, curr = groupNext, groupStart
        
        while curr != groupNext:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        tmp = groupPrev.next
        groupPrev.next = groupEnd
            
        return tmp
        
        
        
    def getKthNode(self, head, k):
        while head and k > 0:
            head = head.next
            k-=1
        return head
      
    