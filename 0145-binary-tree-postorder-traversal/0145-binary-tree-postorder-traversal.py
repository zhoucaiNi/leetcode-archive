# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            dfs(node.right)

            self.res.append(node.val)
            
        dfs(root)
        return self.res
        
        
        
        
            
            
        
    
            