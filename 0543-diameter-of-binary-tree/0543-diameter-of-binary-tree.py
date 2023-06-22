# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0 
        
        def dfs(p):
            if not p: return 0
            left = dfs(p.left)
            right = dfs(p.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
        