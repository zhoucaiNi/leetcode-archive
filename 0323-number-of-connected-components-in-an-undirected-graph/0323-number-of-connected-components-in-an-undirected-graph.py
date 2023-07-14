class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        print(rank)
        count = n
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(e1,e2):
            nonlocal count
            p1,p2 = find(e1), find(e2)
            
            if p1 == p2:
                return 
            else:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
                count-=1
                
        for e1, e2 in edges:
            union(e1, e2)
            
        return count
                
        