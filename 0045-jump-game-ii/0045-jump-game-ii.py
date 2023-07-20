class Solution:
    def jump(self, nums: List[int]) -> int:
        row = [None] * len(nums)
        row[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i+j < len(row) and row[i+j] != None:
                    if row[i] == None:
                        row[i] = 1 + row[i+j]
                    else:
                        row[i] = min(row[i], row[i+j]+1)
        return row[0]
        