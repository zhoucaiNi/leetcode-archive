from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict()
        
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
        
        return(list(d.keys())[:k])