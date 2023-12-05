class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        minLength = len(strs[0])
        
        for i in range(1, len(strs)): 
            print(res)
            minLength = min(minLength, len(strs[i]), len(res))
            tempRes = res
            for j in range(minLength -1, -1, -1):
                if res[j] != strs[i][j]:
                    tempRes = res[0:j]
            res = tempRes[0:minLength]
        return res
        