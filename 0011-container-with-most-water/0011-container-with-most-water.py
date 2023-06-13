class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        
        area = 0
        
        while l <r:
            area = max(area, min(height[l],height[r]) * abs(l-r))
            if height[l] >= height[r]:
                r-=1
            else:
                l+=1
        return area
            