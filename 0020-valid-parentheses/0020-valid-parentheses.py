class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {"]":"[", "}":"{", ")":"("}
        
        for char in s:
            if char in d.values():
                stack.append(char)
            elif stack == [] or d[char] != stack.pop() :   
                return False
        return stack == []
                