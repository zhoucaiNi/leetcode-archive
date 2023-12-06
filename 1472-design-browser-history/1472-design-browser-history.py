class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.current = 0
        print(self.history)
        

    def visit(self, url: str) -> None:
        self.history = self.history[0:self.current+1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        x = min(self.current, steps)
        print(self.history)
        self.current = self.current-x
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        x = min(len(self.history)- 1 - self.current, steps)
        self.current = self.current + x
        return self.history[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)