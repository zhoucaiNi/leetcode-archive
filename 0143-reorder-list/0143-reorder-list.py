# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find the middle 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow = the middle
        
        # reverse the slow list
        curr = slow.next 
        prev = slow.next = None
        # print(slow.val)
        while curr:
            tmp = curr.next
            curr.next = prev
            
            prev = curr
            curr = tmp
            
        # join the two list 
        
        list1, list2 = head, prev
        
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            
            list1 = tmp1
            list2 = tmp2
            
            
        
        