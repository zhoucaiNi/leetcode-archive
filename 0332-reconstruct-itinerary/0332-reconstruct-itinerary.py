class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = {}
        res = ["JFK"]
        tickets.sort()
        
        for ticket in tickets:
            if ticket[0] in adjList:
                adjList[ticket[0]].append(ticket[1])
            else:
                adjList[ticket[0]] = [ticket[1]]
                    
        # print(adjList)
        
        def dfs(city):
            if len(res) == len(tickets) + 1:
                return True
            if city not in adjList:
                return False
            
            temp = list(adjList[city])
            
            for i, v in enumerate(temp):
                adjList[city].pop(i)
                res.append(v)
                if dfs(v): return True
                adjList[city].insert(i,v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
            