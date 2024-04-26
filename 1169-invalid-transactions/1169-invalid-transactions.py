class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transDict, invalid = {}, []
        
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            time = int(time)
            
            if time not in transDict:
                transDict[time] = {name: [city]}
            else:
                # bro wtfffff
                if name not in transDict[time]:
                    transDict[time][name] = [city]
                else:
                    transDict[time][name].append(city)

        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            
            if int(amount) >1000:
                invalid.append(transactions[i])
                continue
            time = int(time)
            for j in range(time-60, time+61):
                if j not in transDict: continue
                if name not in transDict[j]: continue
                    
                if len(transDict[j][name]) > 1 or transDict[j][name][0] != city:
                    invalid.append(transactions[i])
                    break
        
        return invalid