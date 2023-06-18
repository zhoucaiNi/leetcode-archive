# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev, stack, placeholder = None, [], head
        while head:
            stack.append(head)
            head = head.next
            
        while stack and n > 1:
            prev = stack.pop()
            n-=1
            
        stack.pop()
        if stack: 
            stack.pop().next = prev
        else:
            return prev
        return placeholder
        
            
            
        