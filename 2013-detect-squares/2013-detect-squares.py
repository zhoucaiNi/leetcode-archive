class DetectSquares:

    def __init__(self):
        self.ptMap = defaultdict(int)
        self.values = []

    def add(self, point: List[int]) -> None:
        self.ptMap[tuple(point)] += 1
        self.values.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.values:
            if abs(px - x) != abs(py-y) or px == x or py == y:
                continue
                
            res += self.ptMap[(x,py)] * self.ptMap[(px, y)]
                             
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)