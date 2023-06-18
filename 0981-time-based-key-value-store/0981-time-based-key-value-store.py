class TimeMap(object):
    

    def __init__(self):
        self.timeMap = {}
        
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.timeMap:
            self.timeMap[key] = []
            
        self.timeMap[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        theList = self.timeMap.get(key, [])
        res = ""
        if theList:
            l, r = 0, len(theList) - 1
            while l <= r:
                mid = l + ((r-l) // 2)

                if theList[mid][1] <= timestamp:
                    res = theList[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1

        return res
        
            
            
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)