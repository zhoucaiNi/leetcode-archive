class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIndex, maxIndex = 0,0
        minValue, maxVlaue = float("inf"), float("-inf")

        for i in range(len(nums)):
            if nums[i] < nums[minIndex]:
                minIndex = i
                minValue = nums[i]
            if nums[i] > nums[maxIndex]:
                maxIndex = i
                maxValue = nums[i]

        left,right = min(minIndex, maxIndex), max(minIndex, maxIndex)
        print(left,right)

        return min(right + 1, len(nums) - left, left + 1 + (len(nums) - right))
        