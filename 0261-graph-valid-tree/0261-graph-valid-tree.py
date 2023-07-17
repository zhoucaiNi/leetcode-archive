class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        par = [i for i in range(n)]
        print(par)
        rank = [1] * n
        count = n
            
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            print("parent of " + str(n) + " is " + str(p))
            return p
        
        def union(n1, n2):
            nonlocal count
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            else:
                if rank[p1] < rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
                count-=1
                return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
            
        return True if count == 1 else False
            
            
            
        