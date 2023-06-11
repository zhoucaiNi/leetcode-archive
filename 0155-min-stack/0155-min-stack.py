class MinStack(object):

    def __init__(self):
        self.q = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        currMin = self.getMin()
        if currMin == None or val < currMin:
            currMin = val
        self.q.append((val, currMin))
        
        
        

    def pop(self):
        """
        :rtype: None
        """
        self.q.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.q ) == 0:
            return None
        
        return self.q[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        
        return self.q[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()