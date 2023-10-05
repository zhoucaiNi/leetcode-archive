class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = set()
        i = 0
        while i < len(nums):
            if nums[i] in t:
                nums.remove(nums[i])
                i-=1
            else:
                t.add(nums[i])
            i+=1

        return len(nums)