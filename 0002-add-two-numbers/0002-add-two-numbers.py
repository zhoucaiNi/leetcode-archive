# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        resNode = ListNode()
        currNode = resNode        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            
            valSum = val1 + val2 + carry 
            carry = valSum // 10
            val = valSum % 10
            
            currNode.next = ListNode(val)
            
            currNode = currNode.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return resNode.next
        
        