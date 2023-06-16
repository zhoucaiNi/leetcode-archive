class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)
     
        mid = (l + r ) // 2 
        
        while l != r:
            print(mid)
            curr = nums[mid]
            if target > curr:
                l = mid + 1
            elif target < curr:
                r = mid
            else: 
                return mid
            mid = (l + r ) // 2
            
        return -1
        