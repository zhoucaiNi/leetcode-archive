class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#       find the cycle
        slow, fast = 0 ,0 
        print(slow,fast)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow,fast)
            if slow == fast:
                break
                
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
            
        
        return slow