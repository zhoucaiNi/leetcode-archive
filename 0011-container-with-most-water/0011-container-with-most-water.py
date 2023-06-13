class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, area = 0, len(height)-1, 0
        
        while l <r:
            if height[l] >= height[r]:
                temp = height[r] * (r-l)
                r-=1
                
            else:
                temp = height[l] * (r-l)
                l+=1
            if temp > area: area = temp
                
        return area
            