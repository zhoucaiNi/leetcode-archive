class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, area = 0, len(height)-1, 0
        
        while l <r:
            area = max(area, min(height[l],height[r]) * abs(r-l))
            if height[l] >= height[r]:
                r-=1
            else:
                l+=1
        return area
            