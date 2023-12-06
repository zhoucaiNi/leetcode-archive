class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mainDict = collections.defaultdict(int)
        for domain in cpdomains:
            count, d = (domain.split(" "))
            print(count)
            dList = d.split(".")
            track = ""
            for i in range(len(dList)-1, -1, -1):
                if track != "":
                    track = dList[i] +"."+ track
                else:
                    track = dList[i]
                    
                mainDict[track] += (int(count))
        res = []
        for t in mainDict.items():
            res.append(str(t[1]) + " " + str(t[0]))
            
        return res