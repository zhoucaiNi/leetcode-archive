class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        pre = '.'.join(str(len(x)) for x in strs)
        return pre + "#" + "".join(strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        before, after = s.split("#", 1)
        part = before.split(".")
        res = []
        t = 0
        for i in part:
            i = int(i)
            res.append(after[t:t+i])
            t+= i
        return res
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))