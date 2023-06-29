class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(idx, subset, curr):
            # base case 
            print(idx)
            if curr == target:
                res.append(subset[::])
                return 
            
            # if it goes over
            if idx == len(candidates) or curr + candidates[idx] > target:
                return
            
            subset.append(candidates[idx])
            backtrack(idx + 1, subset, curr + candidates[idx])
            subset.pop()
            
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
                
            backtrack(idx + 1, subset, curr)
            
        backtrack(0, [], 0)
        
        return res
            
            
            
        