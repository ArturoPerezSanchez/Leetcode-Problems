# https://leetcode.com/problems/design-browser-history

class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.ind = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        if(self.ind+1 == len(self.stack)): self.stack.append(url)
        else: self.stack[self.ind+1] = url
        self.ind +=1
        self.bound = self.ind

    def back(self, steps: int) -> str:
        self.ind = max(self.ind-steps, 0)
        return self.stack[self.ind]

    def forward(self, steps: int) -> str:
        self.ind = min(self.ind+steps, self.bound)
        return self.stack[self.ind]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)