# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 <len(lists) else None
                mergedList.append(self.merge2Lists(list1, list2))
            lists = mergedList
        
        
        return lists[0]
        
        
    def merge2Lists(self, list1, list2):
        temp = ListNode()
        head = temp
        
        while list1 and list2:
            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next
        
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
            
        return head.next