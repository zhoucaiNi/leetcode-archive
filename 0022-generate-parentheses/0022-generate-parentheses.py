class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def tree(left, right, string):
            if len(string) == 2* n:
                res.append(string)
                return
            if left < n:
                tree(left+1, right, string+"(")
            if right < left:
                tree(left, right+1, string+")")
           
            
        
        tree(0,0,'')
        return res
        