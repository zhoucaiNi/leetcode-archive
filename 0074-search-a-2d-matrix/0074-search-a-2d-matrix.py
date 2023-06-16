class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i])-1
            while l <= r:
                m = l+ ((r-l) // 2)
                if target < matrix[i][m]:
                    r = m - 1
                elif target > matrix[i][m]:
                    l = m + 1
                else:
                    return True
                
        return False
        