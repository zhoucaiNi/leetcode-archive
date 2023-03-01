class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict1:
                return [dict1[complement], i]
            else:
                dict1[nums[i]] = i
        return []