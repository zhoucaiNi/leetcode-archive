class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = collections.deque()
        l, r = 0,0
        while r < len(nums):
            # if index is 
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # only append if num is greater than 
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            # next
            if (r+1) >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
            # print(q)
        return res
            
        
        
        
            
        