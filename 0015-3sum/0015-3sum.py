class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        
        n,p,z = [],[],[]
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
                
        N,P = set(n), set(p)
        
        if z:
            for i in P:
                if -i in N:
                    res.add((0, i, -i))
                            
        
        if len(z) >= 3:
            res.add((0,0,0))
            
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                twoSum = p[i] + p[j]
                if -twoSum in N:
                    res.add(tuple(sorted([p[i], p[j], -twoSum])))
                    
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                twoSum = n[i] + n[j]
                if -twoSum in P:
                    res.add(tuple(sorted([n[i], n[j], -twoSum])))
        return res
            