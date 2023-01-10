# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.aux = []

    def push(self, val: int) -> None:
        self.aux.append(val)

    def pop(self) -> None:
        return self.aux.pop()

    def top(self) -> int:
        return self.aux[-1]

    def getMin(self) -> int:
        return min(self.aux)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()