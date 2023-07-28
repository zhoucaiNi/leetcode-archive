class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (float)(n + 1) / 2
        print(total)
        return int(total - sum(nums))
        