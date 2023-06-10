class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, pre, suf = [1] * len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1 -i] *= suf
            suf *= nums[-1 -i]
        return ans

        