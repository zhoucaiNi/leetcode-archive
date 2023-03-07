class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's algo
        t = k = nums[0]
        for i in nums[1:]:
            t = max(i, t+i)
            k = max(k, t)
        return k

