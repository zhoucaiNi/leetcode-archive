class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                r, l = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(l+r)
                elif i == "*":
                    stack.append(l*r)
                elif i == "-":
                    stack.append(l-r)
                else:
                    stack.append(int(float(l) / r))
        return stack.pop()