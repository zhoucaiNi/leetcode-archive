# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return 
            
            res.append(str(root.val))
                
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        # print(",".join(res))
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        i = [0]
        
        def dfs(): 
            if vals[i[0]] == "N":
                i[0]+=1
                return None
            node = TreeNode(int(vals[i[0]]))
            i[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))