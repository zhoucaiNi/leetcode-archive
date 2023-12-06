class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c_counter = Counter() 
        
        prev_ch = {
            "c":'k',
            "r":'c',
            'o':'r',
            'a':'o',
            "k":'a'
        }
        
        for char in croakOfFrogs:
            p_ch = prev_ch[char]
            
            if c_counter[p_ch] > 0:
                c_counter[p_ch] -= 1
                c_counter[char] += 1
            elif char == "c":
                c_counter[char] += 1
            else:
                return -1
            
        for char, count in c_counter.items():
            if char != "k" and count > 0:
                return -1
            
        return c_counter['k']
        