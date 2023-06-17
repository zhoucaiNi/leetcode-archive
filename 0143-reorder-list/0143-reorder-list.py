# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
#         step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # step 2: reverse the second list
        prev, curr = None, slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None
        
        # step 3: join list
        list1, list2 = head, prev
        while list1 and list2:
            next1 = list1.next
            next2 = list2.next
            
            list1.next = list2
            list2.next = next1
            
            list1 = next1
            list2 = next2
            
        
            