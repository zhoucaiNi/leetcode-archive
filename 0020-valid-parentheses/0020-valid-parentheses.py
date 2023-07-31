class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for c in s:
            if c not in valid:
                stack.append(c)
                continue
            if not stack or stack[-1] != valid[c]:
                return False
            stack.pop()
            
        print(stack)
        return not stack
            
            