class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1,-1):
            if digits[i] + 1 == 10:
                digits[i] = 0
                if i == 0:
                    temp = digits
                    digits = [1]
                    for i in temp:
                        digits.append(i)
            else:
                digits[i] += 1
                break
                
        return digits
        