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
            elif char in d.keys():
                if stack == [] or d[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
                