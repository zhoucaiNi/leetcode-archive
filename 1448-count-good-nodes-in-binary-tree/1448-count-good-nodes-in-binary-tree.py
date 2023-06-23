# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(d, maxVal):
            if not d:
                return 0
            
            if d.val >= maxVal:
                res = 1
            else:
                res = 0
                
            maxVal = max(maxVal, d.val)
            res += dfs(d.left, maxVal)
            res += dfs(d.right, maxVal)
            
            return res
        
        return dfs(root, root.val)
        
                
        
        