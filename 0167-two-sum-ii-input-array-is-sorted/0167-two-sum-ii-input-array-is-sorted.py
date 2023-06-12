class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[r] + numbers[l]
            if  s == target:
                return[l+1,r+1]
            elif s < target:
                l+=1
            elif s > target:
                r-=1
                
        return None
        