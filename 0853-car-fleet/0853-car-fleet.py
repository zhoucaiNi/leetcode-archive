class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            distance = target - p
            if not stack:
                stack.append(distance / s)
            elif distance /s > stack[-1]:
                stack.append(distance/s)
    
        return len(stack)
        