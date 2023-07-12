class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        output = []
        cycle, seen = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            cycle.remove(crs)
            seen.add(crs)
            output.append(crs)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        return output