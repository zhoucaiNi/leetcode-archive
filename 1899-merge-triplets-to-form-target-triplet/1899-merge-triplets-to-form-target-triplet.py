class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        
        for triple in triplets:
            if triple[0] > target[0] or triple[1] > target[1] or triple[2] > target[2]:
                continue
            
            for i in range(3):
                # print(triple[i], target[i])
                if triple[i] == target[i]:
                    good.add(i)
            
        # print(good)
        return len(good) == 3 