class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res, stack = [0] * len(T), []
        
        for index, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                res[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return res