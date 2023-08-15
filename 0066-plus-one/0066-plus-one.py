class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        for i in range(len(digits)+1):
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
            else:
                digits.append(1)
                break
                
        return digits[::-1]
        