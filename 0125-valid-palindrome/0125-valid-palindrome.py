class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        real_s = ""
        for char in s:
            if char.isalnum():
                stack.append(char.lower())
                real_s += char.lower()
            
        t = ""
        while stack:
            t = t+ stack.pop()
    
        return t == real_s