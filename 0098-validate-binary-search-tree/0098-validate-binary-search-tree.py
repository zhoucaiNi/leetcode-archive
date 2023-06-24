# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root, left, right):
            if not root:
                return True
            if not(root.val > left and root.val < right):
                return False
            
            leftValid = valid(root.left, left, root.val)
            rightValid = valid(root.right, root.val, right)
            
            return leftValid and rightValid
        
        return valid(root, float("-inf"), float("inf"))
        