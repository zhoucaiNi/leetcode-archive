class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
    

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        
        self.least, self.most = Node(0,0), Node(0,0)
        
        self.least.next, self.most.prev = self.most, self.least
        
    def insert(self, node):
        currRecent, most = self.most.prev, self.most
        currRecent.next = most.prev = node
        node.prev, node.next = currRecent, most
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = (Node(key,value))
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            LRU = self.least.next
            self.remove(LRU)
            del self.cache[LRU.key]
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)